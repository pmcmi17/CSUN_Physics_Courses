function dydt = ODEexp(t,y)
    % Given first order differential equation. Function file for the script
    % 'first_order_ODEexample.m'
    dydt = (t^3-2*y)/t;
end