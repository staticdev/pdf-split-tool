"""Command-line interface."""
import click

import pdf_split_tool.file_handler
import pdf_split_tool.pdf_splitter


def _confirm_split_file(filepath: str, max_size_bytes: int) -> None:
    """Split file if user confirms or is valid.

    Args:
        filepath: PDF path.
        max_size_bytes: max size in bytes.
    """
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
            return
    splitter.split_max_size(max_size_bytes)


@click.command()
@click.version_option()
@click.argument("filepath", type=click.Path(exists=True), default=".")
@click.option(
    "-m",
    "--max-size",
    type=int,
    help="Max size in megabytes.",
    default=20,
    show_default=True,
)
def main(filepath: str, max_size: int) -> None:
    """Pdf Split Tool."""
    max_size_bytes = max_size * 1024 * 1024  # convert to MB
    if filepath.endswith(".pdf"):
        _confirm_split_file(filepath, max_size_bytes)
    else:
        filepaths = pdf_split_tool.file_handler.get_filenames(filepath, "*.pdf")
        for path in filepaths:
            _confirm_split_file(path, max_size_bytes)


if __name__ == "__main__":
    main(prog_name="pdf-split-tool")  # pragma: no cover
