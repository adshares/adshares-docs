
Cryptovoxels code for web3ads
===============================

Put following script into ``image`` feature.
Remember to fill out your payout address

.. code-block:: js

   let config = {
       "payout_network": "{PAYOUT_NETWORK}", // payout network "ads" or "bsc"
       "payout_address": "{PAYOUT_ADDRESS}", // your wallet address (AAAA-BBBBBBBB-CCCC for ads network, 0xabcd... for bsc)
       "adserver": "https://app.web3ads.net" // visit web3ads.net to see banner stats
   }

   fetch(config.adserver + "/supply/cryptovoxels.js").then(function(response) {
       response.text().then(function(text) {
           eval(text);
       });
   });
