# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# region Project information
project = "PDBe API webinar series"
copyright = "2020, Protein Data Bank in Europe"
author = "Protein Data Bank in Europe"

# The short X.Y version
version = "1.0"
# The full version, including alpha/beta/rc tags
release = "1.0"

# endregion

# region General configuration

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "jupyter_sphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.todo",
    "sphinx_markdown_tables",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "recommonmark",
]
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3', None),
#     'rdkit': ('https://www.rdkit.org/docs/', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_parsers = {".rst": "restructuredtext", ".txt": "markdown", ".md": CommonMarkParser}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# endregion

# region Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
}
html_logo = "_static/imgs/pdbelogo.png"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/styles.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
# end region

# region Options for HTMLHelp output

# Output file base name for HTML help builder.
htmlhelp_basename = "pdbetutorials"

# endregion

# region Options for LaTeX output

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "pdbetutorials.tex",
        "pdbetutorials Documentation",
        "Protein Data Bank in Europe",
        "manual",
    ),
]
# endregion

# region Options for manual page output

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pdbetutorials", "pdbetutorials Documentation", [author], 1)]
# endregion

# region Options for Texinfo output

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "pdbetutorials",
        "pdbetutorials Documentation",
        author,
        "pdbetutorials",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# endregion

# region Extension configuration
github_doc_root = "https://github.com/rtfd/recommonmark/tree/master/doc/"


def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "url_resolver": lambda url: github_doc_root + url,
            "auto_toc_tree_section": "Contents",
        },
        True,
    )
    app.add_transform(AutoStructify)
    app.connect("autodoc-process-docstring", no_namedtuple_attrib_docstring)


def no_namedtuple_attrib_docstring(app, what, name, obj, options, lines):
    is_namedtuple_docstring = len(lines) == 1 and lines[0].startswith(
        "Alias for field number"
    )
    if is_namedtuple_docstring:
        # We don't return, so we need to purge in-place
        del lines[:]


# endregion
