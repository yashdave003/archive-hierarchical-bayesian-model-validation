%% generate pdf for gaussian with generalized gamma variances
%matlab.engine.shareEngine
%% set parameters
function res = compute_cdf_using_gengamma(r,eta, x)
    
    beta = (eta + 1.5)/r; % change to standard parametrization
    scale = 1;

    
    
    
    %% define integrands
    gen_gamma_cdf = @(x) gammainc(x.^r, beta);

    gauss_density = @(z) (1./(sqrt(2*pi))).*exp(-0.5*(z.^2));
   
    %% integrate
    
    integrand = @(z) gauss_density(z) .* (1 - gen_gamma_cdf((x./z).^2));
    %integrand = @(z) gauss_density(z);
    res = integral(integrand, -Inf, 0);
    if x > 0
        res = 1 - res;
    end





