"""Test cases for the __main__ module."""
from typing import Any
from unittest.mock import Mock
from unittest.mock import patch

import click.testing
import pytest
from pytest_mock import MockFixture

from pdf_split_tool import __main__


@pytest.fixture
def runner() -> click.testing.CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_file_handler_get_filenames(mocker: MockFixture) -> Any:
    """Fixture for mocking pdf_split_tool.file_handler.get_filenames."""
    return mocker.patch(
        "pdf_split_tool.file_handler.get_filenames", return_value=["filename"]
    )


@pytest.fixture
def mock_pdf_splitter_pdfsplitter(mocker: MockFixture) -> Any:
    """Fixture for mocking pdf_splitter.PdfSplitter."""
    return mocker.patch("pdf_split_tool.pdf_splitter.PdfSplitter", autospec=True)


def test_main_valid_resolution(
    runner: click.testing.CliRunner,
    mock_file_handler_get_filenames: Any,
    mock_pdf_splitter_pdfsplitter: Any,
) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_main_invalid_resolution_skipped(
    runner: click.testing.CliRunner,
    mock_file_handler_get_filenames: Any,
    mock_pdf_splitter_pdfsplitter: Any,
) -> None:
    """It exits with a status code of zero."""
    mock_pdf_splitter_pdfsplitter.return_value.validate_resolution.return_value = False
    result = runner.invoke(__main__.main)
    assert result.output == (
        "Warning: filename has more than 200kb per page. "
        "Consider reducing resolution before splitting.\n"
        "Do you want to continue? [y/N]: \n"
        "filename skipped.\n"
    )
    assert result.exit_code == 0


@patch("click.confirm", return_value=True)
def test_main_invalid_resolution_confirm(
    mock_click_confirm: Mock,
    runner: click.testing.CliRunner,
    mock_file_handler_get_filenames: Any,
    mock_pdf_splitter_pdfsplitter: Any,
) -> None:
    """It exits with a status code of zero."""
    mock_pdf_splitter_pdfsplitter.return_value.validate_resolution.return_value = False
    result = runner.invoke(__main__.main)
    assert result.output == (
        "Warning: filename has more than 200kb per page. "
        "Consider reducing resolution before splitting.\n"
    )
    assert result.exit_code == 0


def test_main_uses_specified_filepath(
    runner: click.testing.CliRunner, mock_pdf_splitter_pdfsplitter: Any,
) -> None:
    """It uses the specified filepath."""
    with runner.isolated_filesystem():
        with open("test.pdf", "w"):
            result = runner.invoke(__main__.main, ["test.pdf"])
    assert result.exit_code == 0
