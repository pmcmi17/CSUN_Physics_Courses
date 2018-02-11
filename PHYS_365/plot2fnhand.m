function plot2fnhand(hand1,hand2)
% Recieves two function handles. Plots both functions in seperate windows.
% Finds a random integer in the range of 4 to 10 and uses this number as
% the number of points to plot for each function. The function handles will
% be displayed as the titles of the graphs, respectively.
x = 1:randi([4,10],1);
figure;
fplot(hand1,(x))
title(func2str(hand1))
figure;
fplot(hand2,(x))
title(func2str(hand2))
end

