reinitialize
bg_color white

import pointsplane
import plane

load Heteroaromatics/Pyridine.xyz
select pyr, Pyridine and not name H

dict = {'ALPHA':0.6, 'COLOR':[0.55, 0.25, 0.60], 'INVERT':False}
pointsplane.make_points_plane(name="pyr plane", sele="pyr", settings=dict)

load Heteroaromatics/Benzofuran.xyz
select benz, Benzofuran and not name H

dict2 = {'ALPHA':0.6, 'COLOR':[0.0, 0.0, 1.0], 'INVERT':False}
pointsplane.make_points_plane(name="benz plane", sele="benz", settings=dict2)