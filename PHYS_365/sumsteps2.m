function [sumstep2] = sumsteps2(n)
% Takes an integer argument 'n' to sum from 1 to 'n' in steps of 2. Meaning
% summing all odd numbers from 1 to n.
for ind = 1:n
    values = 1:2:n;
    sumstep2 = sum(values);
end
    
end

