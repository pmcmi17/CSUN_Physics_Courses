function [brakDist] = calcbd(s,R)
% Takes a car's speed when brakes are applied and the braking efficency and
% calculated the braking distance.
g = 9.80;
brakDist = s^2/(2*R*g);
end

