"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Pdf Split Tool."""


if __name__ == "__main__":
    main(prog_name="pdf-split-tool")  # pragma: no cover
