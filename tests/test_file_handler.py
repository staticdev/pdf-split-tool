"""Test cases for the file_handler module."""
import os
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

from pdf_split_tool import file_handler


@pytest.fixture
def cwd(fs: MockFixture, monkeypatch: Mock) -> None:
    """Fixture for pyfakefs fs."""
    fs.cwd = "/path"
    monkeypatch.setenv("HOME", "/home")


def test_get_filename_not_found(fs: MockFixture, cwd: Mock) -> None:
    """It raises `SystemExit` when file is not found."""
    with pytest.raises(SystemExit):
        assert file_handler.get_filenames("*.pdf")


def test_get_filename_current_folder(fs: MockFixture, cwd: Mock) -> None:
    """It returns filename found in current folder."""
    fs.create_file("/path/report.pdf")
    assert (
        file_handler.get_filenames("*.pdf") == ["report.pdf"]
    )
