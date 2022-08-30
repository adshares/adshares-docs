
Quality
===================================

To ensure the best quality we decided to use two approaches:

* BDD - business cases (Behat)
* TDD - unit tests (PHPUnit)

To run unit tests execute:

::

    ./vendor/bin/phpunit

To run BDD tests execute:

::

    ./vendor/bin/behat

Coding styles rules are ensured by several tools:

* Sensio Security Checker
* PHP Static Analysis Tool
* PHP Codesniffer
* PHP Parallel Lint

One command can be used to run all tools above:

::

    composer qa-check

You can also run all commands separately:

* ``security-checker security:check``
* ``parallel-lint --no-colors --blame --exclude vendor .``
* ``phpcs -s --standard=PHPCompatibility src tests``
* ``phpcs -s --standard=PSR2 src tests``
* ``phpstan --no-ansi --no-progress analyse -c phpstan.neon -l 7 src tests``
