reinitialize
bg_color white

import pointsplane

########################################
load Heteroaromatics/Pyridine.xyz
select Pyridine_sel, Pyridine and not name H

dict = {'ALPHA':0.6, 'COLOR':[0.55, 0.25, 0.60], 'INVERT':False}
pointsplane.make_points_plane(name="Pyridine_plane", sele="Pyridine_sel", settings=dict)
########################################

disable Pyridine*

########################################
load Heteroaromatics/Benzofuran.xyz
select Benzofuran_sel, Benzofuran and not name H

dict2 = {'ALPHA':0.6, 'COLOR':[0.0, 0.0, 1.0], 'INVERT':False}
pointsplane.make_points_plane(name="Benzofuran_plane", sele="Benzofuran_sel", settings=dict2)
########################################

disable Benzofuran*

########################################
load Heteroaromatics/1_2-Oxazole.xyz
select 1_2-Oxazole_sel, 1_2-Oxazole and not name H

dict2 = {'ALPHA':0.6, 'COLOR':[1.0, 0.5, 0.0], 'INVERT':False}
pointsplane.make_points_plane(name="1_2-Oxazole_plane", sele="1_2-Oxazole_sel", settings=dict2)
