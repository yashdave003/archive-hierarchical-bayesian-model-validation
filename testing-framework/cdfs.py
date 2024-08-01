def compute_prior_pdf(r, eta, method='gamma_cdf', n_samples = 10000, tail_bound = 0.01, tail_percent = 0.1, scale = 1, scipy_int=True, eng= None, debug=False, enforce_assert=True, return_assert=False):
    if method == 'gamma_cdf':
        xs, cdf = compute_prior_cdf_using_gamma_cdf(r=r, eta=eta, n_samples=n_samples, tail_bound=tail_bound, tail_percent=tail_percent, scale=scale, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, return_xs=True)
        return xs, cdf.derivative()
    elif method == 'normal_cdf':
        xs, cdf = compute_prior_cdf_using_normal_cdf(r=r, eta=eta, n_samples=n_samples, tail_bound=tail_bound, tail_percent=tail_percent, scale=scale, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, return_xs=True)
        return xs, cdf.derivative()
    elif method == 'numerical_old':
        return compute_prior_pdf_using_numerical_old(r=r, eta=eta, n_samples=n_samples, tail_bound=tail_bound, tail_percent=tail_percent, scale=scale, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, return_xs=True)

def compute_prior_cdf(r, eta, method='gamma_cdf', n_samples = 10000, tail_bound = 0.01, tail_percent = 0.1, scale = 1, scipy_int=True, eng= None, debug=False, enforce_assert=True, return_assert=False, return_xs=False):

    if method == 'gamma_cdf':
        return compute_prior_cdf_using_gamma_cdf(r=r, eta=eta, n_samples=n_samples, tail_bound=tail_bound, tail_percent=tail_percent, scale=scale, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, return_xs=return_xs)
    elif method == 'normal_cdf':
        return compute_prior_cdf_using_normal_cdf(r=r, eta=eta, n_samples=n_samples, tail_bound=tail_bound, tail_percent=tail_percent, scale=scale, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, return_xs=return_xs)
    elif method == 'numerical_old':
        return compute_prior_cdf_using_numerical_old(r=r, eta=eta, n_samples=n_samples, tail_bound=tail_bound, tail_percent=tail_percent, scale=scale, scipy_int=scipy_int, eng=eng, enforce_assert=enforce_assert, return_assert=return_assert, return_xs=return_xs)

def compute_prior_pdf_using_numerical_old(r, eta, n_samples = 10000, tail_bound = 0.01, tail_percent = 0.1, scale = 1, scipy_int=True, eng= None, debug=False, return_xs=True):

    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma(beta + 1/r)/scipy.special.gamma(beta)
    cheby = np.sqrt(var_prior/(tail_bound))
    n_tail = int(n_samples*tail_percent)
    x_max = min(99, cheby) 
    if cheby < 120:
        n_tail = 0
        if debug:
            print(f"No tail")
    if debug:
        print(f"Chebyshev bound: {cheby}")

    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))

    prior_pdf = np.full(xs.shape, np.nan)

    for j, x in enumerate(xs):

        def integrand(theta):
            return (1./(np.sqrt(2*np.pi)*np.sqrt(theta))) * np.exp(-0.5*(x**2/theta)) * (np.abs(r)/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        if scipy_int:
            prior_pdf[j] = integrate.quad(integrand, 0, np.inf)[0]
        else:
            prior_pdf[j] = eng.compute_prior(float(r), float(eta), float(x), nargout=1)

    if return_xs:
        return xs, prior_pdf
    else:
        return prior_pdf

def pdf_to_cdf_using_numerical_old(xs, prior_pdf, return_assert=False, enforce_assert=True, debug = False):

    prior_cdf = np.zeros_like(prior_pdf)
    prior_cdf[0] = 0
    for i in range(1, len(xs)):
        prior_cdf[i] = (interpolate.CubicSpline(x=xs[:i+1], y=prior_pdf[:i+1])).integrate(xs[0], xs[i])+0

    normalizer = prior_cdf[-1]
    first = prior_cdf[1]

    if debug:
        print("First CDF value:", first)
        print("Last CDF value:", normalizer)

    if return_assert:
        if not 0.05 > first > -0.05:
            return None
        if not 1.05 > normalizer > 0.95:
            return None    

    if enforce_assert:
        assert 0.05 > first > -0.05    
        assert 1.05 > normalizer > 0.95
    
    prior_cdf = prior_cdf/normalizer   

    k = int(0.01*len(xs))
    zero_padding = np.zeros(k)
    ones_padding = np.ones(k)

    pad_max = max(10e5, np.round(max(np.abs(xs)) ** 2))
    if debug:
        print(f"0, 1 padding bounds: {pad_max}")

    prior_cdf_padded = np.concatenate([zero_padding, prior_cdf, ones_padding])
    xs_padded = np.concatenate([
        np.linspace(-pad_max, xs[0] - 1e-5, k),
        xs,
        np.linspace(xs[-1] + 1e-5, pad_max, k)
    ])

    cdf_spline = interpolate.CubicSpline(x=xs_padded, y=prior_cdf_padded)

    if enforce_assert:
        assert np.isclose(cdf_spline(-1e10), 0, atol=1e-8)
        assert np.isclose(cdf_spline(1e10), 1, atol=1e-8)

    return cdf_spline

def compute_prior_cdf_using_numerical_old(r, eta, n_samples=10000, tail_bound=0.01, tail_percent=0.1, scale=1, scipy_int=True, eng=None, enforce_assert=True, return_assert = False, return_pdf=False, debug=False, return_xs=False):
    
    xs, prior_pdf = compute_prior_pdf_using_numerical_old(r = r, eta = eta, n_samples = n_samples, 
                                      tail_bound = tail_bound, tail_percent = tail_percent, 
                                      scale = scale, scipy_int = scipy_int, eng = eng, debug = debug, return_xs=True)
    cdf_spline = pdf_to_cdf_using_numerical_old(xs = xs, prior_pdf = prior_pdf, enforce_assert = enforce_assert, return_assert = return_assert, debug = debug)

    if return_xs:
        if return_pdf:
            return xs, prior_pdf, cdf_spline
        else:
            return xs, cdf_spline
    else:
        if return_pdf:
            return prior_pdf, cdf_spline
        else:
            return cdf_spline

    
def compute_prior_cdf_using_gamma_cdf(r, eta, n_samples = 2000, tail_bound = 0.01, tail_percent = 0.1, scale = 1, scipy_int=True, eng= None, enforce_assert=True, return_assert = False, return_xs=False, debug=False):
    
    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma(beta + 1/r)/scipy.special.gamma(beta)
        
    cheby = np.sqrt(var_prior/(tail_bound))
    if np.isnan(var_prior):
        cheby = 1e100
    n_tail = int(n_samples*tail_percent)
    
    # introduced additional bound in case chebyshev is unwieldy
    x_max = min(99, cheby) 
    if cheby < 120:
        n_tail = 0
        if debug:
            print(f"No tail")
    if debug:
        print(f"Chebyshev bound: {cheby}")

    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))

    prior_cdf = np.full(xs.shape, np.nan)

    if debug:
        loop = tqdm(range(len(xs)))
    else:
        loop = range(len(xs))
    for j in loop:

        x = xs[j]
        # Note that theta = variance, np.sqrt(theta) = SD
        def gauss_density(z):
            return (1/(np.sqrt(2*np.pi)) * np.exp(-0.5*(x**2)))

        def gen_gamma_cdf(x):
            return special.gammainc(beta, x**r)

        def integrand(z):
            return gauss_density(z) * (1-gen_gamma_cdf((x/z)**2))

        if scipy_int:
            res = integrate.quad(integrand, 0, np.inf)[0]
            if x > 0:
                res = 1-res
            prior_cdf[j] = res
        else:
            prior_cdf[j] = eng.compute_cdf_using_gengamma(float(r), float(eta), float(x), nargout=1)
        
    normalizer = prior_cdf[-1]
    first = prior_cdf[1]

    if debug:
        print("First CDF value:", first)
        print("Last CDF value:", normalizer)

    eps = 0.01
    if return_assert:
        if not -eps < first < eps:
            return None
        if not 1 - eps < normalizer < 1 + eps:
            return None    

    if enforce_assert:
        assert -eps < first < eps    
        assert 1 - eps < normalizer < 1 + eps
    
    prior_cdf = (prior_cdf - first)
    normalizer_new = prior_cdf[-1]
    prior_cdf = prior_cdf/normalizer_new

    if cheby > 1e10:
        k = 10
    else:
        k = int(0.01*len(xs))
   
    zero_padding = np.zeros(k)
    ones_padding = np.ones(k)
    
    pad_max = max(10e5, np.round(max(np.abs(xs)) ** 2))
    step_size = (pad_max - xs[0]/2)/k
    
    if debug:
        print(f"0, 1 padding bounds: {pad_max}; Number of 0, 1 nodes, k: {k}")

    prior_cdf_padded = np.concatenate([zero_padding, prior_cdf, ones_padding])
    xs_padded = np.concatenate([
        np.arange(-pad_max, xs[0]/2, step_size),
        xs,
        np.arange(xs[-1] *2, pad_max, step_size)
    ])

    cdf_spline = interpolate.CubicSpline(x=xs_padded, y=prior_cdf_padded, bc_type=((1, 0.0), (1, 0.0)))

    if enforce_assert:
        x = np.sort(sample_prior(r, eta, 100000))
        res = stats.ks_1samp(x, cdf_spline)
        if debug:
            print(res)
        assert 0 <= res.statistic <= 1
        if res.pvalue < 0.01:
            assert np.abs(res.statistic_location) > cheby

    if return_assert:
        x = np.sort(sample_prior(r, eta, 100000))
        res = stats.ks_1samp(x, cdf_spline)
        if debug:
            print(res)
        if not 0 <= res.statistic <= 1:
            return None
        if res.pvalue < 0.01:
            if not np.abs(res.statistic_location) > cheby:
                return None

    if return_xs:
        return xs, cdf_spline
    else:
        return cdf_spline
    
def compute_prior_cdf_using_normal_cdf(r, eta, n_samples = 2000, tail_bound = 0.01, tail_percent = 0.1, scale = 1, scipy_int=True, eng= None, enforce_assert=True, return_assert = False, return_xs=False, debug=False):
    
    beta = (eta + 1.5)/r 
    var_prior = scale * scipy.special.gamma(beta + 1/r)/scipy.special.gamma(beta)
    cheby = np.sqrt(var_prior/(tail_bound))
    n_tail = int(n_samples*tail_percent)
    
    x_max = min(99, cheby) 
    if cheby < 120:
        n_tail = 0
        if debug:
            print(f"No tail")
    if debug:
        print(f"Chebyshev bound: {cheby}")

    xs = np.linspace(-x_max, x_max, n_samples-2*n_tail)
    xs = np.append(-np.logspace(np.log10(cheby), 2, n_tail), xs)
    xs = np.append(xs, np.logspace(2, np.log10(cheby), n_tail))

    prior_cdf = np.full(xs.shape, np.nan)

    for j in tqdm(range(len(xs))):

        x = xs[j]
        def gen_gamma_density(theta):
            return (np.abs(r)/scipy.special.gamma(beta)) * (1/scale) * (theta/scale)**(r*beta - 1) * np.exp(-(theta/scale)**r)

        def integrand(theta):
            return stats.norm.cdf(x/np.sqrt(theta)) * gen_gamma_density(theta)

        if scipy_int:
            prior_cdf[j] = integrate.quad(integrand, 0, np.inf)[0]
        else:
            prior_cdf[j] = eng.compute_cdf_using_phi(float(r), float(eta), float(x), nargout=1)
    
    
    normalizer = prior_cdf[-1]
    first = prior_cdf[1]

    if debug:
        print("First CDF value:", first)
        print("Last CDF value:", normalizer)

    eps = 0.01
    if return_assert:
        if not -eps < first < eps:
            return None
        if not 1 - eps < normalizer < 1 + eps:
            return None    

    if enforce_assert:
        assert -eps < first < eps    
        assert 1 - eps < normalizer < 1 + eps
    
    prior_cdf = prior_cdf/normalizer   

    k = int(0.01*len(xs))
    zero_padding = np.zeros(k)
    ones_padding = np.ones(k)

    pad_max = max(10e5, np.round(max(np.abs(xs)) ** 2))
    if debug:
        print(f"0, 1 padding bounds: {pad_max}")

    prior_cdf_padded = np.concatenate([zero_padding, prior_cdf, ones_padding])
    xs_padded = np.concatenate([
        np.linspace(-pad_max, xs[0] - 1e-5, k),
        xs,
        np.linspace(xs[-1] + 1e-5, pad_max, k)
    ])

    cdf_spline = interpolate.CubicSpline(x=xs_padded, y=prior_cdf_padded)

    if enforce_assert:
        x = np.sort(sample_prior(r, eta, 100000))
        res = stats.ks_1samp(x, cdf_spline)
        if debug:
            print(res)
        assert 0 <= res.statistic <= 1
        if res.pvalue < 0.01:
            assert np.abs(res.statistic_location) > cheby

    if return_assert:
        x = np.sort(sample_prior(r, eta, 100000))
        res = stats.ks_1samp(x, cdf_spline)
        if debug:
            print(res)
        if not 0 <= res.statistic <= 1:
            return None
        if res.pvalue < 0.01:
            if not np.abs(res.statistic_location) > cheby:
                return None
    
    if return_xs:
        return xs, cdf_spline
    else:
        return cdf_spline