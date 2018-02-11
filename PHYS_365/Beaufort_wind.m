% This script generates a force value on the Beufort Scale (randomly), and
% prints a statement based on the number generated. 

ranforce = randi([0,12]);
if ranforce == 0 
    fprintf('There is no wind.\n')
elseif ranforce > 0 && ranforce <= 6
    fprintf('There is a breeze.\n')
elseif ranforce > 6 && ranforce <= 9
    fprintf('There is a gale.\n')
elseif ranforce > 9 && ranforce < 12
    fprintf('It is a storm.\n')
else
    fprintf('Hello, Hrricane!\n')
end