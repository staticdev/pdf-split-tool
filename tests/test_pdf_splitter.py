"""Test cases for the pdf splitter module."""
from unittest.mock import Mock
from unittest.mock import patch

from pdf_split_tool import pdf_splitter


@patch("PyPDF4.PdfFileReader")
class TestPdfSplitter:
    """PdfSplitter test class."""

    def test_validate_resolution_valid(
        self, mock_pypdf4_pdffilereader: Mock, fs: Mock
    ) -> None:
        """It returns valid resolution."""
        # 1mb pdf with 10 pages
        filename = "small_res.pdf"
        fs.create_file(filename, st_size=1000000)
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 10
        splitter = pdf_splitter.PdfSplitter(filename)

        assert splitter.validate_resolution() is True

    def test_validate_resolution_invalid(
        self, mock_pypdf4_pdffilereader: Mock, fs: Mock
    ) -> None:
        """It returns invalid resolution."""
        # 10mb pdf with 10 pages
        filename = "big_res.pdf"
        fs.create_file(filename, st_size=10000000)
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 10
        splitter = pdf_splitter.PdfSplitter(filename)

        assert splitter.validate_resolution() is False

    def test_split_max_size_equal_max(
        self, mock_pypdf4_pdffilereader: Mock, fs: Mock
    ) -> None:
        """It does nothing."""
        # 1mb pdf with 1mb max_size
        filename = "small.pdf"
        max_size = 1000000
        fs.create_file(filename, st_size=max_size)
        splitter = pdf_splitter.PdfSplitter(filename)

        assert splitter.split_max_size(max_size) == 0

    @patch("PyPDF4.PdfFileWriter")
    def test_split_max_size_greater_than_max(
        self, mock_pypdf4_pdffilewriter: Mock, mock_pypdf4_pdffilereader: Mock, fs: Mock
    ) -> None:
        """It splits."""
        # 2mb pdf with 1mb max_size
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 2
        max_size = 1000000
        fs.create_file("big.pdf", st_size=2000000)
        splitter = pdf_splitter.PdfSplitter("big.pdf")

        assert splitter.split_max_size(max_size) == 2

    @patch("PyPDF4.PdfFileWriter")
    def test_split_max_size_uneven_distribution_of_pages(
        self, mock_pypdf4_pdffilewriter: Mock, mock_pypdf4_pdffilereader: Mock, fs: Mock
    ) -> None:
        """It splits in 2 pages and 1 page."""
        # 3mb pdf with 2mb max_size
        filename = "uneven.pdf"
        fs.create_file(filename, st_size=3000000)
        mock_pypdf4_pdffilereader.return_value.getNumPages.return_value = 3
        splitter = pdf_splitter.PdfSplitter(filename)

        assert splitter.split_max_size(2000000) == 2
