"""Setup for decision tree module."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest']
}


setup(
    name='K-Means Clustering Algorithm',
    description='Rough implementation of the KMeans clustering algorithm.',
    version=0.0,
    author='Kurt Maurer',
    author_email='kurtrm@gmail.com',
    extras_require=extra_packages
)
