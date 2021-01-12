import pyransac3d as pyrsc
import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("test_mesh.ply")
#print(pcd)

pcd = np.asarray(pcd.points)
#print(pcd.shape)

plane1 = pyrsc.Plane()
best_eq, best_inliers = plane1.fit(pcd, 0.01)

#print(best_eq)
#print(best_inliers)

candidate = best_inliers.tolist()

arr = []

for i in range(len(pcd)):
    if i in candidate:
        
        arr.append(pcd[i].tolist())

arr = np.array(arr)

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(arr)

o3d.visualization.draw_geometries([point_cloud])