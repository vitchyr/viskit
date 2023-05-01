"""Setup script for viskit."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Flask==2.3.2', 'matplotlib', 'plotly==5.1.0', 'numpy', 'Jinja2>=3.0']

setup(name='viskit',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    package_data={
        'viskit': ['static/css/*', 'static/js/*', 'templates/main.html'],
    },
    packages=[p for p in find_packages() if p.startswith('viskit')],
    description="rllab's viskit with some added features")
