
Incoming payments
=================
The supply side is responsible for scanning incoming ADS transfers for advertisement payments.

Scan ADS blockchain for payments
--------------------------------
Check account log - get_log

Fetch incoming payments - entries with `type` ('send_many' || 'send_one') and `inout` equal `in`.

Extract:

- $transactionId = $logEntry['id']
- $amount = $logEntry['amount']
- $address = $logEntry['address']

It is worth to store time of last event to limit log next time.

Validate transaction
--------------------
Update blockchain data - get_block

Fetch valid transaction's data - get_transaction

Extract `type` - it should match ('send_many' || 'send_one')


https://github.com/adshares/ads/wiki/How-to-check-incoming-transactions
