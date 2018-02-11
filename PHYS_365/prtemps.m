% Prompts the user for a value in degrees Celsius within the range of
% (-16,20). Then checks for a valid input. Creates a table of degrees in
% Celsius and degrees in Fahrenheit from -16 degrees Celsius to the value
% given by the user. (Incements of 5 degrees Fahrenheit are used in the
% table.)
value = input('Enter a value within the range (-16,20): \n');
while value <= -16 || value >= 20
    fprintf('You entered a value outside of the range.\n');
    value = input('Enter a value within the range (-16,20): \n');
end
F = 0;
fprintf('F     C\n')
while F >=0 && F < (9/5)*value+32
    C = (5/9)*(F-32);
    fprintf('%6.1f %6.1f \n',F,C);
    F = F + 5;
end