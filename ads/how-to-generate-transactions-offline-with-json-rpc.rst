.. _ads-json-rpc:

How to generate transactions offline with JSON-RPC
==================================================

Abstract
--------

The ADS blockchain allows users to prepare transactions and execute them later.
The aim of this article is to show how to sign a transaction and execute it later without the secret key.
This flow is widely used by exchanges, because secret key does not have to be transferred anywhere (even through safe channels).

This article also introduces ``ads-json-rpc``, the JSON-RPC client for ADS.

Requirements
------------

.. _json-rpc-client-for-ads:

JSON-RPC client for ADS
^^^^^^^^^^^^^^^^^^^^^^^

The JSON-RPC client for ADS (``ads-json-rpc``) was created to simplify ``ads`` wallet program usage.
It supports most of :ref:`ADS API methods <ads-api-methods>`
and complies `JSON-RPC <https://www.jsonrpc.org/specification>`_ specification version 2.0.
The client can be used for creating transaction for ADS blockchain.
The ``ads-json-rpc`` is part of ``ads-tool`` package.
It's installation and usage is described in details on `ads-tools project page <https://github.com/adshares/ads-tools>`_.

Adshares made publicly available JSON-RPC clients for ADS Mainnet and Testnet.

* mainnet: https://rpc.adshares.net
* testnet: https://rpc.e11.click

Both clients have disabled transaction methods, but can send transactions to network using ``send_again`` method.

Installation
~~~~~~~~~~~~

Binary version of ``ads-json-rpc`` can be installed from official *Adshares PPA*.

.. code-block::

   sudo add-apt-repository ppa:adshares/releases -y
   sudo apt-get update
   sudo apt-get install ads ads-tools

Setup
~~~~~

Run ``ads-json-rpc -h`` to get the list of command line options and config file parameters.
To ensure operation working directory must contains ``settings.cfg`` file with ``address``, ``host``, ``port``, and ``secret`` set.
Below is sample content of ``settings.cfg`` file.

.. code-block::

   port=6511
   host=127.0.0.1
   address=0001-00000000-XXXX
   secret=0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF

Above file should be placed in working directory.
The ``ads-json-rpc`` client utilizes two working directories:

* first for read_only functions
* second for transactions

By default working directories are the same as for ``ads`` client which is ``$HOME/.ads``.
They can be changed with ``--working-dir`` [``-w``] and ``--transactions-dir`` [``-t``] option.

It is important that publicly available clients should forbid to execute transaction functions, eg. send_one.
Therefore ``--transactions-dir`` should be set to empty directory, or at least to directory where ``settings.cfg`` file is NOT present.

Usage
~~~~~

The ``ads-json-rpc`` supports `JSON-RPC <https://www.jsonrpc.org/specification>`_ specification version 2.0.
It means that each request must have body with request id, method, parameters, and supported JSON-RPC version.
All requests must be **HTTP POST** and should have header ``Content-Type: application/json``.

The client supports most of :ref:`ADS API methods <ads-api-methods>`.
Method ``get_block`` cannot be requested directly.
It is called by client in background while needed.
All others method can be requested with parameters described in :ref:`ADS API methods <ads-api-methods>` documentation.
Name of the method must be given as ``method`` instead of run parameter.
Other parameters must be passed as fields of ``params`` object.

Below is example body of request executed with curl.

.. code-block::

   curl -X POST 127.0.0.1:6868 \
   -H "Content-Type: application/json" \
   -d @- << EOF
   {
       "jsonrpc": "2.0",
       "id": "1",
       "method": "get_account",
       "params": {
           "address": "0001-00000000-9B6F"
       }
   }
   EOF

It is equivalent to the following ``ads`` call.

.. code-block::

   echo '{"run":"get_account","address":"0001-00000000-9B6F"}' | ads

The dry-run option for ads client causes that transaction will not be sent to network.
Functions which read network status are not affected by this options.
The dry-run is turned off by default.
It can be enabled in ``ads-json-rpc`` by adding special param ``"_dry-run": true``.

Dry-run example
~~~~~~~~~~~~~~~

Below is example usage of dry-run.
Function ``broadcast`` allows send message up to 32,000 bytes.
Compare output with and without dry-run.
Meaning of msid and hash option will be explained in next paragraph.

Dry-run is on.
Parameter ``"_dry-run": true`` is added.
Transaction will not be sent.

.. code-block::

   curl -X POST 127.0.0.1:6868 \
   -H "Content-Type: application/json" \
   -d @- << EOF
   {
       "jsonrpc": "2.0",
       "id": "1",
       "method": "broadcast",
       "params": {
           "message": "01020304050607080900",
           "_dry-run": true
       }
   }
   EOF

.. code-block::

   {
       "id": "1",
       "jsonrpc": "2.0",
       "result": {
           "current_block_time": "1547033088",
           "previous_block_time": "1547032576",
           "tx": {
               "account_hashin": "6967DE3325EEB7A3C0B2EC1DC88539E76A8185D4371F8C591417F04836860423",
               "account_hashout": "E3500202C37D7CE1D45AF789CEF69E481FE9544CEBEB5D82D9C481AD62ADBCC3",
               "account_msid": "12",
               "data": "030100050000000C00000074DA355C0A0001020304050607080900",
               "deduct": "0.00000010000",
               "fee": "0.00000010000",
               "signature": "DECA9D7E4D74AFB3F6D085FEDFEF57BE1259F750AC70D47ECA57ADE67F559FF658C1900E324E5373BF2AB851F2F037E4A01EE09FE24CDEF6E296BA235744630C",
               "time": "1547033204"
           }
       }
   }

Dry-run is off.
Parameter ``"_dry-run"`` is omitted.
Transaction will be sent.

.. code-block::

   curl -X POST 127.0.0.1:6868 \
   -H "Content-Type: application/json" \
   -d @- << EOF
   {
       "jsonrpc": "2.0",
       "id": "1",
       "method": "broadcast",
       "params": {
           "message": "01020304050607080900"
       }
   }
   EOF

.. code-block::

   {
       "id": "1",
       "jsonrpc": "2.0",
       "result": {
           "account": {
               "address": "0001-00000005-CBCA",
               "balance": "1041.93194747647",
               "date": "2019-01-09 12:28:02",
               "hash": "43AB819727F407DE32DC0BD8174353DD0890ECF087F67EFD8A9445CEC64F5334",
               "id": "5",
               "local_change": "1547033088",
               "msid": "13",
               "node": "1",
               "paired_id": "0",
               "paired_node": "0",
               "public_key": "860BB97F2E355C094CEFB63A7A1245C3D3073E535087FBACEF573C6EC48E17A9",
               "remote_change": "1545309696",
               "status": "0",
               "time": "1547033282"
           },
           "current_block_time": "1547033088",
           "previous_block_time": "1547032576",
           "tx": {
               "account_hashin": "6967DE3325EEB7A3C0B2EC1DC88539E76A8185D4371F8C591417F04836860423",
               "account_hashout": "43AB819727F407DE32DC0BD8174353DD0890ECF087F67EFD8A9445CEC64F5334",
               "account_msid": "12",
               "data": "030100050000000C000000C2DA355C0A0001020304050607080900",
               "deduct": "0.00000010000",
               "fee": "0.00000010000",
               "id": "0001:000016FE:0001",
               "node_mpos": "1",
               "node_msid": "5886",
               "signature": "539F038651996E7045C8DD0011AAD528A4644A5C7AE445F66DE3E9D6AB9E4EAD7837A567699039E16CCD58CDF5AFB9C60ECDE517532B28DA44B3614500BF7405",
               "time": "1547033282"
           }
       }
   }

When dry-run is not active transaction is sent to network.
In this case response has additional fields.
The most important elements are:

* ``result.tx.id`` - id of transaction assigned by node, which means that node accepted transaction
* ``result.account`` object - current state of account, which created transaction

Blockchain network account
^^^^^^^^^^^^^^^^^^^^^^^^^^

ADS account will be treat as transaction issuer and will be charged for executing transaction.

Address
~~~~~~~

Address is needed to indicate transaction's sender.
Every account has unique address assigned during creation.

Secret key, msid, hash
~~~~~~~~~~~~~~~~~~~~~~

Secret key, msid, and hash are required to sign transaction.
**Secret key** is private and should not be revealed to anyone.
**Msid** is number of account's transactions.
**Hash** is hash of last transaction.
Both msid and hash are public.
They are changing after each transaction.
They can be read from:


* `block explorer <https://operator.adshares.net/blockexplorer>`_: node -> account -> account details
* response of :ref:`get_account <get_account>` function
* previous transaction

Host and port of node
~~~~~~~~~~~~~~~~~~~~~

Node's host and port must be known to connect to the network and send transaction.

Transaction signing
-------------------

Each transaction must be signed before executing.
Usually sign and execute operations are done together, but this article describes different approach as mentioned in abstract.

Assume that money transfer of 12 ADS should be sent to account 0002-00000001-659C.
Transfer can be written as ``send_one`` transaction.
All transaction types are listed on :ref:`ADS API methods <ads-api-methods>` page.

Below is example ``ads`` client input.

.. code-block::

   {"run":"send_one", "amount":"12", "address":"0002-00000001-659C"}

Below is the same request for ``ads-json-rpc`` client.

.. code-block::

   {
       "jsonrpc": "2.0",
       "id": "1",
       "method": "send_one",
       "params": {
           "address": "0002-00000001-659C",
           "amount": "12"
       }
   }

Option ``"_dry-run": true`` should be used to get transaction signature without executing it.
Also ``msid`` and ``hash`` should be provided.

Below is curl request.

.. code-block::

   curl -X POST 127.0.0.1:6868 \
   -H "Content-Type: application/json" \
   -d @- << EOF
   {
       "jsonrpc": "2.0",
       "id": "1",
       "method": "send_one",
       "params": {
           "address": "0002-00000001-659C",
           "amount": "12",
           "_dry-run": true,
           "hash": "EED4BB783ABA5A2943CCB59F4DBE48845651CF650BDBA06C74A8334F9AAB726F",
           "msid": 14
       }
   }
   EOF

Below is the response after formatting.

.. code-block::

   {
       "id": "1",
       "jsonrpc": "2.0",
       "result": {
           "current_block_time": "1547053568",
           "previous_block_time": "1547053056",
           "tx": {
               "account_hashin": "EED4BB783ABA5A2943CCB59F4DBE48845651CF650BDBA06C74A8334F9AAB726F",
               "account_hashout": "3D4DC529AC97D1AA76A5F4B4D4E8515A22E7AD84A025DC3D451575FD20D74E73",
               "account_msid": "14",
               "data": "040100050000000E0000001A2B365C02000100000000E09265170100000000000000000000000000000000000000000000000000000000000000000000",
               "deduct": "12.01200000000",
               "fee": "0.01200000000",
               "signature": "6A6E0166C7CE584FC4885E4EE9DF4FD731B93B0C927426B7469A53603A6DAFAF73EF2EC7405BAD745BC2925430DA6DC2988DE790B0C99ED438D0C6453CA1450A",
               "time": "1547053850"
           }
       }
   }

To send transaction ``result.tx.data`` and ``result.tx.signature`` from above response are needed.
The ``result.tx.data`` is transaction data encoded as hexadecimal string.
Length of this string varies between transactions.
If You want to prepare next transaction, increment ``msid`` and use ``result.tx.account_hashout`` as ``params.hash``.

Transaction send
----------------

Send transaction without secret key using encoded transaction data and signature.
To connect to node only node's host and port are needed.
They are passed as special parameters ``_host`` and ``_port``.

.. code-block::

   curl -X POST 127.0.0.1:6868 -H "Content-Type: application/json" -d @- << EOF
   {
       "jsonrpc": "2.0",
       "id": "1",
       "method": "send_again",
       "params": {
           "data": "040100050000000E0000001A2B365C02000100000000E09265170100000000000000000000000000000000000000000000000000000000000000000000",
           "signature": "6A6E0166C7CE584FC4885E4EE9DF4FD731B93B0C927426B7469A53603A6DAFAF73EF2EC7405BAD745BC2925430DA6DC2988DE790B0C99ED438D0C6453CA1450A",
           "_host": "t01.e11.click",
           "_port": 6511
       }
   }
   EOF

Below is the formatted response.

.. code-block::

   {
       "id": "1",
       "jsonrpc": "2.0",
       "result": {
           "account": {
               "address": "0001-00000005-CBCA",
               "balance": "1017.90794747647",
               "date": "2019-01-09 18:10:50",
               "hash": "3D4DC529AC97D1AA76A5F4B4D4E8515A22E7AD84A025DC3D451575FD20D74E73",
               "id": "5",
               "local_change": "1547054080",
               "msid": "15",
               "node": "1",
               "paired_id": "0",
               "paired_node": "0",
               "public_key": "860BB97F2E355C094CEFB63A7A1245C3D3073E535087FBACEF573C6EC48E17A9",
               "remote_change": "1545309696",
               "status": "0",
               "time": "1547053850"
           },
           "current_block_time": "1547054080",
           "previous_block_time": "1547053568",
           "tx": {
               "data": "040100050000000E0000001A2B365C02000100000000E09265170100000000000000000000000000000000000000000000000000000000000000000000",
               "deduct": "12.01200000000",
               "fee": "0.01200000000",
               "id": "0001:00001700:0001",
               "node_mpos": "1",
               "node_msid": "5888",
               "signature": "6A6E0166C7CE584FC4885E4EE9DF4FD731B93B0C927426B7469A53603A6DAFAF73EF2EC7405BAD745BC2925430DA6DC2988DE790B0C99ED438D0C6453CA1450A",
               "time": "1547053850"
           }
       }
   }

Note that in ``result`` object ``tx.data`` and ``tx.signature`` are the same as given,
``account.msid`` and ``account.hash`` are the same as read from *dry-run* response.
Transaction was accepted by node, because ``result.tx.id`` is present.

Generating transaction batches
------------------------------

Transaction can be created in batches.
The most important thing to remember is not to change transaction order.
Transactions for particular account must be executed in the same order as they were signed.
It is result of fact that each transaction signature is generated using hash and incremented msid of previous transaction.
