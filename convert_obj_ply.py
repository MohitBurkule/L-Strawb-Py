import pymeshlab
import glob
import os


# find all objs in /out
files = glob.glob("out/*.obj")

if not os.path.exists("data"):
            os.makedirs("data")

for filename in files:
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(filename)

    pymeshlab.MeshSet.apply_filter(ms,"meshing_surface_subdivision_midpoint")
    pymeshlab.MeshSet.apply_filter(ms,"compute_color_transfer_face_to_vertex")
    pymeshlab.MeshSet.apply_filter(ms,"meshing_poly_to_tri")
    
    ms.save_current_mesh(f'data/{filename[4:-4]}.ply',binary=False)

  
