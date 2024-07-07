# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = u"scimpl"
copyright = u"2024, Ryan Park"
author = u"Ryan Park"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # View the documentation compilation times.
    "sphinx.ext.duration",
    # Actually run documented interpreter script
    "sphinx.ext.doctest",
    # Auto generate docs for methods, module, classes etc.
    "sphinx.ext.autodoc",
    # Auto generate summaries for classes and their corresponding
    # docs.
    "sphinx.ext.autosummary",
    # Mathtext ":math:" in docs
    "sphinx.ext.mathjax",
    # Google docstring parsing
    "sphinx.ext.napoleon",
    # Link source code in docs
    "sphinx.ext.viewcode",
    # Link to external docs
    "sphinx.ext.intersphinx",
    # RTD html theme
    "sphinx_rtd_theme",
]
autoapi_dirs = ["../../src"]

intersphinx_mapping = {
    "python": ("http://docs.python.org/", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/dev", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
}


templates_path = ["_templates"]
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# -- Latex options
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

