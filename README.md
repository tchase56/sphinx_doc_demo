# Sphinx Documentation Demo README

This repository demonstrates how to utilize Sphinx to automatically create professionally formatted documentation and publish it to GitHub Pages.

## Overview

This project provides Python modules with utility functions:

1. **Unit Conversions** - Distance and weight unit conversion functions
2. **Simple Arithmetic** - Basic mathematical operations (helper functions)
3. **Simple String Operations** - Common string manipulation functions

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

### Simple Arithmetic (`src/unit_conversions/helper_functions/simple_arithmetic.py`)

Provides basic arithmetic operations:

- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers (with zero-check)
- `power(a, b)` - Raise a number to a power
- `modulo(a, b)` - Calculate remainder of division
- `floor_divide(a, b)` - Perform floor division (integer division)
- `absolute(a)` - Get the absolute value of a number
- `negate(a)` - Negate a number (multiply by -1)

**Example:**
```python
from src.unit_conversions.helper_functions.simple_arithmetic import add, multiply, power, modulo

result = add(5, 3)        # Returns 8
product = multiply(4, 5)  # Returns 20
squared = power(2, 3)     # Returns 8
remainder = modulo(10, 3) # Returns 1
```

### Unit Conversions

#### Distance Conversions (`src/unit_conversions/distance_conversions.py`)

Convert between different distance units:

- `mi_to_km(miles)` - Convert miles to kilometers
- `km_to_mi(kilometers)` - Convert kilometers to miles
- `ft_to_m(feet)` - Convert feet to meters
- `m_to_ft(meters)` - Convert meters to feet
- `m_to_km(meters)` - Convert meters to kilometers
- `km_to_m(kilometers)` - Convert kilometers to meters
- `m_to_cm(meters)` - Convert meters to centimeters
- `cm_to_m(centimeters)` - Convert centimeters to meters
- `mi_to_ft(miles)` - Convert miles to feet
- `ft_to_mi(feet)` - Convert feet to miles
- `ft_to_in(feet)` - Convert feet to inches
- `in_to_ft(inches)` - Convert inches to feet

**Example:**
```python
from src.unit_conversions.distance_conversions import mi_to_km, ft_to_m

km = mi_to_km(5)  # Returns approximately 8.047
meters = ft_to_m(10)  # Returns approximately 3.048
```

#### Weight Conversions (`src/unit_conversions/weight_conversions.py`)

Convert between different weight units:

- `lb_to_kg(pounds)` - Convert pounds to kilograms
- `kg_to_lb(kilograms)` - Convert kilograms to pounds
- `oz_to_g(ounces)` - Convert ounces to grams
- `g_to_oz(grams)` - Convert grams to ounces
- `kg_to_g(kilograms)` - Convert kilograms to grams
- `g_to_kg(grams)` - Convert grams to kilograms
- `g_to_mg(grams)` - Convert grams to milligrams
- `mg_to_g(milligrams)` - Convert milligrams to grams
- `lb_to_oz(pounds)` - Convert pounds to ounces
- `oz_to_lb(ounces)` - Convert ounces to pounds

**Example:**
```python
from src.unit_conversions.weight_conversions import lb_to_kg, oz_to_g

kg = lb_to_kg(150)  # Returns approximately 68.04
grams = oz_to_g(16)    # Returns approximately 453.59
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
├── Makefile                  # Build automation
├── pyproject.toml            # Project configuration
├── README.md                 # This file
├── docs/                     # Sphinx documentation
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Documentation index
│   ├── python_modules.rst   # Python modules documentation
│   ├── api/                 # Auto-generated API docs
│   └── _build/              # Generated documentation
│       └── html/            # HTML output
└── src/                     # Source code
    ├── __init__.py
    ├── simple_string.py     # String operations
    └── unit_conversions/    # Unit conversion modules
        ├── __init__.py
        ├── distance_conversions.py
        ├── weight_conversions.py
        └── helper_functions/
            ├── __init__.py
            └── simple_arithmetic.py
```
