from plotly import ContourPlot3D
a = 3; b = 2; c = 1;
ContourPlot3D[x^2/a^2 + y^2/b^2 + z^2/c^2 == 1, {x, -3, 3}, {y, -3, 3}, {z, -3, 3}]

