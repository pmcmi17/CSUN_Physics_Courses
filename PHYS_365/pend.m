function Yp = pend(t,Y)
% ODE of a pendulum
    c = 9.81;
    dydt = Y(2);
    dypdt = -c*sin(Y(1));
    Yp = [dydt dypdt]';
end

