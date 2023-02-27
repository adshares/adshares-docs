.. _protocol-payments-receiving-scan:

Scan the blockchain for payments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check account log - get_log

Fetch incoming payments - entries with `type` ('send_many' || 'send_one') and `inout` equal `in`.

Extract:

- $transactionId = $logEntry['id']
- $amount = $logEntry['amount']
- $address = $logEntry['address']

It is recommended to store the timestamp of the last event in order to limit the log during a subsequent call.

.. _protocol-payments-receiving-validate:

Validate transaction
^^^^^^^^^^^^^^^^^^^^

Update blockchain data - get_block

Fetch valid transaction's data - get_transaction

Extract `type` - it should match ('send_many' || 'send_one')

:ref:`How to check incoming transactions <how-to-check-incoming-transactions>`