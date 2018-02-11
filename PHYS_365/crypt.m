function crypt(str)
% Takes a string and finds the first letter of each word in the string
% (separated by white space). Concatenates the letters to form a new string
% which is returned as 'message'.
% Splits string into as many strings as there are words in the original 
% string, and finds the first letter of each. 
C = strsplit(str);
message = zeros(1,size(C,2));
for i = 1:size(C,2)
    c = C{i}(1);
    message(i) = char(c);
end
disp(char(message))
end

