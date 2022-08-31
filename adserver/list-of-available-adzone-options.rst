
.. _list-of-available-adzone-options:

List of available Adzone options
==================================

Adzone options can be provided by adding ``data-options`` attribute to zone HTML code (see example).

* ``adblock_only`` - Serve adshares ads only when adblock is present
* ``min_cpm={value}`` - Serve adshares ads only when expected CPM is at least ``{value}``

If adzone options makes adshares ads unavailable backfill/fallback code will be displayed.

Example
-------

.. code-block:: html

   <script src="http://example.com/-/find.js" async></script>

   <!-- Serve only for adblock users with minimum expected CPM of $1.5 -->
   <div class="xaabbccddeeff" data-options="adblock_only,min_cpm=1.5" data-zone="018ac5d9e1eb426abb20bbd52ce7911d" style="width:728px;height:90px;display: block;margin: 0 auto">
       <!--  style tag is only a container -->
       <style type="app/backfill">
           <!-- Render this code in other conditions -->
           <script async src="https://other.adnetwork.example.com/ads.js"></script>
           <div class="otherAdnetwork" data-zone="C-112233445566"></div>
           <!-- End of fallback/backfill code -->
       </style>
   </div>
   `
