.. _protocol-payments:

Payments
========

:ref:`Demand-Side Platforms <protocol-definitions-dsp>` need to pay :ref:`Supply-Side Platforms <protocol-definitions-ssp>` 
whose :ref:`Sites <protocol-definitions-site>` choose to display their :ref:`Creatives <protocol-definitions-creative>`.

The amount of this payment depends on the number of  :ref:`Impression Events <protocol-definitions-impression>` 
and :ref:`Conversion Events <protocol-definitions-conversion>` that have taken place in a given time interval.

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
