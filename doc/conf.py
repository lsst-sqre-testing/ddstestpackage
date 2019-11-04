"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.ddstestpackage


_g = globals()
_g.update(build_package_configs(
    project_name='ddstestpackage',
    version=lsst.ddstestpackage.version.__version__))
