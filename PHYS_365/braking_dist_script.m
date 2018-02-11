% This script calculates braking distance of a car given the car's speed 
% and it's braking efficency. This script is designed to call three 
% functions. One for asking for an input for the speed of a car and it's 
% braking efficency. One for calculating the braking distance, and one for 
% printing the calculated braking distance.

[s,R] = promptSandR();
brakDist = calcbd(s,R);
printbd(brakDist)