function [root1,root2] = Real_roots(a,b,c)
% Takes the coefficients a, b, and c of a quadratic equation 
% (of the form ax^2 + bx + c). Finds the discriminant D using a nested
% function, and returns the roots (if real).
    function [D] = discriminant(a,b,c)
        D = (b ^ 2 -(4 * a * c));
    end
D = discriminant(a,b,c);
if D < 0 
    fprintf('Error. Roots are not real.\n')
    root1 = 'Imaginary';
    root2 = 'Imaginary';
else
    root1 = (- b + sqrt(D)) / ( 2 * a);
    root2 = (- b - sqrt(D)) / ( 2 * a);
end
end

