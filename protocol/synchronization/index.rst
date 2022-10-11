
.. _inventory:

Synchronization
===============

Workflow
--------

.. uml::
    :align: center

    skinparam monochrome true
    skinparam shadowing false

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

Contents
--------
.. toctree::
    :maxdepth: 1

    broadcasting
    discovering
    updating