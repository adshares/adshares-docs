
Serve ad zone JS code locally to circumvent adblocks
======================================================

Ad blockers can be circumvent by replacing a server address which hosts ad units' script.
This operation demands changes in server's configuration.

Below is an example for the nginx server.
This excerpt from configuration has a proxy defined for script ``main.js``.
The ``main.js`` script is responsible for adding ads on page.

.. code-block::

   # can be put in /etc/nginx/nginx.conf if you use multiple virtual servers
   proxy_cache_path  /tmp/ads-cache  levels=1:2    keys_zone=ads:1m    inactive=24h  max_size=10m;

   server {

   # ... other site configuration options ... #

       location /main.js {
           expires 1h;
           proxy_pass https://ADSERVER_DOMAIN/main.js;
           proxy_ssl_server_name on;
           proxy_buffering on;

           proxy_cache            ads;
           proxy_cache_valid      200  1h;
           proxy_cache_use_stale  error timeout invalid_header updating;
       }
   }

Typically the configuration can be found in ``/etc/nginx/sites-enabled/YOUR-SITE`` or ``/etc/nginx/conf.d/*.conf`` file.
The ``ADSERVER_DOMAIN`` must be replaced with the valid domain.
The AdServer's domain can be obtained from common code for ad units.
It is available on the site's details page after clicking **Get code** button.

.. code-block:: html

   <!-- Common code for all ad units, should be inserted into head section -->
   <script type="text/javascript" src="https://ADSERVER_DOMAIN/main.js" async></script>
   <!-- End of common code -->

The AdServer's domain can be replaced with the publisher's site name, e.g.

.. code-block:: html

   <script type="text/javascript" src="https://example.com/main.js" async></script>

or left empty

.. code-block:: html

   <script type="text/javascript" src="/main.js" async></script>
