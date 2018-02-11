%This is the example problem from the uploaded pdf on numerical methods.
%Uses ode45 to find the solution of the differential equation, given the
%initial conditions of 1<=t<=3 and y = 4.2
[t, y] = ode45(@ODEexp,(1:0.01:3),4.2);
plot(t,y)
xlabel('t')
ylabel('y')
title('Solution to the first order differential equation: (t^3-2*y)/t')