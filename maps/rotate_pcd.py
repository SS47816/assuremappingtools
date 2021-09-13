import open3d as o3d
import numpy as np
import copy 

folder_path = "/home/arc/ss_ws/assuremappingtools/maps/"
input_file_name = "utown/01.pcd"
output_file_name = "utown/01_rotated.pcd"

print("Load a point cloud, print it, and render it")
pcd_raw = o3d.io.read_point_cloud(folder_path + input_file_name)
pcd_out = copy.deepcopy(pcd_raw)

# Rotate the first time (90 deg wrt X)
# axis_angle = np.arange(3).reshape(3, 1)
# axis_angle = np.array([[np.pi/2], [0], [0]], dtype = np.float64)
R1 = o3d.geometry.get_rotation_matrix_from_xyz((np.pi/2, np.pi, 0))
pcd_out = pcd_out.rotate(R1, center=(0, 0, 0))

# Rotate the second time (180 deg wrt Y)
# axis_angle = np.array([[0], [np.pi], [0]], dtype = np.float64)
# R2 = o3d.geometry.get_rotation_matrix_from_xyz((0, np.pi, 0))
# pcd_out = pcd_out.rotate(R2, center=(0, 0, 0))

# Translation (7.5 m wrt Y)
pcd_out = pcd_out.translate((0, 0, 1.55))

o3d.io.write_point_cloud(folder_path + output_file_name, pcd_out)

# Visualization 
coords = o3d.geometry.TriangleMesh.create_coordinate_frame() 
pcd_raw.paint_uniform_color([0.7, 0.7, 0.7])
pcd_out.paint_uniform_color([0.8, 0.2, 0.5])
o3d.visualization.draw_geometries([coords, pcd_raw, pcd_out])