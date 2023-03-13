.. _protocol-payments-receiving:

Receiving payments
==================

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
to verify the consistency between the following datasets:

* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` 
  and the resulting payment amounts reported by :ref:`Demand-Side Platform <protocol-definitions-dsp>`
* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>`
  and the resulting payment amounts expected by :ref:`Supply-Side Platform <protocol-definitions-ssp>`

The above reconciliation only refers to :ref:`Impression Events <protocol-definitions-impression>`,
(i.e. :ref:`Register Events <protocol-definitions-registerevent>`, :ref:`View Events <protocol-definitions-viewevent>` and :ref:`Click Events <protocol-definitions-clickevent>`)
while :ref:`Conversion Events <protocol-definitions-conversion>` are not reconciled in this way, as they are only reported within 
:ref:`Demand-Side Infrastructure <protocol-definitions-dsi>`, thus without :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` being involved. 

Nevertheless, the :ref:`Ad Pay Module <protocol-definitions-apm>` operating within :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` 
is incentivised to include :ref:`Conversion Events <protocol-definitions-conversion>` in its :ref:`Payment Report <protocol-definitions-paymentreport>`,
as this builds trust and incentivizes the :ref:`Ad Select Module <protocol-definitions-asm>` of a given :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
to continue choosing the same :ref:`Demand-Side Platform <protocol-definitions-dsp>` in the future.

Also, it's important to note that :ref:`Ad Select Module <protocol-definitions-asm>` needs to be kept updated about the received payments,
as this information is likely to affect its future decisions on choosing :ref:`Creatives <protocol-definitions-creative>` 
from particular :ref:`Demand-Side Platforms <protocol-definitions-dsp>`.

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