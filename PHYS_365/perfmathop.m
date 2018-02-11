% Reads in file 'mathfile.dat' and then iterates through each line,
% performing the operation and printing the result.

fid = fopen('mathfile.dat');
if fid == -1
    fprintf('File did not open.\n')
else
    fprintf('File opened properly.\n')
    for line = 1:length(mathfile)
        li = fgetl(fid);
        n = eval(li);
        fprintf('%d\n',n)
    end
end
fid = fclose(fid);
if fid == 0
    fprintf('File closed properly.\n')
else
    fprintf('File did not close properly.\n')
end