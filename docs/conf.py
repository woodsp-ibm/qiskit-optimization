# This code is part of a Qiskit project.
#
# (C) Copyright IBM 2021, 2025.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("."))

import qiskit_optimization

# Set env flag so that we can doc functions that may otherwise not be loaded
# see for example interactive visualizations in qiskit.visualization.
os.environ["QISKIT_DOCS"] = "TRUE"

# -- Project information -----------------------------------------------------
project = "Qiskit Optimization"
copyright = f"2018, {date.today().year}, Qiskit Optimization Development Team"  # pylint: disable=redefined-builtin
author = "Qiskit Optimization Development Team"

docs_url_prefix = "qiskit-optimization"

# The short X.Y version
version = qiskit_optimization.__version__
# The full version, including alpha/beta/rc tags
release = qiskit_optimization.__version__

rst_prolog = """
.. raw:: html

    <br><br><br>

.. |version| replace:: {0}
""".format(
    release
)

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}
.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. note::
        This page was generated from `docs/{{ docname }}`__.

        __"""

vers = version.split(".")
link_str = f" https://github.com/qiskit-community/qiskit-optimization/blob/stable/{vers[0]}.{vers[1]}/docs/"
nbsphinx_prolog += link_str + "{{ docname }}"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx_design",
    "jupyter_sphinx",
    "reno.sphinxext",
    "sphinx.ext.doctest",
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "qiskit_sphinx_theme",
]
html_static_path = ["_static"]
templates_path = ["_templates"]

nbsphinx_timeout = 180
nbsphinx_execute = os.getenv("QISKIT_DOCS_BUILD_TUTORIALS", "never")
nbsphinx_widgets_path = ""
nbsphinx_thumbnails = {
    "tutorials/01_quadratic_program": "_static/1_quadratic_program.png",
    "tutorials/02_converters_for_quadratic_programs": "_static/2_converters.png",
    "tutorials/03_minimum_eigen_optimizer": "_static/3_min_eig_opt.png",
    "tutorials/04_grover_optimizer": "_static/4_grover.png",
    "tutorials/05_admm_optimizer": "_static/5_ADMM.png",
    "**": "_static/images/logo.png",
}

spelling_word_list_filename = "../.pylintdict"
spelling_filters = ["lowercase_filter.LowercaseFilter"]

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

autosummary_generate = True
autosummary_generate_overwrite = False

# -----------------------------------------------------------------------------
# Autodoc
# -----------------------------------------------------------------------------
# Move type hints from signatures to the parameter descriptions (except in overload cases, where
# that's not possible).
autodoc_typehints = "description"
# Only add type hints from signature to description body if the parameter has documentation.  The
# return type is always added to the description (if in the signature).
autodoc_typehints_description_target = "documented_params"

autodoc_default_options = {
    "inherited-members": None,
}

autoclass_content = "both"

# If true, figures, tables and code-blocks are automatically numbered if they
# have a caption.
numfig = True

# A dictionary mapping 'figure', 'table', 'code-block' and 'section' to
# strings that are used for format of figure numbers. As a special character,
# %s will be replaced to figure number.
numfig_format = {"table": "Table %s"}

translations_list = [
    ("en", "English"),
    ("ja_JP", "Japanese"),
    ("es_UN", "Spanish"),
]
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**site-packages", "_build", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "colorful"

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for
# py:function directives.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# This can be handy if you document a project that consists of a single
# package. Works only for the HTML builder currently.
modindex_common_prefix = ["qiskit_optimization."]

# -- Configuration for extlinks extension ------------------------------------
# Refer to https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html


# -- Options for HTML output -------------------------------------------------

html_theme = "qiskit-ecosystem"
html_title = f"{project} {release}"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "networkx": ("https://networkx.org/documentation/stable", None),
    "docplex.mp": ("https://ibmdecisionoptimization.github.io/docplex-doc/mp", None),
    "qiskit": ("https://quantum.cloud.ibm.com/docs/api/qiskit", None),
    "qiskit_algorithms": ("https://qiskit-community.github.io/qiskit-algorithms", None),
}

html_context = {"analytics_enabled": True}
