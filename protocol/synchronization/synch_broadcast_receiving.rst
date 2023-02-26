.. _protocol-synchronization-receivebroadcast:

Receiving broadcasts
====================

Before connecting to other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` or :ref:`Demand-Side Platforms <protocol-definitions-dsp>` it is crucial to find them in the network.

At least every 24 hours, all :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
are expected to broadcast their :ref:`Platform Metadata <protocol-definitions-metadata>` using :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

This implies that if a :ref:`Supply-Side Platform <protocol-definitions-ssp>` or a :ref:`Demand-Side Platform <protocol-definitions-dsp>` wants to collect information 
about other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` or :ref:`Demand-Side Platforms <protocol-definitions-dsp>`, 
it needs to check every block created within the last 24 hours for the presence of a URL.

Then, each URL needs to be verified if it actually points to valid :ref:`Platform Metadata <protocol-definitions-metadata>`.

:ref:`Platform Metadata <protocol-definitions-metadata>` is structured according to :ref:`Metadata Format <protocol-synchronization-metadata>`.

In the :ref:`Metadata Format <protocol-synchronization-metadata>`, the most important field is ``inventoryUrl``, as it points to:

* the current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` of a :ref:`Supply-Side Platform <protocol-definitions-ssp>`
* the current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` of a :ref:`Demand-Side Platform <protocol-definitions-dsp>`

Another important field is ``adsAddress``, as it defines the :ref:`ADS Account <protocol-definitions-account>` address.
