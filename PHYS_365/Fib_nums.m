function [n] = Fib_nums(n_terms)
% Takes argument 'n_terms'. Find the nth term of the Fibonacci sequence. 
if n_terms == 1
    n = 0;
elseif n_terms == 2
    n = 1;
else
    n = Fib_nums(n_terms-2)+Fib_nums(n_terms-1);
end
end

