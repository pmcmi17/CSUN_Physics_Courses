y1 = 0;
yp1 = -2;
Y_initial = [y1 yp1]';
options = odeset('abstol',1e-8,'reltol',1e-8);
[X,Y] = ode45(@odefn,[0 3],Y_initial,options);
plot(X,Y)
title('y = sqrt(1+y^2)')
xlabel('x')
legend('y','yp')