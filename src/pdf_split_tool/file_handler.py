"""File handler module."""
import glob
import os
import sys
from typing import List


def get_filenames(filepath: str, pattern: str) -> List[str]:
    """Returns all filenames that matches the pattern in current folder.

    Args:
        filepath (str): folder path.
        pattern (str): filename pattern.

    Returns:
        List[str]: list of paths.
    """
    filenames = glob.glob(os.path.join(filepath, pattern))
    if filenames:
        return filenames
    return sys.exit("Error: no file found, check the documentation for more info.")
