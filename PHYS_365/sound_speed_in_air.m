% This script is designed to take a user input of temperature in the range
% of 0 to 50 C, and estimate the speed of sound in air at that temperature.
% If a temperature is given which is outside of the range, the user will be
% shown an error message.

x = input('Please enter a temperature in the range of 0 to 50 Celsius: \n');

if x>0
    if x<50
        
        v = 331 + x*0.6;
        fprintf('The speed of sound in air at %f is %f \n', x, v)
    else
        fprintf('You have entered a temperature outside of the required range. \n The required range is from 0 to 50 Celsius.\n')
    end
else
    fprintf('You have entered a temperature outside of the required range. \n The required range is from 0 to 50 Celsius.\n')
    
end