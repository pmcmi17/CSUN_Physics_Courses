% Prompts the user for 'n' radii of circles. Calculates the area of each
% circle by calling a function 'calc_area', and writes the area to a file 
% 'circle_areas.dat'.
n = 5;
fid = fopen('circle_areas.dat','a');
if fid == -1
    fprintf('File did not open properly.\n')
else
    fprintf('File opened properly.\n')
end
for i = 1:n
    r = input('Please enter a radius of a circle:\n');
    area = calc_area(r);
    fprintf(fid,'The area of the circle of radius %f is: %f\n',r,area);
end
fid = fclose(fid);
if fid == 0
    fprintf('File closed properly.\n')
else
    fprintf('File did not close properly.\n')
end