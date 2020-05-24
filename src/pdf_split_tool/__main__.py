"""Command-line interface."""
import os

import click
import PyPDF4

import pdf_split_tool.file_handler


MAX_SIZE = 20 * 1024 * 1024  # 20 MB


@click.command()
@click.version_option()
def main() -> None:
    """Pdf Split Tool."""
    filepaths = pdf_split_tool.file_handler.get_filenames("*.pdf")
    for filepath in filepaths:
        size = os.path.getsize(filepath)
        print(filepath, size)
        if size > MAX_SIZE:
            input_pdf = PyPDF4.PdfFileReader(filepath, "rb")
            pdf_count = 0
            # need to create one instance per pdf
            pdf_writer = PyPDF4.PdfFileWriter()
            for page in range(0, 2):
                pdf_writer.addPage(input_pdf.getPage(page))
            # print("tamanho writer: {}".format(pdf_writer.size))
            with open(
                filepath.replace(".pdf", "-{}.pdf".format(pdf_count)), "wb"
            ) as out:
                pdf_writer.write(out)
            print("pdf-split!")


if __name__ == "__main__":
    main(prog_name="pdf-split-tool")  # pragma: no cover
