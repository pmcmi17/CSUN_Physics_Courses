function [vol,varargout] = Vol_area(radius)
% Calulates the volume of a sphere given radius. If the user specifies two
% outputs, also calulates the surface area of the sphere.
vol = (4 / 3) * pi * (radius) ^ 3;
SA = 4 * pi * (radius) ^ 2;
varargout{1} = SA;
end

