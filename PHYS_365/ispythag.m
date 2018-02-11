function logicalval = ispythag(a,b,c)
% Takes three positive integers and determines if the set of the integers
% forms a pythagorean triple (i.e. if a, b, and c satisfy a^2+b^2=c^2).


val = a^2+b^2;

logicalval = logical(c^2==val);

end

