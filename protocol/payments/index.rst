
.. _payments:

Payments
========

Workflow
--------

.. uml::
    :align: center

    skinparam monochrome true
    skinparam shadowing false

    actor       "Publisher"         as publisher
    collections "Supply AdServers"  as supplyServer
    participant "ADS Blockchain"    as blockchain
    participant "Demand AdServer"   as demandServer

    ==Outgoing payments==

    loop every 1 hour
        demandServer -> demandServer: Generate report
        demandServer -> demandServer: Calculate payments
        demandServer -> blockchain: Send multi transaction
    end

    ==Incoming payments==

    loop periodically
        supplyServer -> blockchain: Fetch transactions
        blockchain --> supplyServer: List of transactions
        supplyServer -> supplyServer: Analyze transactions

        supplyServer -> demandServer: Fetch report
        demandServer --> supplyServer: Return report
        supplyServer -> supplyServer: Analyze report
        supplyServer -> publisher: Post profit
    end

Contents
--------
.. toctree::
    :maxdepth: 1

    payments_outgoing
    payments_incoming
