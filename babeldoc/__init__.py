"""BabelDOC - A document translation and processing library.

Fork of funstory-ai/BabelDOC, providing tools for translating
and processing PDF and other document formats.

Personal fork: customized for local experimentation and learning.
Upstream: https://github.com/funstory-ai/BabelDOC

Note: Using 'unknown' as fallback version instead of a fake semver
string, to make it clearer when the package isn't properly installed.

Fork notes:
- Tracking upstream at funstory-ai/BabelDOC
- Local changes are minimal and experimental; not intended for production use
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("babeldoc")
except PackageNotFoundError:
    # Use 'unknown' to clearly indicate the package is not installed,
    # rather than implying a specific (fake) version number.
    __version__ = "unknown"

__author__ = "BabelDOC Contributors"
__license__ = "AGPL-3.0"

__all__ = ["__version__", "__author__", "__license__"]
