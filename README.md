
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
