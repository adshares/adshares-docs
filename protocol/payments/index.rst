.. _protocol-payments:

Payments
========

Workflow
--------
.. uml::
    :align: center

    skinparam monochrome true

    actor       "Publisher"             as publisher
    collections "Supply-Side Platforms" as SSP
    participant "ADS Blockchain"        as blockchain
    participant "Demand-Side Platform"  as DSP

    ==Outgoing payments==

    loop every 1 hour
        DSP -> DSP: Generate report
        DSP -> DSP: Calculate payments
        DSP -> blockchain: Send multi transaction
    end

    ==Incoming payments==

    loop periodically
        SSP -> blockchain: Fetch transactions
        blockchain --> SSP: List of transactions
        SSP -> SSP: Analyze transactions

        SSP -> DSP: Fetch report
        DSP --> SSP: Return report
        SSP -> SSP: Analyze report
        SSP -> publisher: Post profit
    end

:ref:`Demand-Side Platforms <protocol-definitions-dsp>` need to pay :ref:`Supply-Side Platforms <protocol-definitions-ssp>` they cooperate with
for :ref:`Impression Events <protocol-definitions-impression>` and :ref:`Conversion Events <protocol-definitions-conversion>` that have taken place in a given time interval.

Contents
--------
.. toctree::
    :maxdepth: 1

    payments_sending
    payments_receiving

Money flow
----------
.. uml::
    :align: center

    skinparam monochrome true
    skinparam linetype ortho

    actor   "Advertiser"        as advertiser
    actor   "Publisher"         as publisher
    agent   "Software provider" as provider
    agent   "Community"         as community

    node "Demand-Side \nPlatform" as DSP {
        circle  " " as demandIn #black
        card demandLicenseFee [
            License fee
            -----------
            <i>license dependent
            <i>CE free of charge
        ]
        card demandOperatorFee [
            Operator fee
            ------------
            <i>set by the operator
        ]
        card demandCommunityFee [
            Community fee
            -------------
            <i>1% fees
            <i>set by the DAO
        ]
        circle  " " as demandOut #white
    }

    node "Supply-Side \nPlatform" as SSP {
        circle  " " as supplyIn #black
        card supplyLicenseFee [
            License fee
            -----------
            <i>license dependent
            <i>CE free of charge
        ]
        card supplyOperatorFee [
            Operator fee
            ------------
            <i>set by the operator
        ]
        circle  " " as supplyOut #white
    }

    advertiser -ri-> DSP

    demandIn -[dashed]do-> demandLicenseFee
    demandLicenseFee --> provider
    demandLicenseFee -[dashed]do-> demandOperatorFee
    demandOperatorFee -[dashed]do-> demandCommunityFee
    demandCommunityFee --> community
    demandCommunityFee -[dashed]do-> demandOut

    DSP -[bold]ri-> SSP

    supplyIn -[dashed]do-> supplyLicenseFee
    supplyLicenseFee --> provider
    supplyLicenseFee -[dashed]do-> supplyOperatorFee
    supplyOperatorFee -[dashed]do-> supplyOut

    SSP -ri-> publisher