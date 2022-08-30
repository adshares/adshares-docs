
Installation
===================================

#. Make sure you're using PHP (+mongodb module) 7.1 or higher and have `composer <https://getcomposer.org/>`_ installed
#. Clone repository: ``git clone https://github.com/adshares/ads-operator.git``
#. Create a configuration file ``.env`` based on ``.env.dist`` in the root of the application
#. Create Behat configuration file ``behat.yml`` based on ``behat.yml.dist`` in the root of the application
#. Install all dependencies using composer: ``composer install``
#. Add ``127.0.0.1 ads-operator.ads`` entry to your hosts

Nginx
--------------------

We assume that you've installed ADS Operator project in ``/ads-operator`` directory.

.. code-block::
   :caption: ads-operator.conf

    server {
        listen 80;

        server_name ads-operator.ads;
        root /ads-operator/public;

        index index.htm index.html index.php;

        location ~ /\.  {
            return 403;
        }

        location / {
            # try to serve file directly, fallback to rewrite
            try_files $uri $uri/ /index.php?$query_string;
        }

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        }

        location = /favicon.ico  {
            log_not_found off;
        }
    }
