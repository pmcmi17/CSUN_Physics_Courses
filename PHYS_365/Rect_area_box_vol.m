function [area,varargout] = Rect_area_box_vol(len,widt,varargin)
% Takes length and width of a rectangle. Calculates the area. If user also
% supplies a height for a box, calculates the volume of the box with the
% rectangle base. 
area = len * widt;
if nargin > 2
    vol = len * widt * varargin{1};
    varargout{1} = vol;
end
end
