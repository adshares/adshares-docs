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

To be able to interact with each other:

* Every :ref:`Supply-Side Platform <protocol-definitions-ssp>` needs to inform all available :ref:`Demand-Side Platforms <protocol-definitions-dsp>` about its availability and its current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`.
* Every :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to inform all available :ref:`Supply-Side Platforms <protocol-definitions-ssp>` about its availability and its current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`.

Here is why :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` might want to stay in sync by querying each other inventories:

* :ref:`Publishers <protocol-definitions-publisher>` query :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` to be able to choose among :ref:`Advertisers <protocol-definitions-advertiser>` willing to buy space on their :ref:`Sites <protocol-definitions-site>`.
* :ref:`Advertisers <protocol-definitions-advertiser>` query :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` to be able to specify what :ref:`Sites <protocol-definitions-site>` they want to include or exclude in their :ref:`Campaign<protocol-definitions-campaign>` definitions.

.. note::
    In most ecosystems, :ref:`Advertisers <protocol-definitions-advertiser>` receive information about :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` 
    declared by :ref:`Publishers <protocol-definitions-publisher>`, and based on this information they offer their bids to buy advertising space. 
    However, in :ref:`Adshares Protocol<adshares-protocol>` the opposite workflow is applied, i.e. :ref:`Publishers <protocol-definitions-publisher>` 
    collect information about :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` declared by :ref:`Advertisers <protocol-definitions-advertiser>`, 
    and based on this information they make a decision to whom they want to sell space on their :ref:`Sites <protocol-definitions-site>`.

This information sharing is done by :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
broadcasting via :ref:`Adshares Blockchain <protocol-definitions-blockchain>` a URL pointing to :ref:`Platform Metadata <protocol-definitions-metadata>`.

Once the :ref:`Platform Metadata <protocol-definitions-metadata>` is retrieved, the next step is to retrieve
:ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` or  :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`.

This is done by using the endpoints contained in the :ref:`Platform Metadata <protocol-definitions-metadata>` ``inventoryUrl`` field:

.. container:: protocol

    * :ref:`Supply-Side Platform <protocol-definitions-ssp>` retrieves :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` from all available :ref:`Demand-Side Platforms <protocol-definitions-dsp>`.
    * :ref:`Demand-Side Platform <protocol-definitions-dsp>` retrieves :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` from all available :ref:`Supply-Side Platforms <protocol-definitions-ssp>`.

To be useful, the inventory data needs to be tagged. In order to apply tagging for its inventory data:

* :ref:`Supply-Side Platform <protocol-definitions-ssp>` makes a request to its :ref:`Site Tagging Platform <protocol-definitions-stp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` makes a request to its :ref:`Creative Tagging Platform <protocol-definitions-ctp>`.

As inventory data is likely to change over time, the ``inventoryUrl`` needs to be queried on a regular basis.

Contents
--------
.. toctree::
    :maxdepth: 1

    synch_broadcast_sending
    synch_broadcast_receiving
    synch_inventory_demand
    synch_inventory_supply