"""Test cases for the __main__ module."""
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from pdf_split_tool import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@patch("pdf_split_tool.file_handler.get_filenames")
def test_main_succeeds(mock_file_handler_get_filenames, runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
