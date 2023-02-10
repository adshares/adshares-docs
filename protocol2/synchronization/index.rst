Synchronization
===============

.. _protocol-synchronization:

To be able to interact with each other:

* every :ref:`Supply-Side Platform <protocol-definitions-ssp>` needs to inform other :ref:`Demand-Side Platforms <protocol-definitions-dsp>` about its availablity and its current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`
* every :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to inform other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` about its availablity and its current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`

This information sharing is done by broadcasting via :ref:`Adshares Blockchain <protocol-definitions-blockchain>` a URL pointing to JSON-based metadata.

The URL is published on :ref:`Adshares Blockchain <protocol-definitions-blockchain>` in the form of an uppercase hexadecimal string.

.. note::
    Most programming languages have a utility to convert an ASCII string to its hex representation. Online converters can be used as well.

.. container:: protocol

    Every :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>` is required to broadcast a URL pointing to its metadata every 24 hours. 

This means that if a :ref:`Supply-Side Platform <protocol-definitions-ssp>` or a :ref:`Demand-Side Platform <protocol-definitions-dsp>` wants to collect information 
about other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` or :ref:`Demand-Side Platforms <protocol-definitions-dsp>`, 
it needs to check every block created within the last 24 hours for the presence of a URL. 
Then, each URL needs to be verified if it actually points to valid metadata.

Within the metadata, the most important field is `inventoryUrl`, as it points to:

* the current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` of a :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
* the current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` of a :ref:`Demand-Side Platform <protocol-definitions-dsp>` 

As inventory data is likely to change over time, the `inventoryUrl` needs to be queried on a regular basis.

Using the endpoints contained in the `inventoryUrl` field:

.. container:: protocol

    * :ref:`Supply-Side Platform <protocol-definitions-ssp>` retrieves :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` from all available :ref:`DSPs <protocol-definitions-dsp>`
    * :ref:`Demand-Side Platform <protocol-definitions-dsp>` retrieves :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` from all available :ref:`SSPs <protocol-definitions-ssp>`

.. note::
    In most ecosystems, :ref:`Advertisers <protocol-definitions-advertiser>` receive information about :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` 
    declared by :ref:`Publishers <protocol-definitions-publisher>`, and based on this information they offer their bids to buy advertising space. 
    However, in :ref:`Adshares Protocol<adshares-protocol2>` the opposite workflow is applied, i.e. :ref:`Publishers <protocol-definitions-publisher>` 
    collect information about :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` declared by :ref:`Advertisers <protocol-definitions-advertiser>`, 
    and based on this information they make a decision to whom they want to sell space on their :ref:`Sites <protocol-definitions-site>`.

In summary, here is why :ref:`SSPs <protocol-definitions-ssp>` and :ref:`DSPs <protocol-definitions-dsp>` might want to query each other:

* :ref:`Publishers <protocol-definitions-publisher>` query :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` to be able to choose among :ref:`Advertisers <protocol-definitions-advertiser>` willing to buy space on their :ref:`Sites <protocol-definitions-site>`.
* :ref:`Advertisers <protocol-definitions-advertiser>` query :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` to be able to specify what :ref:`Sites <protocol-definitions-site>` they want to include or exclude in their :ref:`Campaign<protocol-definitions-campaign>` definitions.
