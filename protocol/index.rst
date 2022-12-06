
.. _adshares-protocol:

Adshares Protocol
===================================

Simplified workflow
-------------------

.. uml::
    :align: center

    skinparam monochrome true

    actor       "Publisher"         as publisher
    actor       "User"              as user
    participant "Supply AdServer"   as supplyServer
    participant "ADS Blockchain"    as blockchain
    participant "Demand AdServer"   as demandServer
    actor       "Advertiser"        as advertiser

    ==Synchronization==

    demandServer -> blockchain: Broadcast
    supplyServer -> blockchain: Fetch broadcasts
    blockchain --> supplyServer: List of broadcasts
    supplyServer -> demandServer : Fetch inventory
    demandServer --> supplyServer: Inventory
    supplyServer -> supplyServer: Update AdServer's inventory

    ==Impressions==

    user -> supplyServer : Register event

    user -> supplyServer : Find creatives
    supplyServer --> user : Return creatives

    user -> demandServer : Get creative content
    demandServer --> user : Return creative content

    user -> supplyServer: View event
    supplyServer -> demandServer: View event //redirected//
    user -> demandServer : Register event

    user -> supplyServer : Click event
    supplyServer -> demandServer : Click event //redirected//
    demandServer -> advertiser : Click event //redirected//

    ==Payments==

    demandServer -> blockchain: Send multi transaction
    supplyServer -> blockchain: Fetch transactions
    blockchain --> supplyServer: List of transactions
    supplyServer -> demandServer: Fetch report
    demandServer --> supplyServer: Return report
    supplyServer -> publisher: Post profit

Contents
--------
.. toctree::
    :maxdepth: 1

    authentication
    taxonomy/index
    synchronization/index
    impressions/index
    payments/index
..    conversions/index
