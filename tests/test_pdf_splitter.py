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

        splitter = pdf_splitter.PdfSplitter("small_res.pdf")
        assert splitter.validate_resolution() is True

    def test_validate_resolution_invalid(
        self, mock_os_path_getsize: Mock, mock_pypdf4_pdffilereader: Mock
    ) -> None:
        """It returns invalid resolution."""
        # 10mb pdf with 10 pages
        mock_os_path_getsize.return_value = 10000000
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 10

        splitter = pdf_splitter.PdfSplitter("big_res.pdf")
        assert splitter.validate_resolution() is False

    def test_split_max_size_equal_max(
        self, mock_os_path_getsize: Mock, mock_pypdf4_pdffilereader: Mock
    ) -> None:
        """It does nothing."""
        # 1mb pdf with 1mb max_size
        mock_os_path_getsize.return_value = 1000000
        max_size = 1000000
        splitter = pdf_splitter.PdfSplitter("small.pdf")

        assert splitter.split_max_size(max_size) == 0

    @patch("PyPDF4.PdfFileWriter")
    @patch("tempfile.TemporaryFile")
    def test_split_max_size_greater_than_max(
        self,
        mock_temporaryfile: Mock,
        mock_pypdf4_pdffilewriter: Mock,
        mock_os_path_getsize: Mock,
        mock_pypdf4_pdffilereader: Mock,
    ) -> None:
        """It splits."""
        # 2mb pdf with 1mb max_size
        mock_os_path_getsize.return_value = 2000000
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 2
        max_size = 1000000
        mock_temporaryfile.return_value.__enter__.return_value.tell.return_value = (
            1000000
        )
        splitter = pdf_splitter.PdfSplitter("big.pdf")

        assert splitter.split_max_size(max_size) == 2

    @patch("PyPDF4.PdfFileWriter")
    @patch("tempfile.TemporaryFile")
    def test_split_max_size_uneven_distribution_of_pages(
        self,
        mock_temporaryfile: Mock,
        mock_pypdf4_pdffilewriter: Mock,
        mock_os_path_getsize: Mock,
        mock_pypdf4_pdffilereader: Mock,
    ) -> None:
        """It splits in 2 pages and 1 page."""
        # 3mb pdf with 2mb max_size
        mock_os_path_getsize.return_value = 3000000
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 3
        max_size = 2000000
        mock_temporaryfile.return_value.__enter__.return_value.tell.return_value = (
            2000000
        )
        splitter = pdf_splitter.PdfSplitter("uneven.pdf")

        assert splitter.split_max_size(max_size) == 2
