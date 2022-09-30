Quality
=========================

Tests
------------------------
We have Unit tests and UI (functional) tests in the project.
Each setup is completely different.

Unit test
^^^^^^^^^^^^

We use `Jest <https://jestjs.io/>`_ for Unit tests.
1. To run all tests type a command: ``npm run test``

UI test (functional)
^^^^^^^^^^^^^^^^^^^^^^^

#. Configure Selenium, WireMock, Maven
#. To run ``ui`` tests type a command: ``mvn verify``

Coding styles
------------------------
We use `ESlint <https://eslint.org/>`_ as a linting utility.
All configuration is stored in ``.eslintrc.js`` file.
Additionally we use `Prettier <https://github.com/prettier/prettier>`_ library to format code.

* To check source code run a command: ``npm run lint``
* To check ``prettier`` suggestions run a command: ``npm run prettify``
