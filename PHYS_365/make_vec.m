% Preallocates space for a vector of zeros of length 4. Then prompts the user for four
% numbers, which will then replace the zeros in the vector, and print the
% vector to the users screen through the command prompt. 

vector = zeros(1,4);

fprintf('You will be prompted for four numbers, which will be taken and placed into a vector.\n')

for ind = 1:4
    n = input('Please enter a number: \n');
    vector(ind) = n ;
end
fprintf('Your vector is: \n')
disp(vector);