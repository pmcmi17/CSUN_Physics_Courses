function [code] = name_dept_to_code(name,dept)
% Takes a name and a department, and returns a 4 letter upper case code
% which consists of the first two letters of the name and the last two
% letters of the department.
break_name = upper(strtok(name,name(3)));
[~,dept_end] = strtok(dept,dept(length(dept)-1));
dept_end = upper(dept_end);
code = [break_name dept_end];
end

