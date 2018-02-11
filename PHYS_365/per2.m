function [running_sum] = per2(num)
% Creates a persistent variable 's', used to calculate a running sum of
% arguments passed into the function.
persistent s
if isempty(s)
    s = 0;
end
s = s + num;
running_sum = s;
end

