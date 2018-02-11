% Script used to calculate the area of a triange. Prompts the user for
% three coordinates in two dimensional space which correspond to the
% vertices of the triangle. Coordinates must be entered as a MATLAB
% vector. Calls a function calc_area, which calls on a sub-function 
% get_dist to find the lengths of the sides of the triangle. 

a = input('Please enter the coordinates of the first vertex of a triangle:');
b = input('Please enter the coordinates of the second vertex of a triangle:');
c = input('Please enter the coordinates of the third vertex of a triangle:');

area = calc_area(a,b,c);

fprintf('Here is the area of your triangle: %f\n',area);