function random_row(matrix)
% Takes a matrix, and prints a random row of the matrix to the command
% line.
a = size(matrix,2);
n = randi([1 a],1,1);
disp(matrix(n,:))
end

