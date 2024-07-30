%% generate pdf for gaussian with generalized gamma variances
%matlab.engine.shareEngine
%% set parameters
function res = compute_cdf(r,eta)
    
    beta = (eta + 1.5)/r; % change to standard parametrization
    scale = 1;

    
    %% pick discretization range and scale
    n_samples = 10^3;
    x_max = 100;
    xs = linspace(-x_max,x_max,n_samples);
    
    
    %% preallocate
    prior_pdf = nan(size(xs));
    
    %% loop over xs
    
    
        %% define integrands
    syms x theta
    gauss_density = (1/(sqrt(2*pi)*sqrt(theta))).*exp(-0.5*(x^2)/theta);
    gen_gamma_density = (abs(r)/gamma(beta))*(1/scale)*(theta/scale).^(r*beta - 1).*...
        exp(-(theta/scale).^r);
    %% integrate
    first_int = vpaintegral(vpaintegral(gauss_density * gen_gamma_density,theta,0, Inf), x, -Inf, Inf);
    res = first_int;




