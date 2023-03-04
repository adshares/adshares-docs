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

        SSP -> DSP: Fetch Payment Report
        DSP --> SSP: Return Payment Report
        SSP -> SSP: Analyze Payment Report
        SSP -> publisher: Post profit
    end

Contents
--------
.. toctree::
    :maxdepth: 1

    payments_moneyflow
    payments_sending
    payments_receiving
