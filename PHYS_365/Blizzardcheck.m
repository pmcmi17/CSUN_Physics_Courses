% This script loads in storm data and determines whether or not a blizzard
% condition was met on a particular day. 
load stormtrack.dat;
index = 1;
count = 0;
while index <= size(stormtrack,1) && count <4
    if stormtrack(index,2) >= 30 && stormtrack(index,3) <= 0.5
        count = count + 1;
        if count == 4
            fprintf('A blizzard occured today.\n');
        end
    else
        count = 0;
    end
    index = index +1;
    if index == size(stormtrack,1) && count < 4
        fprintf('No blizzard today!\n')
    end
end