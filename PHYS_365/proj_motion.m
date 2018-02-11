% Prompts the user for the initial velocity and the angle at which a
% projectile is fired from the horizontal. Takes these parameters and finds
% the range of the projectile, plots the verticle position as a
% function of x, plots the hieght of the projectile as a function of
% time, and calculates the amount of time taken for the projectile to reach
% its maximum height. 
g = 9.81;
v_0 = input('Enter the intial speed of the projectile: \n');
theta_0 = input('Enter the angle the intial velocity makes with the horizontal: \n');

t_roots = roots([-1/2*g v_0*sind(theta_0) 0]);
x_max = v_0*cosd(theta_0)*t_roots(2);
fprintf('The range of the projectile is %f m.\n',x_max)
t_to_y_max = t_roots(2)/2;
fprintf('The time it takes to reach max height is %f s.\n',t_to_y_max)
t = linspace(0,t_roots(2));
x = v_0*cosd(theta_0).*t;
y = -1/2*g.*t.^2 + v_0*sind(theta_0).*t;
subplot(1,2,1)
plot(x,y)
title('Position')
xlabel('x')
ylabel('y')
subplot(1,2,2)
plot(t,y)
title('Height v Time')
xlabel('t')
ylabel('y')