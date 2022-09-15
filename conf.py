from datetime import date
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Adshares"
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
html_theme = "furo"
html_theme_path = ["_themes"]
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"
html_css_files = ['custom.css']
html_theme_options = {
    "light_logo": "logo.svg",
    "dark_logo": "logo-dark-mode.svg",
    "light_css_variables": {
        "font-stack": "'HCo Gotham', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', 'Liberation Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'",
        "color-brand-primary": "#000",
        "color-brand-content": "#1aa8bf",
    },
    "dark_css_variables": {
        "color-foreground-primary": "#ddd",
        "color-brand-primary": "#ddd",
        "color-brand-content": "#1aa8bf",
    },
#     "touch_icon" : "apple-touch-icon.png",
    "sidebar_hide_name": True,
}
