.. _protocol-synchronization-sendbroadcast:

Sending broadcasts
==================

To become a part of the network :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
need to inform other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` that they are accessible.

This is done on :ref:`ADS Blockchain <protocol-definitions-blockchain>` by broadcasting 
a URL pointing to :ref:`Platform Metadata <protocol-definitions-metadata>`.

Every 24 hours, all :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
are required to broadcast a URL pointing to their :ref:`Platform Metadata <protocol-definitions-metadata>`. 

.. note::

    Broadcast must be sent from the account declared in the ``adsAddress`` field, as defined in the :ref:`Metadata Fromat <protocol-synchronization-metadata>`.

The URL itself, as well as the :ref:`Platform Metadata <protocol-definitions-metadata>` behind it, need to adhere to specific formats:

.. toctree::
    :maxdepth: 1

    synch_broadcast_sending_url
    synch_broadcast_sending_metadata


::

    Instruction how to broadcast using *ads* client:
    :ref:`ADS API broadcast <broadcast>`

    We provide a PHP client for the ADS blockchain.

    The source code is available on GitHub: https://github.com/adshares/ads-php-client.

    Install the package with Composer::

    composer require adshares/ads-client

    We provide a JSON RPC client.

    The source code is available on GitHub: https://github.com/adshares/ads-json-rpc.