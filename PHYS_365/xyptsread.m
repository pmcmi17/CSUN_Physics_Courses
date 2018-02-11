% Opens data file xypts.dat. Tells if file was opened properly. Reads in
% data as a string making vectors for the data. Then plots the data, closes
% the file and tells if the file was closed correctly.

fid = fopen('xypts.dat');
if fid == -1
    fprintf('Unable to open file xypts.dat.\n')
else
    fprintf('File opened successfully.\n')
    xvals = zeros(1,10);
    yvals = zeros(1,10);
    for line = 1:10
        % We use 1:10 because we know the length of the file.
        l = fgetl(fid);
        vals = strsplit(l);
        xvals(line) = str2double(vals(2));
        yvals(line) = str2double(vals(4));
    end
    plot(xvals,yvals)
    title('x vs y')
    xlabel('x')
    ylabel('y')
end
fid = fclose(fid);
if fid ~= 0
    fprintf('File did not properly close.\n')
else
    fprintf('File properly closed.\n')
end