from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

setup(
    name='add_matrix_cuda',
    version='1.0',
    author='kenny',
    author_email='kenny@iluvatar.com',
    description='cpp cuda example',
    long_description='cpp cuda example',
    ext_modules=[
        CUDAExtension(
            name='add_matrix_cuda',
            sources=['add_matrix.cpp', 'add_matrix_kernel.cu'])
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
