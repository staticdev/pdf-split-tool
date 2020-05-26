"""Command-line interface."""
import click

import pdf_split_tool.file_handler
import pdf_split_tool.pdf_splitter


@click.command()
@click.version_option()
@click.option(
    "-m",
    "--max-size",
    type=int,
    help="Max size in megabytes.",
    default=20,
    show_default=True,
)
def main(max_size: int) -> None:
    """Pdf Split Tool."""
    max_size_bytes = max_size * 1024 * 1024  # convert to MB
    filepaths = pdf_split_tool.file_handler.get_filenames("*.pdf")
    for filepath in filepaths:
        splitter = pdf_split_tool.pdf_splitter.PdfSplitter(filepath)
        valid = splitter.validate_resolution()
        if not valid:
            click.secho(
                (
                    "Warning: {} has more than 200kb per page. "
                    "Consider reducing resolution before splitting."
                ).format(filepath),
                fg="yellow",
            )
            if not click.confirm("Do you want to continue?"):
                click.secho("{} skipped.".format(filepath), fg="blue")
                continue
        splitter.split_max_size(max_size_bytes)


if __name__ == "__main__":
    main(prog_name="pdf-split-tool")  # pragma: no cover
