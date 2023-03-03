.. _protocol-synchronization:

Synchronization
===============

Why is synchronization needed?
------------------------------

For comparsion, here how :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` interact with each other in centralized systems:

* In the very moment a :ref:`User <protocol-definitions-user>` navigates to their :ref:`Site <protocol-definitions-site>`, :ref:`Publishers <protocol-definitions-publisher>` broadcast information regarding their :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`.
* :ref:`Advertisers <protocol-definitions-advertiser>` use the information contained in :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` (as well as :ref:`Context Data <protocol-definitions-contextdata>`) to offer their bids to buy advertising space.

However, in :ref:`Adshares Protocol <adshares-protocol>` a different workflow is applied:

* Prior to any :ref:`User <protocol-definitions-user>` interaction, :ref:`Publishers <protocol-definitions-publisher>` collect information about :ref:`Demand-Side Inventories <protocol-definitions-demandinventory>`, as declared by :ref:`Advertisers <protocol-definitions-advertiser>`, and :ref:`Advertisers <protocol-definitions-advertiser>` collect information about :ref:`Supply-Side Inventories <protocol-definitions-supplyinventory>`, as declared by :ref:`Publishers <protocol-definitions-publisher>`. This process is called :ref:`Synchronization <protocol-synchronization>`.
* In the very moment a :ref:`User <protocol-definitions-user>` navigates to their :ref:`Site <protocol-definitions-site>`, :ref:`Publishers <protocol-definitions-publisher>` use the information collected during :ref:`Synchronization <protocol-synchronization>` (as well as :ref:`Context Data <protocol-definitions-contextdata>`) to make a determination to whom it makes the most sense to sell space on their :ref:`Sites <protocol-definitions-site>`.

Thus, in :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* Every :ref:`Supply-Side Platform <protocol-definitions-ssp>` needs to inform all available :ref:`Demand-Side Platforms <protocol-definitions-dsp>` about its availability and its current :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`.
* Every :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to inform all available :ref:`Supply-Side Platforms <protocol-definitions-ssp>` about its availability and its current :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`.

And here is why :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` want to stay in sync by querying each other inventories:

* :ref:`Publishers <protocol-definitions-publisher>` query :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` to be able to choose among :ref:`Advertisers <protocol-definitions-advertiser>` willing to buy space on their :ref:`Sites <protocol-definitions-site>`.
* :ref:`Advertisers <protocol-definitions-advertiser>` query :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` to be able to specify what :ref:`Sites <protocol-definitions-site>` they want to include or exclude in their :ref:`Campaign<protocol-definitions-campaign>` definitions.

Synchronization workflow
------------------------

The following diagram presents an overview of the :ref:`Synchronization <protocol-synchronization>` process:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side Platform"      as SSP
    participant "ADS Blockchain"            as blockchain
    collections "Demand-Side Platforms"     as DSP

    ==Sending Broadcast==

    loop at least once every 24 hours
        SSP -> blockchain: Broadcast
    end

    loop at least once every 24 hours
        DSP -> blockchain: Broadcast
    end

    ==Receiving Broadcast==

    loop at least once every 24 hours
        SSP -> blockchain: Fetch broadcasts
        blockchain --> SSP: List of broadcasts
        SSP -> SSP: Analyze\nbroadcast
        SSP -> DSP: Fetch Platform Metadata
        DSP --> SSP: Return Platform Metadata
        SSP -> SSP: Update Platform Metadata
    end

    ==Updating Inventory==

    loop periodically
        SSP -> DSP : Fetch Demand-Side Inventory
        DSP --> SSP: Return Demand-Side Inventory
        SSP -> SSP: Update\nDemand-Side\nInventory
    end

    loop periodically
        DSP -> SSP : Fetch Supply-Side Inventory
        SSP --> DSP: Return Supply-Side Inventory
        DSP -> DSP: Update\nSupply-Side\nInventory
    end

:ref:`Synchronization <protocol-synchronization>` is done by :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
broadcasting via :ref:`ADS Blockchain <protocol-definitions-blockchain>` a URL pointing to :ref:`Platform Metadata <protocol-definitions-metadata>`.

Once the :ref:`Platform Metadata <protocol-definitions-metadata>` is retrieved, the next step is to retrieve
:ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` or  :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`.

This is done by using the endpoints contained in the :ref:`Platform Metadata <protocol-definitions-metadata>` ``inventoryUrl`` field:

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