function [logi] = is_filename_str(filename)
% Takes a filename string 'filename' and determines whether or not the 
% filename is a string or not, and if it's extension is 3 characters long. 
% Returns to logical 1 if the filename is a string and the exention is a 
% string and 0 if the filename is not a string. Breaks 'filename' into its 
% name and it's extension to determine this.
[name,extens] = strtok(filename,'.');
if ischar(name) && ischar(extens)
    if length(extens) == 4
        % This must be 4, since the delimiter is included in the split.
        logi = 1;
    else
        logi = 0;
    end
else
    logi = 0;
end
end

