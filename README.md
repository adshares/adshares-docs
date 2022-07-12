<p align="center">
    <a href="https://adshares.net/" title="Adshares sp. z o.o." target="_blank">
        <img src="https://adshares.net/logos/ads.svg" alt="Adshares" width="100" height="100">
    </a>
</p>
<h3 align="center"><small>Adshares / Docs</small></h3>

Build Documentation
-------------------

```bash
$ apt-get install python3-sphinx

$ make html
```

After generating docs, open `./_build/html/index.html` file in browser.

Alternatively, serve them with the internal PHP server:

```bash
$ php -S localhost:8000 -t _build/html/
```

Browse `http://localhost:8000` to read the docs.
