
How to setup fallback backfill code
===================================

Adshares network can help you monetize your adblock traffic. Our solution can also increase your revenue based on regular traffic.

If you are already cooperating with other ad networks (e.g. Coinzilla, Cointraffic, Propeller Ads) you can use Adshares as an additional source of revenue.
What’s important, you’ll be able to use Adshares simultaneously with other ad networks.

Here’s how it works:
--------------------

Adshares ad units can be integrated with your site to serve part of the traffic (e.g. adblock traffic only).
Once you implement the code, Adshares ad unit becomes the primary one, and other ad network’s ad unit becomes the fallback one.

For instance, Adshares ad unit can be used to serve adblock traffic using the ``adblock_only`` option.
In case this option is used, the backfill code (i.e. other ad network’s ad unit) will be rendered for every user who is NOT using an ad blocker.
Implementing Adshares code on your site will not affect your revenue from other ad networks in any way.

**See** :ref:`List of available adzone options <list-of-available-adzone-options>`

Example
-------

The fallback code (i.e. other ad network’s ad unit) should be placed inside the zone div enclosed in the HTML comment.

.. code-block:: html

   <script src="http://example.com/-/find.js" async></script>

   <!-- Serve only for adblock users -->
   <div class="xaabbccddeeff" data-options="adblock_only" data-zone="018ac5d9e1eb426abb20bbd52ce7911d" style="width:728px;height:90px;display: block;margin: 0 auto">
       <!--backfill
       <script async src="https://other.adnetwork.example.com/ads.js"></script>
       <div class="otherAdnetwork" data-zone="C-12345678"></div>
       -->
   </div>
   `

If using HTML comments is not possible, the backfill code can be placed inside the ``<style>`` tag with the ``app/backfill`` type.

.. code-block:: html

   <script src="http://example.com/-/find.js" async></script>

   <!-- Serve only for adblock users -->
   <div class="xaabbccddeeff" data-options="adblock_only" data-zone="018ac5d9e1eb426abb20bbd52ce7911d" style="width:728px;height:90px;display: block;margin: 0 auto">
       <!--  style tag is only a container -->
       <style type="app/backfill">
           <!-- Render this code in other conditions -->
           <script async src="https://other.adnetwork.example.com/ads.js"></script>
           <div class="otherAdnetwork" data-zone="C-12345678"></div>
           <!-- End of fallback/backfill code -->
       </style>
   </div>
   `
