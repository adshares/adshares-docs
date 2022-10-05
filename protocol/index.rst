
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

    user -> supplyServer : Fetch banners
    supplyServer --> user : Return banners

    user -> demandServer : Get banner content
    demandServer --> user : Return banner content

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
    synchronization/index
    impressions/index
    payments/index
..    conversions/index
