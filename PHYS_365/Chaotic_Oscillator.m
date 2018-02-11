% This is the master script for the chaotic oscillator project. This script
% is designed to run all parts of the project, creating one figure with all
% plots clearly labeled, and making all desired comparisons. The companion 
% function is: 'Oscillator_ODE.m'. Overall, we expect to have three 
% figures as output. We will have one subplot figure for the simple 
% harmonic oscillator, one plot consisting of numerical results, the other 
% of analytical results. We will also have one figure consisting of three 
% plots, each demonstrating nonlinear oscillations with different driving 
% forces. Additionally, we will have another subplot figure with two plots,
% each comparing two nearly identical pendulums, having slightly differing 
% initial conditions. First, we solve the simple harmonic oscillator over 
% 60 seconds, plotting angular position versus time. We compare these 
% numerical results to analytical results. Next, we solve the nonlinear 
% driven oscillator for three values of an external driving force, plotting
% our results (angular position versus time) on the same graph over 50 
% seconds. Then we compare two identical pendulums, with slightly different
% initial conditions, plotting the difference in angular position versus 
% time on a semilog axis, and also plotting the same attributes of another 
% pair of pendulums for 150 seconds rather than 60 seconds with a different
% driving force.

% Here we define parameters which will be used throughout the script,
% making them global variables as to use in the companion function. 

global Q g l Omega_D F_D
theta_0_opt = [0.2,0.201];
time_interval = [0 60];
Omega_D = 2/3;
omega_0 = 0;
g = 9.8; 
l = 9.8; 
Q = 0.5;

for run = 1:4 % Loops through to do all problems
    if run == 1
        % Need to ensure we consider only the simple harmonic case
        Q = 0; % Second term = 0
        F_D = 0; % Third term = 0
        theta_0 = theta_0_opt(1); % Correct initial condition
        figure(1)
        for i = 1:2
            if i == 1
                subplot(2,1,1)
                theta_initial = [theta_0, omega_0]';
                [T,theta_out] = ode45(@Oscillator_ODE, time_interval, theta_initial);
                plot(T,theta_out(:,1))
                title('Simple Harmonic Oscillator (Numerical)')
            elseif i == 2
                subplot(2,1,2)
                title('Simple Harmonic Oscillator (Analytical)')
                % Actual work (Analytical Solution)
            end
            xlabel('Time (s)')
            ylabel('Angular Position (\theta)')
        end
    elseif run == 2
        F_D_opt = [0,0.5,1.2]; % Allow for the three cases of force
        F_D_colors = ['r','g','b'];
        theta_0 = theta_0_opt(1); % Correct intitial condition
        figure(2)
        for i = 1:3
            F_D = F_D_opt(i); % Select force case
            % Actual work (nonlinear driven, numerical)
            theta_initial = [theta_0, omega_0]';
            [T,theta_out] = ode45(@Oscillator_ODE, time_interval, theta_initial);
            plot(T,theta_out(:,1),F_D_colors(i))
            hold on
        end
        title('Nonlinear Driven Oscillations (Varying Driving Force)')
        xlabel('Time (s)')
        ylabel('Angular Position (\theta)')
        legend('0 N','0.5 N','1.2 N') % Add legend handles
    elseif run == 3 || 4 
        figure(3)
        if run == 3
            F_D = 0.5; % Correct force
            time_interval = linspace(0,50);
            subplot(2,1,1)
        elseif run == 4
            F_D = 1.2; % Correct force
            time_interval = linspace(0,150); % Correct time interval
            subplot(2,1,2)
        end
        for i = 1:2
            theta_0_0 = theta_0_opt(1); % Correct initial condition
            theta_initial = [theta_0_0, omega_0]';
            [~,theta_out_1] = ode45(@Oscillator_ODE, time_interval, theta_initial);
            theta_1 = theta_out_1(:,1);
            theta_0_1 = theta_0_opt(2); % Correct initial condition
            theta_initial = [theta_0_1, omega_0]';
            [T,theta_out_2] = ode45(@Oscillator_ODE, time_interval, theta_initial);
            theta_2 = theta_out_2(:,1);
            delta_theta = abs(theta_1 - theta_2);
            semilogy(T,delta_theta)
            xlabel('Time (s)')
            ylabel('\Delta\theta')
        end
        if run == 3
            subplot(2,1,1)
            title('\Delta\theta for Driving Force of 0.5 N')
        elseif run == 4
            subplot(2,1,2)
            title('\Delta\theta for Driving Force of 1.2 N')
        end
    end
end