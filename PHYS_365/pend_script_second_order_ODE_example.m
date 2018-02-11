c = 9.81;
while 1 == 1
    y1 = 0;
    yp1 = input('enter a value for yp1: (e.g. 1). To end, let yp1 = 0.\n');
    if yp1 == 0
        break
    end
    Y_initial = [y1 yp1];
    options = odeset('abstol',1e-8,'reltol',1e-8);
    [T,Y] = ode45(@pend, [0 5],Y_initial,options);
    plot(T,Y)
    title('y'' = -c*sin(y)')
    xlabel('time')
    legend('y','yp')
    grid on
end