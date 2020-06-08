"""Test cases for the pdf splitter module."""
import unittest
from unittest.mock import Mock
from unittest.mock import patch

from pdf_split_tool import pdf_splitter


@patch("PyPDF4.PdfFileReader")
@patch("os.path.getsize")
class PdfSplitterTests(unittest.TestCase):
    """PdfSplitter test class."""

    def test_validate_resolution_valid(
        self, mock_os_path_getsize: Mock, mock_pypdf4_pdffilereader: Mock
    ) -> None:
        """It returns valid resolution."""
        # 1mb pdf with 10 pages
        mock_os_path_getsize.return_value = 1000000
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 10

        splitter = pdf_splitter.PdfSplitter("small.pdf")
        assert splitter.validate_resolution() is True

    def test_validate_resolution_invalid(
        self, mock_os_path_getsize: Mock, mock_pypdf4_pdffilereader: Mock
    ) -> None:
        """It returns invalid resolution."""
        # 10mb pdf with 10 pages
        mock_os_path_getsize.return_value = 10000000
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 10

        splitter = pdf_splitter.PdfSplitter("big.pdf")
        assert splitter.validate_resolution() is False
