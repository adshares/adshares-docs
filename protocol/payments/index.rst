
.. _payments:

Payments
========

Money flow
----------

.. uml::
    :align: center

    skinparam monochrome true
    skinparam linetype ortho

    actor   "Advertiser"    as advertiser
    actor   "Publisher"     as publisher
    agent   "Software provider"      as provider
    agent   "Community"     as community

    node "Demand AdServer" as demandServerNode {
        circle  " "         as demandIn #black
        card demandLicenseFee [
            License fee
            ========
            <i>license dependent
            <i>CE free of charge
        ]
        card  "Operator fee"   as demandOperatorFee
        card demandCommunityFee [
            Community fee
            =========
            <i>1% fees
            <i>set by the DAO
        ]
        circle  " "         as demandOut #white
    }

    node "Supply AdServer" as supplyServerNode {
        circle  " "         as supplyIn #black
        card supplyLicenseFee [
            License fee
            ========
            <i>license dependent
            <i>CE free of charge
        ]
        card  "Operator fee"   as supplyOperatorFee
        circle  " "         as supplyOut #white
    }

    advertiser -ri-> demandServerNode

    demandIn -[dashed]do-> demandLicenseFee
    demandLicenseFee --> provider
    demandLicenseFee -[dashed]do-> demandOperatorFee
    demandOperatorFee -[dashed]do-> demandCommunityFee
    demandCommunityFee --> community
    demandCommunityFee -[dashed]do-> demandOut

    demandServerNode -[thickness=4]ri-> supplyServerNode: "payments"

    supplyIn -[dashed]do-> supplyLicenseFee
    supplyLicenseFee --> provider
    supplyLicenseFee -[dashed]do-> supplyOperatorFee
    supplyOperatorFee -[dashed]do-> supplyOut

    supplyServerNode -ri-> publisher

Workflow
--------

.. uml::
    :align: center

    skinparam monochrome true

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
