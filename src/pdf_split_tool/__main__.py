"""Command-line interface."""
import click

import pdf_split_tool.file_handler


@click.command()
@click.version_option()
def main() -> None:
    """Pdf Split Tool."""
    filenames = pdf_split_tool.file_handler.get_filenames("*.pdf")
    for filename in filenames:
        print(filename)


if __name__ == "__main__":
    main(prog_name="pdf-split-tool")  # pragma: no cover
