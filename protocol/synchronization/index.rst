.. _protocol-synchronization:

Synchronization
===============

Why is synchronization needed?
------------------------------

In centralized systems, :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>`
interact with each other in the following way:

* In the very moment a :ref:`User <protocol-definitions-user>` navigates to their :ref:`Site <protocol-definitions-site>`, :ref:`Supply-Side Platforms <protocol-definitions-ssp>` 
  broadcast information regarding their :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` and :ref:`Context Data <protocol-definitions-contextdata>`.
* :ref:`Demand-Side Platforms <protocol-definitions-dsp>` use the information contained in :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`
  and :ref:`Context Data <protocol-definitions-contextdata>` to offer their bids for buying advertising space.

However, in :ref:`Adshares Protocol <adshares-protocol>` a different workflow is applied:

* Prior to any :ref:`User <protocol-definitions-user>` interaction, :ref:`Supply-Side Platforms <protocol-definitions-ssp>` collect information 
  about :ref:`Demand-Side Inventories <protocol-definitions-demandinventory>`, as declared by :ref:`Demand-Side Platforms <protocol-definitions-dsp>`, 
  and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` collect information about :ref:`Supply-Side Inventories <protocol-definitions-supplyinventory>`,
  as declared by :ref:`Supply-Side Platforms <protocol-definitions-ssp>`. This process is called :ref:`Synchronization <protocol-synchronization>`.
* In the very moment a :ref:`User <protocol-definitions-user>` navigates to a :ref:`Site <protocol-definitions-site>`, :ref:`Supply-Side Platforms <protocol-definitions-ssp>` 
  use the information collected during :ref:`Synchronization <protocol-synchronization>` and :ref:`Context Data <protocol-definitions-contextdata>`
  to select the most appropriate :ref:`Creatives <protocol-definitions-creative>` to display in a given situation.

Thus, in :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* Every :ref:`Supply-Side Platform <protocol-definitions-ssp>` needs to inform all available :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
  about its availability and the current content of its :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`.
* Every :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to inform all available :ref:`Supply-Side Platforms <protocol-definitions-ssp>` 
  about its availability and the current content of its :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`.

And here is why :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
want to stay in sync by querying each other inventories:

* :ref:`Supply-Side Platforms <protocol-definitions-ssp>` query :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` 
  to be able to choose among :ref:`Demand-Side Platforms <protocol-definitions-dsp>` willing to buy space on their :ref:`Sites <protocol-definitions-site>`.
* :ref:`Demand-Side Platforms <protocol-definitions-dsp>` query :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`
  to be able to specify what :ref:`Sites <protocol-definitions-site>` they want to include or exclude in their :ref:`Campaign<protocol-definitions-campaign>` definitions.

Synchronization workflow
------------------------

The following diagram presents an overview of the :ref:`Synchronization <protocol-synchronization>` process:

.. uml::
    :align: center

    skinparam monochrome true

    collections "Supply-Side Platform"      as SSP
    participant "ADS Blockchain"            as blockchain
    collections "Demand-Side Platforms"     as DSP

    ==Sending Broadcast==

    loop at least once every 24 hours
        SSP ->          blockchain:   Send Broadcast
    end

    loop at least once every 24 hours
        DSP ->          blockchain:   Send Broadcast
    end

    ==Receiving Broadcast==

    loop at least once every 24 hours
        SSP ->          blockchain:   Fetch Broadcasts
        blockchain -->  SSP:          List of Broadcasts
        SSP ->          SSP:          Analyze\nBroadcast
        SSP ->          DSP:          Fetch Platform Metadata
        DSP -->         SSP:          Platform Metadata
        SSP ->          SSP:          Update\nPlatform\nMetadata
    end

    loop at least once every 24 hours
        DSP ->          blockchain:   Fetch Broadcasts
        blockchain -->  DSP:          List of Broadcasts
        DSP ->          DSP:          Analyze\nBroadcast
        DSP ->          SSP:          Fetch Platform Metadata
        SSP -->         DSP:          Platform Metadata
        DSP ->          DSP:          Update\nPlatform\nMetadata
    end

    ==Updating Inventory==

    loop periodically
        SSP ->          DSP:          Fetch Demand-Side Inventory
        DSP -->         SSP:          Demand-Side Inventory
        SSP ->          SSP:          Update\nDemand-Side\nInventory
    end

    loop periodically
        DSP ->          SSP:          Fetch Supply-Side Inventory
        SSP -->         DSP:          Supply-Side Inventory
        DSP ->          DSP:          Update\nSupply-Side\nInventory
    end

:ref:`Synchronization <protocol-synchronization>` is done by :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
broadcasting via :ref:`ADS Blockchain <protocol-definitions-blockchain>` a URL pointing to :ref:`Platform Metadata <protocol-definitions-platformmetadata>`.

Once the :ref:`Platform Metadata <protocol-definitions-platformmetadata>` is retrieved, the next step is to retrieve
:ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` or  :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`.

This is done by using the endpoints contained in the :ref:`Platform Metadata <protocol-definitions-platformmetadata>` ``supplyInventoryUrl`` and ``demandInventoryUrl`` fields:

* :ref:`Supply-Side Platform <protocol-definitions-ssp>` retrieves :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` 
  from all available :ref:`Demand-Side Platforms <protocol-definitions-dsp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` retrieves :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` 
  from all available :ref:`Supply-Side Platforms <protocol-definitions-ssp>`.

To be applicable, the inventory data needs to be classified by appropriate tags. In order to apply tagging for its inventory data:

* :ref:`Supply-Side Platform <protocol-definitions-ssp>` makes a request to its :ref:`Site Tagging Provider <protocol-definitions-stp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` makes a request to its :ref:`Creative Tagging Provider <protocol-definitions-ctp>`.

As inventory data is likely to change over time, the endpoints defined in ``supplyInventoryUrl`` and ``demandInventoryUrl`` fields need to be queried on a regular basis.

Contents
--------
.. toctree::
    :maxdepth: 1

    synch_broadcast_sending
    synch_broadcast_receiving
    synch_broadcast_metadata
    synch_inventory_demand
    synch_inventory_supply