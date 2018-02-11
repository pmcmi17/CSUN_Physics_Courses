% Prompts the user for four course numbers. Stores numbers in a character
% matrix of size 4 by 5. (Numbers to be of length 5)
matrix = zeros(4,5);
for i = 1:4
    str = input('Please enter a course number of length 5: \n','s');
    while length(str) ~= 5
        fprintf('Wrong length!\n')
        str = input('Please enter a course number of length 5: \n','s');
    end
    for n = 1:n
        matrix(i,n) = str(n);
    end
end
matr = char(matrix);
disp(matr)