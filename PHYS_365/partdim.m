% Reads diameter vs time data
% plots data

load partdim.dat

time = partdim(:,1);
diam = partdim(:,2);

% Plots

plot(time,diam)
xlabel('Time (s)')
ylabel('Diameter (mm)')
legend('Diameter')
title('Diameter (mm) V Time (s)')