% Reads in data from exams.dat. Uses fscanf to make two vectors of exam
% grades. Displays the grades. 
fid = fopen('exams.dat');
if fid == -1
    fprintf('File did not open properly.\n')
else
    fprintf('File opened properly.\n')
    matr = fscanf(fid, '%c %f\n', [2,inf]);
    matA = (matr(1,:)==65);
    matB = (matr(1,:)==66);
    fprintf('Exam A scores:\n')
    disp(matr(2,matA))
    fprintf('Exam B scores:\n')
    disp(matr(2,matB))
end
fid = fclose(fid);
if fid == 0 
    fprintf('File colsed properly.\n')
else
    fprintf('File did not close.\n')
end