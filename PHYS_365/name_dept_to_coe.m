function [code] = name_dept_to_coe(name,dept)
% Takes a name and a department, and returns a 4 letter upper case code
% which consists of the first two letters of the name and the last two
% letters of the department.
break_name = upper(strtok(name,name(3)));
break_dept = upper(strtok(dept,dept(length(dept)-2)));
code = [break_name break_dept];
end

