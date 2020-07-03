"""PDF operations module."""
import os
import sys
import tempfile

import PyPDF4


class PdfSplitter:
    """Pdf Splitter class."""

    def __init__(self, filepath: str) -> None:
        """Constructor."""
        self.filepath = filepath
        self.input_pdf = PyPDF4.PdfFileReader(filepath, "rb")
        self.total_pages = self.input_pdf.getNumPages()
        self.size = os.path.getsize(filepath)
        self.avg_size = self.size / self.total_pages
        print(
            "File: {}\nFile size: {}\nTotal pages: {}\nAverage size: {}".format(
                filepath, self.size, self.total_pages, self.avg_size
            )
        )

    def validate_resolution(self) -> bool:
        """Checks if resolution is too high."""
        if self.avg_size > 1024 * 200:
            return False
        return True

    def _get_pdf_size(self, pdf_writer: PyPDF4.PdfFileWriter) -> int:
        """Generates temporary PDF.

        Args:
            pdf_writer: pdf writer.

        Returns:
            int: generated file size.
        """
        with tempfile.TemporaryFile(mode="wb") as fp:
            pdf_writer.write(fp)
            return fp.tell()

    def split_max_size(self, max_size: int) -> int:
        """Creates new files based on max size.

        Args:
            max_size: size in integer megabytes.

        Returns:
            int: number of PDFs created.
        """
        if self.size > max_size:
            avg_step = int(max_size / self.avg_size)

            pdfs_count = 0
            current_page = 0

            while current_page != self.total_pages:
                end_page = current_page + avg_step
                if end_page > self.total_pages:
                    end_page = self.total_pages

                current_size = sys.maxsize

                # while PDF is too big create smaller PDFs
                while current_size > max_size:
                    pdf_writer = PyPDF4.PdfFileWriter()
                    for page in range(current_page, end_page):
                        pdf_writer.addPage(self.input_pdf.getPage(page))
                    current_size = self._get_pdf_size(pdf_writer)
                    self.input_pdf = PyPDF4.PdfFileReader(self.filepath, "rb")
                    end_page -= 1

                # write PDF with size max_size
                with open(
                    self.filepath.replace(".pdf", "-{}.pdf".format(pdfs_count)), "wb"
                ) as out:
                    pdf_writer.write(out)

                current_page = end_page + 1
                pdfs_count += 1
            return pdfs_count
        return 0
