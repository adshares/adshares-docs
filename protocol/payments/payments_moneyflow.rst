.. _protocol-payments-moneyflow:

Money Flow
==========

The following diagram presents an overview of how the money flows between various participants of :ref:`Adshares Protocol <adshares-protocol>`:

.. uml::
    :align: center

    skinparam monochrome true
    skinparam linetype ortho

    actor   "Advertiser"        as advertiser
    actor   "Publisher"         as publisher
    agent   "Software Provider" as provider
    agent   "Community"         as community

    node "Demand-Side\nPlatform" as DSP {
        circle " " as demandIn #black
        card demandLicenseFee [
            <u>License fee
            <i>license-dependent
            <i>CE free of charge
        ]
        card demandOperatorFee [
            <u>Operator fee
            <i>set by the operator
        ]
        card demandCommunityFee [
            <u>Community fee
            <i>1% fees
            <i>set by the DAO
        ]
        circle " " as demandOut #white
    }

    node "Supply-Side\nPlatform" as SSP {
        circle " " as supplyIn #black
        card supplyLicenseFee [
            <u>License fee
            <i>license-dependent
            <i>CE free of charge
        ]
        card supplyOperatorFee [
            <u>Operator fee
            <i>set by the operator
        ]
        circle " " as supplyOut #white
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

Types of deductions
-------------------

Generally, money flows from :ref:`Advertisers <protocol-definitions-advertiser>` to :ref:`Publishers <protocol-definitions-publisher>`.
But before funds reach a :ref:`Publisher <protocol-definitions-publisher>` some deductions are being made to reward all entities
participating in the process.

Funds get deposited
~~~~~~~~~~~~~~~~~~~

:ref:`Advertiser <protocol-definitions-advertiser>` deposits funds with a :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
Those funds are meant to be utilized as payments for displayed/converted :ref:`Creatives <protocol-definitions-creative>`.
    
Funds get transferred
~~~~~~~~~~~~~~~~~~~~~

The funds sent from :ref:`Demand-Side Platform <protocol-definitions-dsp>` to :ref:`Supply-Side Platform <protocol-definitions-ssp>` are reduced by the following amounts:

* License fee: an amount paid to a :ref:`Software Provider <protocol-definitions-softwareprovider>`. This fee depends on the license type.
  Software released as Community Edition (CE) is free of charge.
* Operator fee: an amount paid to the operators of the software constituting :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
* Community fee: an amount set to 1% of the cashflow, as decided by :ref:`Adshares DAO <dao>`.

Funds get released
~~~~~~~~~~~~~~~~~~

The funds released by :ref:`Supply-Side Platform <protocol-definitions-ssp>` to :ref:`Publisher <protocol-definitions-publisher>` are reduced by the following amounts:

* License fee: an amount paid to a :ref:`Software Provider <protocol-definitions-softwareprovider>`. This fee depends on the license type.
  Software released as Community Edition (CE) is free of charge.
* Operator fee: an amount paid to the operators of the software constituting :ref:`Supply-Side Platform <protocol-definitions-ssp>`.