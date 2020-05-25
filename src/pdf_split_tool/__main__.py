"""Command-line interface."""
import os
import sys
import tempfile

import click
import PyPDF4

import pdf_split_tool.file_handler


def get_pdf_size(pdf_writer: PyPDF4.PdfFileWriter) -> int:
    """Generates temporary PDF.

    Args:
        pdf_writer: pdf writer.

    Returns:
        int: generated file size.
    """
    with tempfile.TemporaryFile(mode="wb") as fp:
        pdf_writer.write(fp)
        return fp.tell()


@click.command()
@click.version_option()
def main() -> None:
    """Pdf Split Tool."""
    max_size = 20 * 1024 * 1024  # 20 MB
    filepaths = pdf_split_tool.file_handler.get_filenames("*.pdf")
    for filepath in filepaths:
        size = os.path.getsize(filepath)
        print("File: {}\nFile size: {}".format(filepath, size))
        if size > max_size:
            input_pdf = PyPDF4.PdfFileReader(filepath, "rb")
            total_pages = input_pdf.getNumPages()
            avg_size = size / total_pages
            avg_step = int(max_size / avg_size)
            print("Total pages: {}\nAverage size: {}".format(total_pages, avg_size))

            # warn high resolution
            if avg_size > 1024 * 200:
                click.secho(
                    (
                        "Warning: {} has more than 200kb per page. "
                        "Consider reducing resolution before splitting."
                    ).format(filepath),
                    fg="yellow",
                )

            pdfs_count = 0
            current_page = 0
            end_page = current_page + avg_step

            while current_page != total_pages:
                current_size = sys.maxsize

                # while PDF is too big create smaller PDFs
                while current_size > max_size:
                    pdf_writer = PyPDF4.PdfFileWriter()
                    for page in range(current_page, end_page):
                        pdf_writer.addPage(input_pdf.getPage(page))
                    current_size = get_pdf_size(pdf_writer)
                    input_pdf = PyPDF4.PdfFileReader(filepath, "rb")
                    end_page -= 1

                # write PDF with first 20mb
                with open(
                    filepath.replace(".pdf", "-{}.pdf".format(pdfs_count)), "wb"
                ) as out:
                    pdf_writer.write(out)

                current_page = end_page + 1
                end_page += avg_step
                if end_page > total_pages:
                    end_page = total_pages
                pdfs_count += 1


if __name__ == "__main__":
    main(prog_name="pdf-split-tool")  # pragma: no cover
