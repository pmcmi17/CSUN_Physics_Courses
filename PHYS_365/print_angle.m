function print_angle(ang_in_deg)
% Takes an angle in radians an prints it to the command line. Function for
% angle_conversion.m.
fprintf('Here is your angle in radians: %f\n',convert_angle(ang_in_deg))
end
function [angle_in_rad] = convert_angle(angle_in_deg)
% Takes angle in degrees and convets it to radians. Function for
% angle_conversion.m.
angle_in_rad = angle_in_deg*(pi/180);
end