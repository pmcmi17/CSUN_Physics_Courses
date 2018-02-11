% Shows the user a menu of geometric shapes of which the area can be
% calculated. THe user is propted to choose an item, and then is propted
% for the appropriate quantities of the shape. Then teh area of the shape
% is calculated and is displayed.

shape = menu('Shapes','cylinder','circle','rectangle');

if shape == 1
    fprintf('You have selected a cylinder.\n');
    radius = input('Please enter the radius of the cylinder: \n');
    if isfloat(radius) || isinteger(radius)
        height = input('Please enter the height of the cylinder: \n');
        if isfloat(height) || isinteger(height)
            area = height * pi * radius^2;
            fprintf('The area of the specified cylinder is %f. \n', area)
        else
            fprintf('You have entered an improper choice. \n')
        end
    else
        fprintf('You have entered an improper choice. \n')
    end
elseif shape == 2
    fprintf('You have selected a circle.\n');
    radius = input('Please enter the radius of the circle: \n');
    if isfloat(radius) || isinteger(radius)
        area = pi * radius^2;
        fprintf('The area of the specified circle is %f. \n', area)
    else
        fprintf('You have entered an improper choice. \n')
    end
elseif shape == 3 
    fprintf('You have selected a rectangle.\n');
    width = input('Please enter the base of the rectangle: \n');
    if isfloat(width) || isinteger(width)
        height = input('Please enter the height of the rectangle: \n');
        if isfloat(height) || isinteger(height)
            area = width * height;
            fprintf('The area of the specified rectangle is %f. \n', area)
        else
            fprintf('You have entered an improper choice. \n')
        end
    else
        fprintf('You have entered an improper choice. \n')
    end
else
    fprintf('You have entered an improper choice.\n')
end