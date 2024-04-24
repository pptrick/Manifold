# cython: c_string_type=unicode, c_string_encoding=utf8

from libcpp cimport bool
from libcpp.vector cimport vector

cdef extern from "Model_OBJ.h":
    int mesh2manifold(const vector[float]& verts, const vector[int]& faces, char* filename, int resolution, bool sharp)

def w_mesh2manifold(vector[float]& verts, vector[int]& faces, char* filename, int resolution=20000, bool sharp=False):
    return mesh2manifold(verts, faces, filename, resolution, sharp)