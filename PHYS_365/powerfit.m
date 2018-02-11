function [b,m] = powerfit(x,y)
% Creates the sub function ssq_expo_fit which is the function needing to be
% fitted to. Fits the input data to the fuction, and finds the parameters
% 'b' and 'm' which give the line of best fit. 
    function [f,Y_theo] = ssq_expo_fit(P,X,Y)
        Y_theo = P(1).*X.^P(2);
        f = sum((Y-Y_theo).^2);
    end
opti = optimset('TolX', 1e-10);
params = fminsearch(@(P)ssq_expo_fit(P,x,y),[0 0],opti);
b = params(1);
m = params(2);
y_fit = params(1).*x.^params(2);
scatter(x,y)
title('Exponential Fit')
ylabel('Y')
xlabel('X')
hold on
plot(x,y_fit)
end