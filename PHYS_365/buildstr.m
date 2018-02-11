function [cell_of_strings] = buildstr(chara,n)
% Takes a character and a positive integer. 
cell_of_strings = {1:n};
i = 1;
while i <= n
    stri = 0:i;
    for ind = 1:i
        stri(ind) = chara+ind;
    end
    cell_of_strings{1} = chara;
    cell_of_strings{i+1} = [chara char(stri)];
    i = i + 1;
end
end

