function [vol, sa] = calc_vol_and_sa(radius,height)
% Takes the radius and height of any cylinder and calculates the volume and
% surface area of the cylinder specified. 
vol = pi*radius^2*height;
sa = 2*pi*radius*height;
end

