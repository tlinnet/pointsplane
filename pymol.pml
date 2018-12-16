reinitialize

import pointsplane
#import plane

load Heteroaromatics/Pyridine.xyz
select pyr, Pyridine and not name H

pointsplane.test("pyr")

# Start the wizard, and do manual picking
#cmd.set_wizard(plane.PlaneWizard())

#plane.make_plane_points(name='plane-00', l1=[-0.67, 1.18, 0.0], l2=[-1.39, -0.01, 0.0], l3=[-0.69, -1.22, 0.0])
#plane.make_plane_points(name='plane-01', l1=[-0.67, 1.18, 0.0], l2=[-1.39, -0.01, 0.0], l3=[-0.69, -1.22, 0.0], center=False)
#plane.make_plane_points(name='plane-02', l2=[-0.67, 1.18, 0.0], l3=[-1.39, -0.01, 0.0], l1=[-0.69, -1.22, 0.0], center=False)
#plane.make_plane_points(name='plane-03', l3=[-0.67, 1.18, 0.0], l1=[-1.39, -0.01, 0.0], l2=[-0.69, -1.22, 0.0], center=False)


#dict = {'ALPHA':0.6, 'COLOR':[0.55, 0.25, 0.60], 'INVERT':True}
#plane.make_plane_points(name='plane-02', l1=[-0.67, 1.18, 0.0], l2=[-1.39, -0.01, 0.0], l3=[-0.69, -1.22, 0.0], center=False, settings=dict)

