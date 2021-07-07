"""Setup script for viskit."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Flask==2.0.1', 'matplotlib==3.4.2', 'plotly==5.1.0', 'numpy==1.21.0', 'Jinja2==2.11.3']

setup(name='viskit',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    package_data={
        'viskit': ['static/css/*', 'static/js/*', 'templates/main.html'],
    },
    packages=[p for p in find_packages() if p.startswith('viskit')],
    description="rllab's viskit with some added features")
