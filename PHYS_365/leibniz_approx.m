function [app,n] = leibniz_approx(ch)
% Uses Leibniz's approximation to approximate pi to either a user entered
% number of terms, or make a "good" approximation to 0.000001 and report
% the number of terms used.
if ch == 3
    n = input('Please enter the number of terms you would like to use to approximate pi.\n');
    app = 1;
    for ind = 1:n
        if mod(ind,2) == 0
            m = 2;
        else
            m = 1;
        end
        app = app + (-1)^(m) * 1/(2 * ind + 1);
    end
    app = 4 * app;
elseif ch == 4
    n = 0;
    app = 0;
    while abs(round(app*100000)/100000 - round(pi*100000)/100000) > 0.000001
        if mod(n,2) == 0
            m = 2;
        else
            m = 1;
        end
        app = app + (-1)^(m) * 4/(2 * n + 1);
        if abs(round(app*100000)/100000 - round(pi*100000)/100000) > 0.000001
            n = n + 1;
        else
            break
        end        
    end
end

