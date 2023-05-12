import open3d as o3d
# import numpy as np

"""
lines = []
with open('s0.obj') as f:
    lines = f.readlines()

mtl = []
with open('s0.mtl') as f:
    mtl = f.read().split("newmtl ")

colour_dict = {}
for entry in mtl:
    split_lines = entry.split("\n")
    if len(split_lines) > 1:
        col_id = split_lines[0].strip()
        colour_val = split_lines[1][4:].strip()
        colour_dict[col_id] = colour_val

vertices = []
n_vert = 0
for i, line in enumerate(lines):
    if line[0:2] == 'v ':
        trimmed_line = line[1:].strip()
        vertices.append(trimmed_line)


# colour_dict = {"Colour_2":"0 255 0"}
# vertex_dict  = {"Colour_2": [1,2,3]}

# map vertices to mtl colours
vertex_dict = {}
edges = []
for i, line in enumerate(lines):

    if line[0:6] == "usemtl":
        colour = colour_dict[line[7:].strip()]
        colour = [str(int(float(c)*255)) for c in colour.split(" ")]
        colour = " ".join(colour)

    if line[0] == "f":
        trimmed_line = line[1:].strip().split(" ")

        extracted_edges = []
        for combo in trimmed_line:
            extracted_edges.append(combo.split("//")[0])

        extracted_edges = np.array(extracted_edges)

        if len(extracted_edges) == 4:  # the petiole vertices are in groups of 4 - so split into 3 and 3
            
            extracted1 = extracted_edges[[0,1,2]]
            extracted2 = extracted_edges[[2,3,0]]        

            edges.append(str(len(extracted1)) + " " +
                         " ".join(extracted1) + "\n")
            edges.append(str(len(extracted2)) + " " +
                         " ".join(extracted2) + "\n")

            for e in extracted1:
                vertex_dict[e] = colour

            for e in extracted2:
                vertex_dict[e] = colour
            
        else:
            edges.append(str(len(extracted_edges)) + " " +
                            " ".join(extracted_edges) + "\n")

            # map to colour
            for e in extracted_edges:
                vertex_dict[e] = colour
                # vertex_dict[e] = "254.22222 255 0" # something funny here *** start here


colours = list(vertex_dict.values())

# keys = list(vertex_dict.keys())

# all_vertices = vertices.copy()


# for v in all_vertices:
#     if v in keys:
#         vertices.append(v)

with open('converted.ply', 'w') as f:
    header = f"ply\nformat ascii 1.0\nelement vertex {len(vertices)}\nproperty float x\nproperty float y\nproperty float z\nproperty uchar diffuse_red\nproperty uchar diffuse_green\nproperty uchar diffuse_blue\nelement face {len(edges)}\nproperty list uchar int vertex_indices\nend_header\n"
    
    f.write(header)

    for i, line in enumerate(vertices):
        f.write(line + " " + colours[i] + "\n") # colours[i]
    for line in edges:
        f.write(line)


"""

import pymeshlab

ms = pymeshlab.MeshSet()
ms.load_new_mesh('s0.obj')

pymeshlab.MeshSet.apply_filter(ms,"meshing_surface_subdivision_midpoint")
pymeshlab.MeshSet.apply_filter(ms,"compute_color_transfer_face_to_vertex")
pymeshlab.MeshSet.apply_filter(ms,"meshing_poly_to_tri")

ms.save_current_mesh('test.ply',binary=False)

# meshing_surface_subdivision_midpoint
# compute_color_transfer_face_to_vertex
# meshing_poly_to_tri (pure triangle mesh)

mesh = o3d.io.read_triangle_mesh(f"test.ply")
o3d.visualization.draw_geometries(
    [mesh], mesh_show_wireframe=True)

# import bpy
# bpy.ops.mesh.quads_convert_to_tris(quad_method='FIXED', ngon_method='BEAUTY')
