
.. _payments:

Payments
========

Abstract
--------
.. @TODO

Workflow
--------

.. uml::
    :align: center

    skinparam monochrome true

    participant "Demand AdServer"   as demandServer
    participant "ADS Blockchain"    as blockchain
    collections "Supply AdServers"  as supplyServer
    actor       "Publisher"         as publisher

    ==Outgoing payments==

    loop every 1 hour
        demandServer -> demandServer: Generate report
        demandServer -> demandServer: Calculate payments
        demandServer -> blockchain: Send multi transaction
    end

    ==Incoming payments==

    loop periodically
        supplyServer -> blockchain: Fetch transactions
        supplyServer -> supplyServer: Analyze transactions

        supplyServer -> demandServer: Fetch report
        demandServer --> supplyServer: Return report
        supplyServer -> supplyServer: Analyze report
        supplyServer -> publisher: Profit
    end

Contents
--------
.. toctree::
    :maxdepth: 1

    payments_outgoing
    payments_incoming
