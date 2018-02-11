function [sig_naught,k] = stress_eq(d,sig_y)
% Creates the sub function ssq_stress_fit which is the function to be
% fitted. Fits the input data to the fuction, and finds the parameters
% 'sig_naught' and 'k' which give the line of best fit. Additionally, will
% use linear and cubic interpolation to estimate the yield stress at a
% specific input value.
    function [f,Y_theo] = ssq_stress_fit(P,d,sig_Y)
        Y_theo = P(1)+P(2)*d.^(-1/2);
        f = sum((sig_Y-Y_theo).^2);
    end
opti = optimset('TolX', 1e-10);
params = fminsearch(@(P)ssq_stress_fit(P,d,sig_y),[0 0],opti);
sig_naught = params(1);
k = params(2);
Estim_by_eq = sig_naught + k*0.005^(-1/2);
fprintf('Using our fitted equation, the yield stress of a material with size 0.005 mm is %f.\n',Estim_by_eq)
sig_y_fit = sig_naught+k*d.^(-1/2);
yi_lin_interp = interp1(d,sig_y,0.005,'linear');
fprintf('Using linear interpolation, the yield stress of a material with size 0.005 mm is %f.\n',yi_lin_interp)
y_lin_interp = interp1(d,sig_y,linspace(0,0.12),'linear');
yi_cub_interp = interp1(d,sig_y,0.005,'PCHIP');
fprintf('Using cubic spline interpolation, the yield stress of a material with size 0.005 mm is %f.\n',yi_cub_interp)
y_cub_interp = interp1(d,sig_y,linspace(0,0.12),'PCHIP');
subplot(1,3,1)
scatter(d,sig_y)
title('Yield Stress (Hall-Petch)')
ylabel('Y')
xlabel('X')
hold on
plot(d,sig_y_fit)
subplot(1,3,2)
scatter(d,sig_y)
title('Yield Stress (Linear Interpolation)')
ylabel('Y')
xlabel('X')
hold on
plot(linspace(0,0.12),y_lin_interp)
subplot(1,3,3)
scatter(d,sig_y)
title('Yield Stress (Cubic Spline Interpolation)')
ylabel('Y')
xlabel('X')
hold on
plot(linspace(0,0.12),y_cub_interp)
end