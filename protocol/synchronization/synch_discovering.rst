
Receiving broadcasts
====================

Before connecting to other :ref:`AdServers <protocol-definitions-adserver>` it is crucial to find them in the network.
At least every 24 hours, all :ref:`AdServers <protocol-definitions-adserver>` are expected to broadcast their metadata using :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

This means that each block from last 24 hours must be checked for the presence of an URL.
Then, each URL must be checked to see if it points to :ref:`AdServer <protocol-definitions-adserver>`'s metadata.

To check the expected format of :ref:`AdServer <protocol-definitions-adserver>`'s metadata read :ref:`Adserver's metadata <adserver_metadata>`.

Save ``inventoryUrl`` and ``adsAddress`` from each metadata.
