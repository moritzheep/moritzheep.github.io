import open3d as o3d
import numpy as np
import glob

def rescale_mesh_to_unit_cube(mesh):
    """
    Rescales an Open3D triangle mesh to fit within the [-1,1]^3 cube.
    
    Parameters:
    -----------
    mesh : open3d.geometry.TriangleMesh
        The input triangle mesh to be rescaled
    
    Returns:
    --------
    open3d.geometry.TriangleMesh
        A new mesh with rescaled vertices
    """
    # Create a copy of the input mesh to avoid modifying the original
    result_mesh = o3d.geometry.TriangleMesh(mesh)
    
    # Get vertex positions as numpy array
    vertices = np.asarray(result_mesh.vertices)
    
    if len(vertices) == 0:
        return result_mesh
    
    # Compute the bounding box
    min_bound = np.min(vertices, axis=0)
    max_bound = np.max(vertices, axis=0)
    
    # Compute the center of the bounding box
    center = (min_bound + max_bound) / 2
    
    # Center the mesh at the origin
    vertices = vertices - center
    
    # Compute the maximum extent along any dimension
    max_extent = np.max(max_bound - min_bound)
    
    if max_extent > 0:
        # Scale the mesh to fit within [-1,1]^3
        # We divide by half the max_extent to get a range of 2 (-1 to 1)
        scale_factor = 2.0 / max_extent
        vertices = vertices * scale_factor
    
    # Update the mesh vertices
    result_mesh.vertices = o3d.utility.Vector3dVector(vertices)
    
    # Update normals to account for the scaling
    result_mesh.compute_vertex_normals()
    
    return result_mesh

def split_triangles(mesh):
	# Create a copy of the input mesh to avoid modifying the original
	result_mesh = o3d.geometry.TriangleMesh(mesh)
    
	# Get vertex positions as numpy array
	vertices = np.asarray(result_mesh.vertices)
	triangles = np.asarray(result_mesh.triangles)
	
	split_vertices = vertices[triangles].reshape([-1, 3])
	split_triangles = np.arange(0, split_vertices.shape[0], dtype=np.int32)
	
	result_mesh.vertices = o3d.utility.Vector3dVector(split_vertices)
	result_mesh.triangles = o3d.utility.Vector3iVector(split_triangles.reshape([-1, 3]))
	
	return result_mesh

meshes = glob.glob("*.obj")

for mesh in meshes:
	print(mesh)
	tmp = o3d.io.read_triangle_mesh(mesh)
	#R = tmp.get_rotation_matrix_from_axis_angle(np.array([0, 180, 0], dtype=float))
	#tmp = tmp.rotate(R, center=(0, 0, 0))
	tmp = rescale_mesh_to_unit_cube(tmp)
	
	# Get vertex positions as numpy array
	vertices = np.asarray(tmp.vertices)
	vertices[:,1:] *= -1
	tmp.vertices = o3d.utility.Vector3dVector(vertices)
	
	triangles = np.asarray(tmp.triangles)
	triangles = triangles[:,::-1]
	tmp.triangles = o3d.utility.Vector3iVector(triangles)
	
	tmp = split_triangles(tmp)
	tmp = tmp.paint_uniform_color([227 / 255, 224 / 255, 205 / 255])
	
	o3d.io.write_triangle_mesh(mesh.replace(".obj", ".glb"), tmp)
	o3d.io.write_triangle_mesh(mesh.replace(".obj", ".ply"), tmp)
