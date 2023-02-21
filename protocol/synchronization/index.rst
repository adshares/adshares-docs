.. _protocol-synchronization:

Synchronization
===============

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply AdServer"   as supplyServer
    participant "ADS Blockchain"    as blockchain
    collections "Demand AdServers"  as demandServer

    ==Broadcasting==

    loop at least once every 24 hours
        supplyServer -> blockchain: Broadcast
    end

    loop at least once every 24 hours
        demandServer -> blockchain: Broadcast
    end

    ==Discovering==

    loop at least once every 24 hours
        supplyServer -> blockchain: Fetch broadcasts
        blockchain --> supplyServer: List of broadcasts
        supplyServer -> supplyServer: Analyze broadcast
        supplyServer -> demandServer: Fetch info
        demandServer --> supplyServer: Info
        supplyServer -> supplyServer: Update AdServer's info
    end

    ==Updating==

    loop periodically
        supplyServer -> demandServer : Fetch inventory
        demandServer --> supplyServer: Inventory
        supplyServer -> supplyServer: Update AdServer's inventory
    end

Workflow
--------

To be able to interact with each other:

* every :ref:`Supply-Side Platform <protocol-definitions-ssp>` needs to inform all potential :ref:`Demand-Side Platforms <protocol-definitions-dsp>` about its availability and its current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`
* every :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to inform all potential :ref:`Supply-Side Platforms <protocol-definitions-ssp>` about its availability and its current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`

This information sharing is done by broadcasting via :ref:`Adshares Blockchain <protocol-definitions-blockchain>` a URL pointing to JSON-based metadata.

The URL is published on :ref:`Adshares Blockchain <protocol-definitions-blockchain>` in the form of an uppercase hexadecimal string.

.. note::
    Most programming languages have a utility to convert an ASCII string to its hex representation. Online converters can be used as well.

.. container:: protocol

    Every 24 hours, all :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` are required to broadcast a URL pointing to their metadata. 

This implies that if a :ref:`Supply-Side Platform <protocol-definitions-ssp>` or a :ref:`Demand-Side Platform <protocol-definitions-dsp>` wants to collect information 
about other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` or :ref:`Demand-Side Platforms <protocol-definitions-dsp>`, 
it needs to check every block created within the last 24 hours for the presence of a URL. 
Then, each URL needs to be verified if it actually points to valid metadata.

Within the metadata, the most important field is `inventoryUrl`, as it points to:

* the current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` of a :ref:`Supply-Side Platform <protocol-definitions-ssp>`
* the current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` of a :ref:`Demand-Side Platform <protocol-definitions-dsp>`

In order to apply tagging for its inventory data:

* :ref:`Supply-Side Platform <protocol-definitions-ssp>` makes a request to its :ref:`Site Tagging Platform <protocol-definitions-stp>`
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` makes a request to its :ref:`Creative Tagging Platform <protocol-definitions-ctp>`

As inventory data is likely to change over time, the `inventoryUrl` needs to be queried on a regular basis.

Using the endpoints contained in the `inventoryUrl` field:

.. container:: protocol

    * :ref:`Supply-Side Platform <protocol-definitions-ssp>` retrieves :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` from all available :ref:`Demand-Side Platforms <protocol-definitions-dsp>`
    * :ref:`Demand-Side Platform <protocol-definitions-dsp>` retrieves :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` from all available :ref:`Supply-Side Platforms <protocol-definitions-ssp>`

.. note::
    In most ecosystems, :ref:`Advertisers <protocol-definitions-advertiser>` receive information about :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` 
    declared by :ref:`Publishers <protocol-definitions-publisher>`, and based on this information they offer their bids to buy advertising space. 
    However, in :ref:`Adshares Protocol<adshares-protocol>` the opposite workflow is applied, i.e. :ref:`Publishers <protocol-definitions-publisher>` 
    collect information about :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` declared by :ref:`Advertisers <protocol-definitions-advertiser>`, 
    and based on this information they make a decision to whom they want to sell space on their :ref:`Sites <protocol-definitions-site>`.

In summary, here is why :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` might want to stay in sync by querying each other inventories:

* :ref:`Publishers <protocol-definitions-publisher>` query :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` to be able to choose among :ref:`Advertisers <protocol-definitions-advertiser>` willing to buy space on their :ref:`Sites <protocol-definitions-site>`.
* :ref:`Advertisers <protocol-definitions-advertiser>` query :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` to be able to specify what :ref:`Sites <protocol-definitions-site>` they want to include or exclude in their :ref:`Campaign<protocol-definitions-campaign>` definitions.

Contents
--------
.. toctree::
    :maxdepth: 1

    synch_broadcasting
    synch_discovering
    synch_updating