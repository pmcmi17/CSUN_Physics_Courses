% Modular program designed to give information and approximations about pi.
% The script has several options. First, to give basic information about
% pi. Second, to give an approximation using Machin's formula. Third,
% to give an approximation using Leibniz's formula, prompting the user for
% an unput for the sumber of terms used. Fourth, to use Leibniz's formula
% until an error of 0.0001 is achieved, printing the value and the number
% of terms needed to get such a result. Finally, an option is presented to
% exit the program without any action being taken.

ch = menu('PI','Information about pi','Machin approximation of pi','Lebniz approximation of pi to a user entered number of terms',' "good" Leibniz approximation','Exit');
while ch ~= 5
    if ch == 1
        fprintf('Pi is an irrational number which is the ratio of the circumfrence of a circle to the diameter. Pi is usually reported as 3.14\n')
    elseif ch == 2
        mach_app = machin_approx;
        fprintf('Here is the Machin approximation of pi to 6 decimal places: %.6f \n',mach_app)
    elseif ch == 3
        [app,n] = leibniz_approx(3);
        fprintf('Here is your approximation of pi to 6 decimal places using Leibniz approximation with %d terms: %.6f\n',n,app)
    elseif ch == 4
        [app,n] = leibniz_approx(4);
        fprintf('Here is the "good" approximation of pi to 6 decimal places using Leibniz approximation: %.6f. This is found using %d terms.\n',app,n)
    end
    ch = menu('PI','Information about pi','Machin approximation of pi','Lebniz approximation of pi to a user entered number of terms',' "good" Leibniz approximation','Exit');
end
fprintf('Exiting the program.\n')