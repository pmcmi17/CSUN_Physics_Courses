% Requests two values for the time constant of the exponetial decay
% function, along with the beginning and ending values of a vector 't'
% (this vector will serve as the bounds for the time axis). Then, a plot
% will be generated with two graphs (one for each time constant given),
% within the range of time specified by the user. 

tau1 = input('Enter value for the time constant: \n');
tau2 = input('Enter a different value for the time constant: \n');
t1 = input('Enter a start time: \n');
t2 = input('Enter an end time: \n');
x = linspace(t1,t2,100);

y1 = exponential(x,tau1);
y2 = exponential(x,tau2);

plot(x,y1,'r')
hold on
plot(x,y2,'b')
ylabel('Exponential Value')
xlabel('Time')
legend('y1','y2')
title('Two exponential graphs with different tau values')
