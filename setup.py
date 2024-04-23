from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [Extension(
    'manifold',
    sources=[
        'src/wrapper.pyx', 
        'src/Model_OBJ.cpp',
        'src/BVH.cpp',
        'src/Intersection.cpp'
    ],
    language='c++',
    extra_compile_args=["-std=c++11"],
    include_dirs=['3rd']
)]

setup(
    name="manifold",
    version="0.1",
    description="Process mesh into manifold",
    ext_modules=cythonize(extensions),
    setup_requires=[
        'Cython',
    ],
)