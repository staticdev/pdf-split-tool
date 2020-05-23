"""File handler module."""
import glob
import sys
from typing import List


def get_filenames(pattern: str) -> List[str]:
    """Returns all filenames that matches the pattern in current folder.

    Args:
        pattern (str): filename pattern.

    Returns:
        List[str]: list of paths.
    """
    filenames = glob.glob(pattern)
    if filenames:
        return filenames
    return sys.exit("Error: no file found, check the documentation for more info.")
