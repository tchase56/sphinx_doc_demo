import os
import sys

# Add paths for both 'import src.module' and 'from helper_functions import ...'
sys.path.insert(0, os.path.abspath(".."))  # For 'import src'
sys.path.insert(0, os.path.abspath("../src"))  # For legacy absolute imports

# Project information
project = "sphinx_doc_demo"
author = "Tyler Chase"
copyright = "2026/01/08", {author}
release = "0.1.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",  # Auto-generate documentation from docstrings
    "sphinx.ext.napoleon",  # Support for Google and NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.intersphinx",  # Link to other project's documentation
    "myst_parser",  # Support for Markdown files
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output options
html_theme = "sphinx_rtd_theme"

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}