.. _protocol-synchronization-sendbroadcast:

Sending broadcasts
==================

To become a part of the network :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
need to inform other entities that they are accessible.

This is done by broadcasting on :ref:`Adshares Blockchain <protocol-definitions-blockchain>`
a URL pointing to :ref:`Platform Metadata <protocol-definitions-metadata>`.

.. note::

    Broadcast must be sent from the account set as ``adsAddress`` in the :ref:`Metadata Fromat <protocol-synchronization-metadata>`.

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