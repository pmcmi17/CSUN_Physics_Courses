function [average] = matrix_average(mat)
% Takes a two dimensional matrix, and uses 'for' loops to calculate the average of all the
% values in the matrix. 
number_of_values = size(mat,1) * size(mat,2);
total_sum = 0;
for index_1 = 1:size(mat,1)
    for index_2 = 1:size(mat,2)
        total_sum = total_sum + mat(index_1,index_2);
    end   
end
average = total_sum / number_of_values;
end

