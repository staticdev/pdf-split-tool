"""Test cases for the pdf splitter module."""
# import unittest
# from unittest.mock import Mock
# from unittest.mock import patch
# from pdf_split_tool import pdf_splitter
# @patch("PyPDF4.PdfFileReader")
# @patch("os.path.getsize", return_value=10000)
# class PdfSplitterTests(unittest.TestCase):
#     def test_validate_resolution_valid(
#         self, mock_os_path_getsize: Mock, mock_PyPDF4_PdfFileReader: Mock
#     ) -> None:
#         splitter = pdf_splitter.PdfSplitter("small.pdf")
#         assert splitter.validate_resolution() == True
# def test_validate_resolution_invalid(self) -> None:
#     splitter = pdf_splitter.PdfSplitter("big.pdf")
#     assert splitter.validate_resolution() == False
