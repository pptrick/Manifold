import os
from pathlib import Path
import argparse

# build the project with `bash install.sh` first
from manifold import w_mesh2manifold

import numpy as np

def normalize_vertices(points:np.ndarray):
    assert points.shape[1] == 3
    span_min = np.min(points, axis=0)
    span_max = np.max(points, axis=0)
    center = (span_min + span_max) / 2.0
    span = np.max((span_max - span_min) / 2.0)
    points = (points - center) / span
    return points

def mesh2manifold(input_path:str|Path, output_path:str|Path, normalize=False, remesh_threshold=-1):
    """Load mesh from local storage (glb, obj, ...), turn to a manifold mesh and store to local storage 

    Args:
        input_path (str | Path): path to input mesh
        output_path (str | Path): path to save manifold mesh
        normalize (bool, optional): If True, normalize mesh vertices to [-1, 1]. Defaults to False.
        remesh_threshold (int): Vertex threshold starting for remeshing, -1 for no remeshing. Defaults to -1.

    Returns:
        int: status, 0 means success
    """
    if str(input_path).endswith(".obj"):
        import trimesh
        mesh = trimesh.load_mesh(input_path, force="mesh")
        vertices = np.array(mesh.vertices, dtype=np.float32)
        indices = np.array(mesh.faces, dtype=np.int32)
    else:
        from libmeshy import LoadedMesh, load_mesh
        mesh: LoadedMesh = load_mesh(str(input_path), remesh_threshold=remesh_threshold)
        vertices = np.array(mesh.vertices, dtype=np.float32)
        indices = np.array(mesh.indices, dtype=np.int32)
    if normalize:
        vertices = normalize_vertices(vertices)
    status = w_mesh2manifold(
        vertices.flatten(), indices.flatten(),
        str(output_path).encode('utf-8'), 200000, True
    )
    return status

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help='Path to the input mesh')
    parser.add_argument("-o", "--output", type=str, default='output.obj', help='Path to the output mesh (should be obj)')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    mesh2manifold(
        input_path=args.input,
        output_path=args.output,
        normalize=True
    )
    
if __name__ == "__main__":
    main()
    import trimesh
    mesh = trimesh.load_mesh("output.obj", force="mesh")
    vertices = mesh.vertices
    print(np.max(vertices))
    