function [mat] = makemat(vec1,vec2)
% This function required two row input vectors, not necessarrily of the same
% length. Given these vectors, it will create a matrix with two rows and n
% columns, where n is the length of the longest vector given. If m is the
% length of the shorter vector, n-m zeros will be added to the end of the
% shorter vector. 

len1 = length(vec1);
len2 = length(vec2);

if len1 == len2
    mat = [vec1;vec2];
elseif len1 > len2
    n = len1-len2;
    m = zeros(1,n);
    vec2 = [vec2,m];
    mat = [vec1;vec2];
elseif len1 < len2
    n = len2 - len1;
    m = zeros(1,n);
    vec1 = [vec1,m];
    mat = [vec1;vec2];
end
end