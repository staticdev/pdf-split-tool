"""Test cases for the __main__ module."""
from unittest.mock import Mock
from unittest.mock import patch

import click.testing
import pytest

from pdf_split_tool import __main__


@pytest.fixture
def runner() -> click.testing.CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


@patch("pdf_split_tool.file_handler.get_filenames")
def test_main_succeeds(
    mock_file_handler_get_filenames: Mock, runner: click.testing.CliRunner
) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
