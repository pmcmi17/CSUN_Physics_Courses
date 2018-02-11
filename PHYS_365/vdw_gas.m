function [vol] = vdw_gas
    global P T n a b R
    P = 6; T = 323.2; n = 2; a = 3.59; b = 0.047; R = 0.08206;
    Vol_est = n*R*T/P;
    vol = fzero(@Waals,Vol_est);
end
function fx = Waals(x)
    global P T n a b R
    fx = (P+n^2*a/x^2)*(x-n*b)-n*R*T;
end