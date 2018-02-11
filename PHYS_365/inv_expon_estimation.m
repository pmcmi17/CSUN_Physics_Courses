% Loops through values of n until (1-(1/n))^n = e^(-1) up to four decimal
% places. Uses the built-in value of e^(-1) for this condition, and prints
% the value of n needed for such an approximation, and prints the value of
% e^(-1) used for the comparison.

n = 0;
while abs(round(exp_est*10000)/10000 - round((exp(1)^(-1))*10000)/10000) > 0.00001
    exp_est = (1-(1/n))^n;
    n = n+1;
end
fprintf('The value of n needed to approximate e^(-1) to four decimal places is %d. \n', n);
fprintf('The estimated value of e^(-1) using this n is %f. \n', exp_est)
fprintf('The value of e^(-1) is %f. \n', exp(1)^(-1));