from datetime import date
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Adshares Documentation"
copyright = "2018-{}, Adshares".format(date.today().year)
author = "Adshares"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ["_templates"]
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "README.md"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "_static/favicon.ico"
html_theme = "alabaster"
html_theme_path = ["_themes"]
html_static_path = ["_static"]
html_theme_options = {
    "font_family": "'HCo Gotham', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'",
    "font_size": "16px",
    "logo" : "adshares-logo.svg",
    "touch_icon" : "apple-touch-icon.png",
}
