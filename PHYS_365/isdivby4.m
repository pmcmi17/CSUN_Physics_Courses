function logicalval = isdivby4(num)
% Takes an integer and determines if that integer is divisible by 4.

logicalval = logical(0==rem(num,4));
end

