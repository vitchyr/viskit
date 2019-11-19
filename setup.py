"""Setup script for viskit."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Flask==1.1.1', 'matplotlib', 'plotly==3.4.2', 'numpy']

setup(name='viskit',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('viskit')],
    description="rllab's viskit with some added features")
