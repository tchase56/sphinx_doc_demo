# Sphinx Documentation Demo

This repository demonstrates how to utilize Sphinx to automatically create professionally formatted documentation and publish it to GitHub Pages.

## Overview

This project provides two simple Python modules with utility functions:

1. **Simple Arithmetic** - Basic mathematical operations
2. **Simple String Operations** - Common string manipulation functions

## Installation

### Requirements

- Python 3.11.9
- uv (Python package manager)

### Setup

Clone the repository and synchronize dependencies:

```bash
git clone <repository-url>
cd sphinx_doc_demo
make sync
```

## Modules

### Simple Arithmetic (`src/simple_arithmetic.py`)

Provides basic arithmetic operations:

- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers (with zero-check)
- `power(a, b)` - Raise a number to a power

**Example:**
```python
from src.simple_arithmetic import add, multiply, power

result = add(5, 3)        # Returns 8
product = multiply(4, 5)  # Returns 20
squared = power(2, 3)     # Returns 8
```

### Simple String Operations (`src/simple_string.py`)

Provides common string manipulation functions:

- `concatenate(str1, str2)` - Combine two strings
- `to_uppercase(text)` / `to_lowercase(text)` - Change case
- `reverse_string(text)` - Reverse a string
- `count_characters(text)` / `count_words(text)` - Count characters or words
- `replace_substring(text, old, new)` - Replace substrings
- `split_string(text, delimiter)` - Split string into list
- `join_strings(strings, separator)` - Join list into string
- `starts_with(text, prefix)` / `ends_with(text, suffix)` - Check string boundaries
- `contains_substring(text, substring)` - Check if substring exists
- `get_substring(text, start, end)` - Extract substring
- `is_numeric(text)` / `is_alphabetic(text)` - Check string type

**Example:**
```python
from src.simple_string import concatenate, reverse_string, split_string

greeting = concatenate("Hello", "World")  # Returns "HelloWorld"
reversed_text = reverse_string("hello")   # Returns "olleh"
words = split_string("hello,world", ",")  # Returns ['hello', 'world']
```

## Documentation

### Building Documentation

Generate HTML documentation using Sphinx:

```bash
make link_readme # only needs to be ran once
make docgen
```

The generated documentation will be in `docs/_build/html/`.

### Viewing Documentation

1. Viewing locally
    * Open `docs/_build/html/index.html` in your browser to view the documentation.

2. Viewing in github pages 
    * Type the following URL pattern into the browser
        * http:<organization-name>.GitHub.io/<repo-name>
    * Open the documentation directly from the repo
        * Go to the repository's Settings.
        * Select Pages on the left pane and start configuring.
        * Click Visit site button at the top of the page

## Development

### Available Make Commands

- `make sync` - Synchronize project dependencies
- `make docgen` - Generate HTML documentation with Sphinx
- `make link_readme` - Create symbolic link for README.md in docs/

### Dependencies

**Development:**
- `black` - Code formatter

**Documentation:**
- `sphinx` (>=7.0, <8.0) - Documentation generator
- `sphinx-rtd-theme` (>=3.0.2) - Read the Docs theme
- `myst-parser` (>=2.0.0) - Markdown support for Sphinx

## Project Structure

```
sphinx_doc_demo/
├── Makefile              # Build automation
├── pyproject.toml        # Project configuration
├── README.md            # This file
├── docs/                # Sphinx documentation
│   ├── conf.py         # Sphinx configuration
│   ├── index.rst       # Documentation index
│   ├── python_modules.rst
│   └── _build/         # Generated documentation
└── src/                # Source code
    ├── simple_arithmetic.py
    └── simple_string.py
```
