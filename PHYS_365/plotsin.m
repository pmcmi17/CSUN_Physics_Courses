function plotsin(low,high)
% Takes a small value and a high value and plots the sin function twice.
% (Ones for the high value and once for the low value). Shows both graphs.
vec1 = linspace(0,2*pi,low);
sin_val1 = zeros(0,low);
for i = 1:low
    sin_val1(i) = sin(vec1(i));
end
vec2 = linspace(0,2*pi,high);
sin_val2 =zeros(0,high);
for i = 1:high
    sin_val2(i) = sin(vec2(i));
end
plot(vec1,sin_val1)
title('Low value vs high value')
xlabel('x')
ylabel('y')
hold on
plot(vec2,sin_val2)
hold off
end

