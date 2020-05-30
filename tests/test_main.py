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


@patch("pdf_split_tool.file_handler.get_filenames", return_value=["filename"])
@patch("pdf_split_tool.pdf_splitter.PdfSplitter", autospec=True)
def test_main_valid_resolution(
    mock_pdf_splitter_pdfsplitter: Mock,
    mock_file_handler_get_filenames: Mock,
    runner: click.testing.CliRunner,
) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


@patch("pdf_split_tool.file_handler.get_filenames", return_value=["filename"])
@patch("pdf_split_tool.pdf_splitter.PdfSplitter", autospec=True)
def test_main_invalid_resolution_skipped(
    mock_pdf_splitter_pdfsplitter: Mock,
    mock_file_handler_get_filenames: Mock,
    runner: click.testing.CliRunner,
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


@patch("pdf_split_tool.file_handler.get_filenames", return_value=["filename"])
@patch("pdf_split_tool.pdf_splitter.PdfSplitter", autospec=True)
@patch("click.confirm", return_value=True)
def test_main_invalid_resolution_confirm(
    mock_click_confirm: Mock,
    mock_pdf_splitter_pdfsplitter: Mock,
    mock_file_handler_get_filenames: Mock,
    runner: click.testing.CliRunner,
) -> None:
    """It exits with a status code of zero."""
    mock_pdf_splitter_pdfsplitter.return_value.validate_resolution.return_value = False
    result = runner.invoke(__main__.main)
    assert result.output == (
        "Warning: filename has more than 200kb per page. "
        "Consider reducing resolution before splitting.\n"
    )
    assert result.exit_code == 0


# @patch("pdf_split_tool.pdf_splitter.PdfSplitter", autospec=True)
# def test_main_uses_specified_filepath(
#     mock_pdf_splitter_pdfsplitter: Mock, runner: click.testing.CliRunner,
# ) -> None:
#     """It uses the specified filepath."""
#     result = runner.invoke(__main__.main, ["test.pdf"])
#     assert result.exit_code == 0
