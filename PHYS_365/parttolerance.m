% This script reads data from the file parttolerance.dat. Then it prompts 
% the user for the weight of the part. Then, it
% determines if the weight for that part number is in the tolerated range.

load parttolerance.dat;

partweight = input('Enter the weight of the part: \n');

if partweight > parttolerance(2) && partweight < parttolerance(3)
    fprintf('The weight is within the tolerance.\n')
else
    fprintf('The weight is outside the tolerance.\n')
end