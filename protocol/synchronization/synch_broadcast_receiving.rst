.. _protocol-synchronization-receivebroadcast:

Receiving broadcasts
====================

Before connecting to other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` or :ref:`Demand-Side Platforms <protocol-definitions-dsp>` it is crucial to find them in the network.

At least every 24 hours, all :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
are expected to broadcast their :ref:`Platform Metadata <protocol-definitions-metadata>` using :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

This means that each block from last 24 hours must be checked for the presence of an URL.
Then, each URL must be checked to see if it points to :ref:`Platform Metadata <protocol-definitions-metadata>`.

:ref:`Platform Metadata <protocol-definitions-metadata>` is structred according to :ref:`Metadata Format <protocol-synchronization-metadata>`.

Here are the most important fields in the :ref:`Platform Metadata <protocol-definitions-metadata>`: 

* ``inventoryUrl``
* ``adsAddress``
