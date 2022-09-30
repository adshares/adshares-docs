<p align="center">
    <a href="https://adshares.net/" title="Adshares sp. z o.o." target="_blank">
        <img src="https://adshares.net/logos/ads.svg" alt="Adshares" width="100" height="100">
    </a>
</p>
<h3 align="center"><small>Adshares / Docs</small></h3>

Build Documentation
-------------------

```bash
sudo apt install graphviz plantuml
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -U sphinx sphinx-design furo sphinxcontrib-plantuml graphviz
make html
deactivate
```

After generating docs, open `_build/html/index.html` file in browser.

Alternatively, serve them with the internal PHP server:

```bash
php -S localhost:8000 -t _build/html/
```

Browse `http://localhost:8000` to read the docs.


More info
---------

- [Sphinx](https://www.sphinx-doc.org/)
- [Sphinx Design](https://sphinx-design.readthedocs.io/)
- [Furo](https://github.com/pradyunsg/furo)
- [Graphviz extension](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html)
- [Graphviz](https://graphviz.org/)
- [PlantUML extension](https://github.com/sphinx-contrib/plantuml/)
- [PlantUML](https://plantuml.com/)