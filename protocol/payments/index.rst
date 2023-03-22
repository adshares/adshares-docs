.. _protocol-payments:

Payments
========

:ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to pay :ref:`Supply-Side Platform <protocol-definitions-ssp>` each time
its :ref:`Creative <protocol-definitions-creative>` is chosen to be displayed on a :ref:`Site <protocol-definitions-site>`.

The amount of this payment depends on the number of  :ref:`Impression Events <protocol-definitions-impression>` 
and :ref:`Conversion Events <protocol-definitions-conversion>` that have taken place in a given time interval.

From the technical perspective, the payment takes place between :ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Supply-Side Platform <protocol-definitions-ssp>`,
but the actual payer is :ref:`Advertiser <protocol-definitions-advertiser>`, whereas the actual payee is :ref:`Publisher <protocol-definitions-publisher>`.

Also, the cost for an :ref:`Advertiser <protocol-definitions-advertiser>` is a bit higher than the income of a :ref:`Publisher <protocol-definitions-publisher>` due to the fact that
some deductions take place, as described in the :doc:`Money Flow <payments_moneyflow>` section.

The following diagram presents an overview of the payment process:

.. uml::
    :align: center

    skinparam monochrome true

    actor       "Publisher"                 as publisher
    collections "Supply-Side\nPlatforms"    as SSP
    participant "ADS Blockchain"            as blockchain
    collections "Demand-Side\nPlatforms"    as DSP
    actor       "Advertiser"                as advertiser

    ==Outgoing payments==

    advertiser -> DSP: Deposit funds
    loop every 1 hour
        DSP -> DSP: Payment Report
        DSP -> DSP: Calculate payments
        DSP -> blockchain: Send multi transaction
    end

    ==Incoming payments==

    loop periodically
        SSP -> blockchain: Fetch transactions
        blockchain --> SSP: List of transactions
        SSP -> SSP: Analyze transactions

        SSP -> DSP: Fetch Payment Report
        DSP --> SSP: Payment Report
        SSP -> SSP: Analyze Payment Report
    end
    SSP -> publisher: Collect funds

Contents
--------
.. toctree::
    :maxdepth: 1

    payments_moneyflow
    payments_sending
    payments_receiving
