# read version from installed package
from importlib.metadata import version
__version__ = version("pybrowser")

from .window import Window

__all__ = [
    "Window",
]
