
Tests
========================

Tests are split into three categories:

* end-to-end
* unit
* coding style

End-to-end tests
-----------------------

Aim of end to end test is to check integration between PHP ADS Client and ADS blockchain network.
Therefore working network must be set and ADS client must be installed in system.
Tests are placed in ``tests/E2E`` directory and can be run with PHPUnit.
ADS network configuration can be setup in ``phpunit.xml`` file.

Unit tests
-------------------------

Unit tests are placed in ``tests/Unit`` directory and can be run with PHPUnit.

Coding style tests
------------------------------

`PHP Code Sniffer` is used to check compatibility with PHP language and PSR-12 standard.

::

    ./vendor/bin/phpcs -s --standard=PHPCompatibility src tests
    ./vendor/bin/phpcs -s --standard=PSR12 src tests

`PHP Code Beautifier and Fixer` can be used for automatic fix of PSR-12 incompatibility.

::

    ./vendor/bin/phpcbf -s --standard=PSR12 src tests

`PHPStan` is used for static analysis.

::

    ./vendor/bin/phpstan --no-ansi --no-progress analyse -c phpstan.neon -l 7 src tests
