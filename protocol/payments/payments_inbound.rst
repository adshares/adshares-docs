Receiving payments
==================

:ref:`Supply-Side Platform <protocol-definitions-ssp>` is expected to scan :ref:`Adshares Blockchain <protocol-definitions-blockchain>` 
for incoming :ref:`ADS <protocol-definitions-ads>` transfers.

.. container:: protocol
  
  If an incoming payment is detected, :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls the appropriate :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  to receive its :ref:`Payment Report <protocol-definitions-paymentreport>`.

The received :ref:`Payment Report <protocol-definitions-paymentreport>` allows :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
to verify the consistency between the following datasets:

* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` and the resulting payment amounts reported by :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>`
* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` and the resulting payment amounts expected by :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`

.. note::
  The above reconciliation only refers to :ref:`Impression Events <protocol-definitions-impression>`, while :ref:`Conversion Events <protocol-definitions-conversion>` 
  cannot be reconciled in this way, as they are not reported to :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`. 
  Nevertheless, :ref:`Demand-Side Platform <protocol-definitions-dsp>` might want to include :ref:`Conversion Events <protocol-definitions-conversion>` 
  in the :ref:`Payment Report <protocol-definitions-paymentreport>`, as this builds trust and incentivizes :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  to keep choosing the same :ref:`Demand-Side Platform <protocol-definitions-dsp>` in the future.

Scan the blockchain for payments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check account log - get_log

Fetch incoming payments - entries with `type` ('send_many' || 'send_one') and `inout` equal `in`.

Extract:

- $transactionId = $logEntry['id']
- $amount = $logEntry['amount']
- $address = $logEntry['address']

It is recommended to store the timestamp of the last event to limit log next time.

Validate transaction
^^^^^^^^^^^^^^^^^^^^

Update blockchain data - get_block

Fetch valid transaction's data - get_transaction

Extract `type` - it should match ('send_many' || 'send_one')

:ref:`How to check incoming transactions <how-to-check-incoming-transactions>`
