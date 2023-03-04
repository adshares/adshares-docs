.. _protocol-payments-moneyflow:

Money flow
==========

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
    