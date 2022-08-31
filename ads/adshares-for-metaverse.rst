
Adshares for Metaverse
======================

Overview
--------

Adshares is a decentralized auction protocol designed for advertising.
It utilizes offline auctions and micropayments in $ADS cryptocurrency to enable competitive pricing of ad space.

Adshares protocol is now powering network of adservers that provide monetization of ad space for web apps.
Network is handling over 6 million ad views per day.
Auction protocol is impartial to type of ad inventory being sold.
Thanks to that, our decentralized auction protocol can also be used in other domains of marketing, like inside metaverse.

What can we provide
-------------------

* Monetization of ad marketplace inside game that is compatible with decentralized environment
* Easy access to in-game ads for advertisers
* Decentralized and flexible direct payments mechanics (to game operator and/or directly to in-game ad space provider)
* Service/oracle that tag ads for efficient filtering of allowable ads
* Tools for whitelisting/blacklisting ads before allowing it in game
* Algorithms that optimize ad selection based on real-time payments flow
* All earnings are final - no chargebacks
* Open source software that allows easy customization

Requirements for integration
----------------------------

* Creation of ad rendering engine inside the game
* Specification of supported ad formats that will be accessible for advertisers
* Providing some way to allow advertisers to measure views or interactions with ads inside the game

Architecture
------------

.. image:: /_static/images/adshares_structure.png
   :target: /_static/images/adshares_structure.png
   :alt: structure


All the core building blocks of Adshares system are independent of ad formats and delivery media.
We have ready ad runtime engine for web ads.
In game ads need to implement only small part of our protocol and gain ability to access all others.
Below you can find lifecycle of ads as it is done one for website

AdServer
--------

AdServer is an open source software that can be run by any participant in Adshares ecosystem to handle their own publishing inventory.
AdServer is connected to other microservices handling various functions required for the protocol operations like: ad classification provider, ad selection algorithms, ...
Metaverse game can run own instance of adserver or can use hosted one.

Ad request
^^^^^^^^^^

Once there is a need to fill empty ad space ad engine send request to adserver to select best ad for a slot.
It provides list of acceptable formats and impression context.

**Request**

.. code-block::

    POST /find
    [{"zone_id": "44d423ff22484955ab8b27e531b32c7d", "format": "...", "context": "..."}, {"zone_id": "69cc6d93a3894e148a1e97dad514aa52", "..."}}

**Response**

.. code-block::

   [{
           "id": "e4eb8f16c7dd42f3b45c83b9ea198810",
           "publisher_id": "65fba894af014a109775f709c898331c",
           "zone_id": "44d423ff22484955ab8b27e531b32c7d",
           "pay_from": "0001-000000F1-6451",
           "type": "html",
           "size": "728x90",
           "serve_url": "https:\/\/qucoxaga.xyz\/serve\/xadb31c3a4fdb438988e5ac1b29ba6fe1.doc?v=6788",
           "creative_sha1": "6788544a7f7a5cdbb2ef7eda0d08935050276a7c",
           "click_url": "https:\/\/qucoxaga.xyz\/l\/n\/click\/e4eb8f16c7dd42f3b45c83b9ea198810?r=aHR0cHM6Ly9xdWNveGFnYS54eXovY2xpY2svYWRiMzFjM2E0ZmRiNDM4OTg4ZTVhYzFiMjliYTZmZTE",
           "view_url": "https:\/\/qucoxaga.xyz\/l\/n\/view\/e4eb8f16c7dd42f3b45c83b9ea198810?r=aHR0cHM6Ly9xdWNveGFnYS54eXovdmlldy9hZGIzMWMzYTRmZGI0Mzg5ODhlNWFjMWIyOWJhNmZlMQ",
           "rpm": 1.8
       }, {
           "id": "69cc6d93a3894e148a1e97dad514aa52",
           "publisher_id": "65fba894af014a109775f709c898331c",
           "zone_id": "1c22c78a1ae340abb339d623001cd21e",
           "pay_from": "0001-000000F1-6451",
           "type": "html",
           "size": "320x100",
           "serve_url": "https:\/\/qucoxaga.xyz\/serve\/x70d09fc4760b408387826de7b3439b7b.doc?v=90b8",
           "creative_sha1": "90b80132b75c925e73c2c73cd2148689c169b190",
           "click_url": "https:\/\/qucoxaga.xyz\/l\/n\/click\/69cc6d93a3894e148a1e97dad514aa52?r=aHR0cHM6Ly9xdWNveGFnYS54eXovY2xpY2svNzBkMDlmYzQ3NjBiNDA4Mzg3ODI2ZGU3YjM0MzliN2I",
           "view_url": "https:\/\/qucoxaga.xyz\/l\/n\/view\/69cc6d93a3894e148a1e97dad514aa52?r=aHR0cHM6Ly9xdWNveGFnYS54eXovdmlldy83MGQwOWZjNDc2MGI0MDgzODc4MjZkZTdiMzQzOWI3Yg",
           "rpm": 2.368
       }
   ]


* Adserver returns winning ads that best matches context and passes all publisher filters
* Rendering engine proceeds to download ad creative from ``server_url``
* Checks if content has matching hash
* Ad is rendered
* User interaction is logged through ``view_url`` and ``click_url`` and advertiser is notified
* Once advertiser verify ad view as valid payment is sent in $ADS

Once this mechanism is implemented in the game, adserver will handle rest of the tasks.
E.g. observe that all the ads matches specified set of filters, monitor incoming $ADS payments and improve ad selection based on real time payments flow.
Provide reports for advertisers, generate income reports, ...
