function [Oscillator_out] = Oscillator_ODE(t, theta)
% Companion function for 'Chaotic_Oscillator.m' script.
% Defines a function used in the ode45 call in the master script to solve
% the problem of the simple harmonic and nonlinear driven oscillators.
global Q g l Omega_D F_D
% Add actual function
omega = theta(2);
d2thetadt2 = -g/l*sin(theta(1)) -Q*omega + F_D*sin(Omega_D*t);
Oscillator_out = [omega, d2thetadt2]';
end