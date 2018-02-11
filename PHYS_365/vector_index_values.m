% Prompts the user for a vector. The script will then take the vector and
% display the index of each vector element, and the value of the element in
% sentence form. 

vector = input('Please enter your vector: \n');

for index = 1:length(vector)
    n = vector(index);
    fprintf('Element %d of your vector is %f. \n', index, n);
end
