function array_out = exponential(x,tau)
% Takes a vector x and value for tau and creates a new vector y which is
% composed of the exponential value from the input paramenters.

A = 1;
array_out = A*exp((-1).*x./tau);


end

