fig = openfig('H80C1_Best_Fit_for_Report.fig');
xlabel('B (Gauss)')
ylabel('Intensity (A.U.)')
title({'Intensity (A.U.) vs Magnetic Field Strength (Gauss)';'of the Unknown Substance at 353.15 K'})
legend('Fitted-Experimental','Fitted','Experimental')

ax = gca;
outerpos = ax.OuterPosition;
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];

fig.PaperPositionMode = 'auto';
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];

print(fig,'Titled_Best_Fit_80C','-dpdf')