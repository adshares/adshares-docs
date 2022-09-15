
Tests
=====

Requirements
------------

- PHP 8.1 with enabled APCu
- ElasticSearch 7.14

Install dependencies
--------------------

::

    composer self-update
    composer install --no-interaction
    wget -O local-php-security-checker https://github.com/fabpot/local-php-security-checker/releases/download/v2.0.4/local-php-security-checker_2.0.4_linux_amd64
    chmod +x local-php-security-checker

Run tests
---------

Check vulnerabilities

::

   ./local-php-security-checker

Check code style

::

   composer qa-check

Test code

::

   composer test-ci
