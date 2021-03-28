import pyransac3d as pyrsc
import open3d as o3d

pcd = o3d.io.read_point_cloud("test_mesh.ply.ply")
print(pcd)

points = load_points(.) # Load your point cloud as a numpy array (N, 3)

plane1 = pyrsc.Plane()
best_eq, best_inliers = plane1.fit(points, 0.01)