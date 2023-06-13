.. _protocol-payments-receiving:

Receiving Payments
==================

The following diagram presents an overview of how :ref:`Supply-Side Platform <protocol-definitions-ssp>` receives
payments from corresponding :ref:`Demand-Side Platforms <protocol-definitions-dsp>`:

.. uml::
    :align: center

    skinparam monochrome true

    actor       "Publisher"                 as publisher
    participant "Ad Select\nModule"         as ASM
    participant "Supply-Side\nPlatform"     as SSP
    participant "ADS Blockchain"            as blockchain
    collections "Demand-Side\nPlatforms"    as DSP

    loop periodically
        SSP -> blockchain: Fetch transactions
        blockchain --> SSP: List of transactions
        SSP -> SSP: Analyze transactions

        SSP -> DSP: Fetch Payment Report
        DSP --> SSP: Payment Report
        SSP -> ASM: Analyze\nPayment Report
    end
    SSP -> publisher: Collect funds

:ref:`Supply-Side Platform <protocol-definitions-ssp>` is expected to scan :ref:`ADS Blockchain <protocol-definitions-blockchain>` 
for incoming :ref:`ADS <protocol-definitions-ads>` transfers.

If an incoming payment is detected, :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls the appropriate :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
to receive the corresponding :ref:`Payment Report <protocol-definitions-paymentreport>`.

The received :ref:`Payment Report <protocol-definitions-paymentreport>` allows :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
to observe which :ref:`Demand-Side Platforms <protocol-definitions-dsp>`, which :ref:`Impression Events <protocol-definitions-impression>` 
and which :ref:`Conversion Events <protocol-definitions-conversion>` are generating the most income.

This incentivizes a given :ref:`Supply-Side Platform <protocol-definitions-ssp>` (and its :ref:`Ad Select Module <protocol-definitions-asm>`) 
to continue choosing the same :ref:`Demand-Side Platform <protocol-definitions-dsp>` in the future.

Also, it's important to note that :ref:`Ad Select Module <protocol-definitions-asm>` needs to be kept updated about payments received by
:ref:`Supply-Side Platform <protocol-definitions-ssp>` from various :ref:`Demand-Side Platforms <protocol-definitions-dsp>`,
as this information might affect its future decisions on choosing :ref:`Creatives <protocol-definitions-creative>` from a particular
:ref:`Demand-Side Platform <protocol-definitions-dsp>`.

.. _protocol-payments-receiving-scan:

Scan the blockchain for payments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scanning is done by retrieving an account's log with the :ref:`get_log <get_log>` command.

In the log, extract inbound payments by searching for entries with `type` (:ref:`send_many <send_many>` || :ref:`send_one <send_one>`) and `inout` equal `in`.

Take note of the following fields:

* $transactionId = $logEntry['id']
* $amount = $logEntry['amount']
* $address = $logEntry['address']

.. note::
  It's recommended to store the timestamp of the last event in order to limit the log size during a subsequent call.

.. _protocol-payments-receiving-validate:

Validate transaction
^^^^^^^^^^^^^^^^^^^^

Retrieve blockchain data using the :ref:`get_block <get_block>` command.

Fetch valid transaction data using the :ref:`get_transaction <get_transaction>` command.

Extract `type` - it should match (:ref:`send_many <send_many>` || :ref:`send_one <send_one>`).

For more details, refer to this section of the documentation:
:ref:`How to check incoming transactions <how-to-check-incoming-transactions>`
