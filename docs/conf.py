"""Sphinx configuration."""
from datetime import datetime


project = "Pdf Split Tool"
author = "Thiago Carvalho D'Ávila"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
autodoc_typehints = "description"
