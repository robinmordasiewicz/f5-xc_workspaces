# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'workspacess'
copyright = '2022, Robin Mordasiewicz'
author = 'Robin Mordasiewicz'
release = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["subprojecttoctree"]
is_subproject=False
readthedocs_url="https://f5-xc-workspaces.readthedocs.io"

html_theme_options = {
    "repository_url": "https://github.com/robinmordasiewicz/workspacedocs",
    "use_repository_button": True,
}

html_title = "Workspace Excercises"
html_logo = "logo_f5.svg"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
