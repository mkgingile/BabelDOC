"""BabelDOC - A document translation and processing library.

Fork of funstory-ai/BabelDOC, providing tools for translating
and processing PDF and other document formats.

Personal fork: customized for local experimentation and learning.
Upstream: https://github.com/funstory-ai/BabelDOC
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("babeldoc")
except PackageNotFoundError:
    __version__ = "0.0.0.dev0"

__author__ = "BabelDOC Contributors"
__license__ = "AGPL-3.0"

__all__ = ["__version__", "__author__", "__license__"]
