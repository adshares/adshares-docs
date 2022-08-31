
How to check incoming transactions
==================================

Abstract
--------

This article aims to explain how an owner of a particular account could list and check incoming transactions.

Requirements
------------

Blockchain network account
^^^^^^^^^^^^^^^^^^^^^^^^^^

Every user of ADS blockchain needs an account to connect to the network.
An account can be created by the node operator or :ref:`Browser Wallet <how-to-use-ads-wallet>`.

Address
~~~~~~~

The address is needed to indicate the transaction's sender.
Every account has a unique address assigned during creation.

Secret key
~~~~~~~~~~

The secret key is needed to sign the transaction.
**Secret key** is private and should not be revealed to anyone.

IP address and port of node
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Node's IP address and port must be known to connect to the network and send transaction.

Communication with the node
^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the operations performed on the ADS blockchain are done using
the ADS wallet program :ref:`ads <ads_client_installation>`
or :ref:`JSON-RPC <json-rpc-client-for-ads>`.

Collecting transactions' ids from account's log
-----------------------------------------------

To get the account's log user needs to call ``get_log`` function.

Function ``get_log`` takes one parameter: ``from``.
Parameter ``from`` is the earliest time of the log entry in seconds since epoch as a decimal number.
If time is not provided (is equal zero) the full log will be returned.

Call with parameter ``from``

.. code-block::
   :caption: ads

   {"run":"get_log","from":"1543247363"}

.. code-block::
   :caption: JSON-RPC

   {"jsonrpc":"2.0","id":"1","method":"get_log", "params":{"address":"0001-00000004-DBEB","from":1543247363}}

Below is a sample response.
Account's events are in ``log`` array.
Log array can be empty if there are no events in the selected period.
Each event has ``time``, ``date``, ``type``, and ``type_no`` fields.
Different types of events have different structure.

.. code-block::

   {
       "current_block_time": "1543244800",
       "previous_block_time": "1543244288",
       "tx": {
           "data": "110200040000000100F05B",
           "signature": "029C4587D45DB0A5550E1155F6D4D3A159E2234C46290380FE28E80FCF5CF137467EC75928E9945102DA5F5916369F7ED16675F27D7363D0755090AB8CC8020A",
           "time": "1542455297",
           "account_msid": "0",
           "account_hashin": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "account_hashout": "9909BA21378298A96B132C73BBCD17757559350FE81ACAA5246C3B1614A9A345",
           "deduct": "0.00000000000",
           "fee": "0.00000000000"
       },
       "account": {
           "address": "0002-00000004-3539",
           "node": "2",
           "id": "4",
           "msid": "64",
           "time": "1543230001",
           "date": "2018-11-26 12:00:01",
           "status": "0",
           "paired_node": "0",
           "paired_id": "0",
           "local_change": "1543229952",
           "remote_change": "1542197760",
           "balance": "1042.79299389909",
           "public_key": "860BB97F2E355C094CEFB63A7A1245C3D3073E535087FBACEF573C6EC48E17A9",
           "hash": "5D4D150853A7BBF2713EE23BA3774B88493A7C95990C9E5E506197E45D76362E"
       },
       "log": [{
               "time": "1542291341",
               "date": "2018-11-15 15:15:41",
               "type_no": "32768",
               "confirmed": "yes",
               "type": "node_started",
               "node_start_msid": "3189",
               "node_start_block": "1542290432",
               "account": {
                   "balance": "1043.99939870000",
                   "local_change": "1542290432",
                   "remote_change": "1542197760",
                   "hash_prefix_8": "177D7A31BF3F915C",
                   "public_key_prefix_6": "860BB97F2E35",
                   "status": "0",
                   "msid": "14",
                   "node": "0",
                   "id": "0",
                   "address": "0000-00000000-313E"
               },
               "dividend": "0.00000000000"
           }, {
               "time": "1542455298",
               "date": "2018-11-17 12:48:18",
               "type_no": "32784",
               "confirmed": "yes",
               "type": "dividend",
               "node_msid": "3320",
               "block_id": "5BF00000",
               "dividend": "-0.00020000000"
           },
           {
               "time": "1543248387",
               "date": "2018-11-26 17:06:27",
               "type_no": "32772",
               "confirmed": "no",
               "type": "send_one",
               "node": "1",
               "account": "4",
               "address": "0001-00000004-DBEB",
               "node_msid": "3744",
               "node_mpos": "1",
               "account_msid": "11",
               "amount": "1.00000000000",
               "sender_fee": "0.00100000000",
               "message": "000000000000000000000000000000002A3DBD3F9B1A4E41AED0A3C0732BC729",
               "inout": "in",
               "id": "0001:00000EA0:0001"
           }
       ]
   }

To make a list of incoming transactions, a log must be filtered.
Incoming transactions have field ``type`` equal ``send_one`` or ``send_many`` and field ``inout`` equal ``in``.

For those events which match the filter field, ``id`` should be stored to process later.

Only one incoming transaction is present in the log example above. Its id is ``0001:00000EA0:0001``.

See more:

* :ref:`API: get_log function <get_log>`

Validation of transactions' IDs
-------------------------------

If transaction ID is known, it should be checked in ADS blockchain.
Transaction checking is divided into two parts:

* collecting block headers (**required only when using ``ads`` program**)
* comparing transaction id with collected headers

Collecting block header
^^^^^^^^^^^^^^^^^^^^^^^

Collecting the block header should be done before checking transaction ids.

Collecting header depends on calling ``get_blocks`` function in loop as long as all header will be updated.

.. code-block::

   {"run":"get_blocks"}

All headers are updated when a value of ``updated_blocks`` is equal 0.
Below is sample response after a successful update.

.. code-block::

   {
       "current_block_time": "1543249408",
       "previous_block_time": "1543248896",
       "tx": {
           "data": "130200040000006E1EFC5B001EFC5B00000000",
           "signature": "C1201AA1EC8D8FD1DA31FB3F1AF59D3DF0AB431FC82657D18DCBD436EECD2D0D636755F7FA0F50AB529EED8AD56BCA9236B402DD9A44D1D51327A9027B802A07",
           "time": "1543249518"
       },
       "updated_blocks": "0"
   }

See more:

* :ref:`API: get_blocks function <get_blocks>`

Checking transaction id
^^^^^^^^^^^^^^^^^^^^^^^

Comparing transaction id with collected headers needs to call ``get_transaction`` function.
It takes one required parameter ``txid`` - transaction id.

.. code-block::

   {"run":"get_transaction","txid":"0001:00000EA0:0001"} #ads
   {"jsonrpc":"2.0","id":"1","method":"get_transaction", "params":{"txid":"0001:00000EA0:0001"}} #JSON-RPC

Below are sample responses for ``send_one`` and ``send_many``.

Example for ``send_one``:

.. code-block::

   {
       "current_block_time": "1543249408",
       "previous_block_time": "1543248896",
       "tx": {
           "data": "140200040000006E1FFC5B0100A00E00000100",
           "signature": "F8A1244D8C0FD364715A439585787DAD7854614DA91B3D1451F68314F1DCB14309526A84ED4AE771A8C75C61969054355CFC8E63743F4AE76DD6117B4C978E0D",
           "time": "1543249774",
           "account_msid": "0",
           "account_hashin": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "account_hashout": "6B9F7E7D4EAD9292AE4273246CCA7E691DB595E01F66A0A6478C5841C8BC34F4",
           "deduct": "0.00000000000",
           "fee": "0.00000000000"
       },
       "network_tx": {
           "id": "0001:00000EA0:0001",
           "block_time": "1543247872",
           "block_id": "5BFC1800",
           "node": "1",
           "node_msid": "3744",
           "node_mpos": "1",
           "size": "125",
           "hashpath_size": "6",
           "data": "040100040000000B000000C118FC5B02000400000000E8764817000000000000000000000000000000000000002A3DBD3F9B1A4E41AED0A3C0732BC7291515D72AF2D0041D8F41727740F8B40A662BC1D7691A00E9B85FE8B15DC5A6C0B08AB898569F432531D89FC762B128962EABD895B3F1D41FB12851B15860E908",
           "hashpath": [
               "D35C5C427D59F0F461CAAE33D941CFF01A3A0F2BFB4A86E349408F45BB48AEBA",
               "807C957C867CA1FA190E1FCDD22A626685E9C554E2235B699142932DE96CE089",
               "BCF77DCB77AA3FB6328B35998DC5917F81F8EF96F82B5441B2FFDD0DBBFC8480",
               "3C90B8BCAE204C3479C45515D584D0F73061149A4427F2716F4E8026BCFA8536",
               "18340797415AF7E5F7B6A61815C210D7007635EA242800A805408BAFBFE76842",
               "F26A9BD1C882E83B865C6EFD82F789FD7548A6A40748BBF4C384B87DB86B8C7B"
           ]
       },
       "txn": {
           "type": "send_one",
           "node": "1",
           "user": "4",
           "msg_id": "11",
           "time": "1543248065",
           "target_node": "2",
           "target_user": "4",
           "sender_fee": "0.00100000000",
           "sender_address": "0001-00000004-DBEB",
           "target_address": "0002-00000004-3539",
           "amount": "1.00000000000",
           "message": "000000000000000000000000000000002A3DBD3F9B1A4E41AED0A3C0732BC729",
           "signature": "1515D72AF2D0041D8F41727740F8B40A662BC1D7691A00E9B85FE8B15DC5A6C0B08AB898569F432531D89FC762B128962EABD895B3F1D41FB12851B15860E908"
       }
   }

Example for ``send_many``:

.. code-block::

   {
       "current_block_time": "1654508544",
       "previous_block_time": "1654508032",
       "tx": {
           "data": "140400A0050000C5CC9D6201002D3203000100",
           "signature": "B3F18514B2539076D812E47483DD14DB9179DB2DA4C64AF0E38E8AF0B211FFD2D1DACA353F1438C56BFF62820FC502D61B16AF8D7FF1A7368A39E5BA89C78E09",
           "time": "1654508741",
           "account_msid": "0",
           "account_hashin": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
           "account_hashout": "45DC956FE8D5ABBC91CFE0F26E9E5A329FEB106EE7113C32190F528825C1E646",
           "deduct": "0.00000000000",
           "fee": "0.00000000000"
       },
       "network_tx": {
           "id": "0001:0003322D:0001",
           "block_time": "1654507008",
           "block_id": "629DC600",
           "node": "1",
           "node_msid": "209453",
           "node_mpos": "1",
           "size": "137",
           "hashpath_size": "6",
           "data": "050100500000001A74010076C79D62040001005000000024B2E17B050000000100280000004F1B242C0900000001002400000037D82332000000000100F1000000216206CC02000000D4B100F6863E653E324AC2A29710381F50498542E632DD376DDB29AD4E2F56B93CCCA41E62F9ED159B96999A02C8E36ABC89C6B986768FE7A9089763EDF10309",
           "hashpath": [
               "2EB240327FE9456037CC5CCF15A9939021F12709A0E68594D3B9BDDAE3D41F3C",
               "19B0897550FF30A5DAAF070BE598F1BB39CA31349DC42BD397CF295722314A21",
               "58F49496542F04373F304EA3DE7EC4432B585C226BE6FF553E025CE94DC337EE",
               "9DC50BD44B3DC1DF1F741E4F0158C93F1FC70F0EE54DE708807D128E57AD0CBA",
               "4D11B80108C04776E01A27297F9C16E08CEA8F5FAB4593A8E9EF50D82ED2B696",
               "BEB926E8456D1E7EC9698A3C038D0E6323F55228786DB75803347BBAAA411628"
           ]
       },
       "txn": {
           "type": "send_many",
           "node": "1",
           "user": "80",
           "sender_address": "0001-00000050-C19A",
           "msg_id": "95258",
           "time": "1654507382",
           "wire_count": "4",
           "sender_fee": "0.00037901302",
           "wires": [
               {
                   "target_node": "1",
                   "target_user": "80",
                   "target_address": "0001-00000050-C19A",
                   "amount": "0.23553225252"
               },
               {
                   "target_node": "1",
                   "target_user": "40",
                   "target_address": "0001-00000028-3E05",
                   "amount": "0.39395269455"
               },
               {
                   "target_node": "1",
                   "target_user": "36",
                   "target_address": "0001-00000024-FF89",
                   "amount": "0.00841209911"
               },
               {
                   "target_node": "1",
                   "target_user": "241",
                   "target_address": "0001-000000F1-6451",
                   "amount": "0.12012904993"
               }
           ],
           "signature": "D4B100F6863E653E324AC2A29710381F50498542E632DD376DDB29AD4E2F56B93CCCA41E62F9ED159B96999A02C8E36ABC89C6B986768FE7A9089763EDF10309"
       }
   }

Transaction details can be read from ``txn`` object.
Especially, sender address is present in ``txn.sender_address``.

In case of ``send_one`` transfer the most important fields are:

* ``txn.amount`` - transaction amount
* ``txn.message`` - transaction title (memo)

.. warning::

    Field ``txn.time`` is insecure because it can be freely set by the user. Use time of the message or the block instead.

In case of ``send_many`` transfer, ``txn`` object holds data of all wires in ``wires`` array.
The transfer to the current account can be found by ``txn.wires[].target_address``.
Amount is in ``txn.wires[].amount`` field.


See more:

* :ref:`API: get_transaction function <get_transaction>`
