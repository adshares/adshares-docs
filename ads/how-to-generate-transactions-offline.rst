
How to generate transactions offline
=====================================

Abstract
--------

The ADS blockchain allows users to prepare transactions and execute them later.
The aim of this article is to show how to sign a transaction and execute it later without the secret key.
This flow is widely used by exchanges, because secret key does not have to be transferred anywhere (even through safe channels).

Requirements
------------

Wallet program ``ads``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating transaction requires the ADS wallet program ``ads``.
Below are excerpts from the ADS documentation.
Installation and usage are described in details on `ADS project page <https://github.com/adshares/ads>`_.

Installation
~~~~~~~~~~~~

Binary version of ``ads`` can be installed from official *Adshares PPA*.

.. code-block::

   sudo add-apt-repository ppa:adshares/releases -y
   sudo apt-get update
   sudo apt-get install ads

Usage
~~~~~

Run ``ads -h`` to get the list of command line options and config file parameters.
While all options can be written in command line,
it is suggested to create ``settings.cfg`` file to store ``address``, ``host``, ``port``, and ``secret``.
Below is sample content of ``settings.cfg`` file.

.. code-block::

   port=6511
   host=127.0.0.1
   address=0001-00000000-XXXX
   secret=0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF

Above file should be placed in ``ads`` working directory.
By default working directory is ``$HOME/.ads``, but it can be changed with ``--work-dir`` [``-w``] option.

``ads`` support commands in JSON format.
The simplest command ``get_me`` does not need any parameters.
You can run ``ads`` and then type ``{"run":"get_me"}``.
Below is presented more convenient usage with stdout pipe.

.. code-block::

   echo '{"run":"get_me"}' | ads

Dry-run option ``--dry-run`` [``-d``] causes that transaction will not be sent to network.
Dry-run is turned off by default (value equal 0). Value of 1 turns dry-run on.
Please, note that functions which read network status are not affected by this options.

Dry-run example
~~~~~~~~~~~~~~~

Below is example usage of dry-run.
Function ``broadcast`` allows send message up to 32,000 bytes.
Compare output with and without dry-run.
Meaning of msid and hash option will be explained in next paragraph.

Dry-run is on, command line parameter ``--dry-run=1`` is added.
Transaction will not be sent.

.. code-block::

   echo '{"run":"broadcast", "message":"01020304"}' | ads -w . --msid=1 --hash=0671C3CF5044009E66AC8BE5896A28F967578F86BB956A3B5804AA5A3A6735A7 --dry-run=1

.. code-block::

   {
       "current_block_time": "1537527584",
       "previous_block_time": "1537527552",
       "tx": {
           "data": "030100000000000100000031CFA45B040001020304",
           "signature": "673EF843E69158B53FF7483101C79B9E0EC4B01F6FD58E758F596E05E01728620FB992D4668C4A4DFF2E03F9C7D0CB5FE766A5170DE52FE20BE0492062A10E07",
           "time": "1537527601",
           "account_msid": "1",
           "account_hashin": "0671C3CF5044009E66AC8BE5896A28F967578F86BB956A3B5804AA5A3A6735A7",
           "account_hashout": "D978D6996671E88E9121433B113F36107C0C8BD0E9644035616CAA7EB0C928C3",
           "deduct": "0.00000010000",
           "fee": "0.00000010000"
       }
   }

Dry-run is off, command line parameter ``--dry-run`` is omitted.
Transaction will be sent.

.. code-block::

   echo '{"run":"broadcast", "message":"01020304"}' | ads -w . --msid=1 --hash=0671C3CF5044009E66AC8BE5896A28F967578F86BB956A3B5804AA5A3A6735A7

.. code-block::

   {
       "current_block_time": "1537527616",
       "previous_block_time": "1537527584",
       "tx": {
           "data": "030100000000000100000044CFA45B040001020304",
           "signature": "E55B82E15F7F5A37BA2F83BF9D987F00A87F6116754F52F9A64527C7EB2224E2B6DFC1A0FF8F2CF5BDBA37958ACEFFF9B82D855B2ECB2C785E8CEF08FDA33802",
           "time": "1537527620",
           "account_msid": "1",
           "account_hashin": "0671C3CF5044009E66AC8BE5896A28F967578F86BB956A3B5804AA5A3A6735A7",
           "account_hashout": "5D23B4EFD69D255A5F8463AC9ED47739DF3C4AE70FAD35BAEDCAF212442E53F0",
           "deduct": "0.00000010000",
           "fee": "0.00000010000",
           "node_msid": "4",
           "node_mpos": "1",
           "id": "0001:00000004:0001"
       },
       "account": {
           "address": "0001-00000000-9B6F",
           "node": "1",
           "id": "0",
           "msid": "2",
           "time": "1537527620",
           "date": "2018-09-21 13:00:20",
           "status": "0",
           "paired_node": "0",
           "paired_id": "0",
           "local_change": "1537527616",
           "remote_change": "1537527584",
           "balance": "8612934.66646612606",
           "public_key": "A9C0D972D8AAB73805EC4A28291E052E3B5FAFE0ADC9D724917054E5E2690363",
           "hash": "5D23B4EFD69D255A5F8463AC9ED47739DF3C4AE70FAD35BAEDCAF212442E53F0"
       }
   }

When dry-run is not active transaction is sent to network.
In this case response has additional fields.
The most important elements are:


* ``tx.id`` - id of transaction assigned by node, which means that node accepted transaction
* ``account`` object - current state of account, which created transaction

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

IP address and port of node
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Node's IP address and port must be known to connect to the network and send transaction.

Transaction signing
-------------------

Each transaction must be signed before executing.
Usually sign and execute operations are done together, but this article describes different approach as mentioned in abstract.

Assume that money transfer of 120 ADS should be sent to account 0002-00000001-659C.
Transfer can be written as ``send_one`` transaction.
All transaction types are listed on :ref:`ADS API <ads-api-methods>` page.

.. code-block::

   {"run":"send_one", "amount":"120", "address":"0002-00000001-659C"}

Option ``is-dry-run=1`` should be used to get transaction signature without executing it.
Also ``msid`` and ``hash`` should be provided.
Following command assumes that secret key is stored in ``settings.cfg`` file inside working directory, so it does not need to be provided explicitly.

.. code-block::

   echo '{"run":"send_one", "amount":"120", "address":"0002-00000001-659C"}' | ads --dry-run=1 --msid=1 --hash=81900B3D4A4470946CE6A183BE20B4B8D620CF0E99C94EB06841713F008783E9

Below is the response.

.. code-block::

   {
       "current_block_time": "1537351648",
       "previous_block_time": "1537351616",
       "tx": {
           "data": "0401000100000001000000F71FA25B02000100000000C0BCF7E90A00000000000000000000000000000000000000000000000000000000000000000000",
           "signature": "1B0F7D6F0C10EF77B25827D27735FFB1D77D2372CC87D2AA385E376B6B780BC7B761DF9B58502807910BD20F5D117FD530E4760FC99B811AEA81F84BE733F50E",
           "time": "1537351671",
           "account_msid": "1",
           "account_hashin": "81900B3D4A4470946CE6A183BE20B4B8D620CF0E99C94EB06841713F008783E9",
           "account_hashout": "210CF7BE22C38E11E7828C52E58E21D20CDBC80F8BC3FE2D44BA74260568D835",
           "deduct": "120.12000000000",
           "fee": "0.12000000000"
       }
   }

To send transaction ``tx.data`` and ``tx.signature`` are needed.
The ``tx.data`` is transaction data encoded as hexadecimal string.
Length of this string varies between transactions.
If You want to prepare next transaction, increment ``msid`` and use ``tx.account_hashout`` as ``hash``.

Transaction send
----------------

Send transaction without secret key using encoded transaction data and signature. To connect to node only node's IP address and port are needed. Command below does not declare them explicitly, because they are stored in ``settings.cfg`` file.

.. code-block::

   echo '{"run":"send_again", "data":"0401000100000001000000F71FA25B02000100000000C0BCF7E90A00000000000000000000000000000000000000000000000000000000000000000000", "signature":"1B0F7D6F0C10EF77B25827D27735FFB1D77D2372CC87D2AA385E376B6B780BC7B761DF9B58502807910BD20F5D117FD530E4760FC99B811AEA81F84BE733F50E"}' | ads

Below is the response.

.. code-block::

   {
       "current_block_time": "1537353728",
       "previous_block_time": "1537353696",
       "tx": {
           "data": "0401000100000001000000F71FA25B02000100000000C0BCF7E90A00000000000000000000000000000000000000000000000000000000000000000000",
           "signature": "1B0F7D6F0C10EF77B25827D27735FFB1D77D2372CC87D2AA385E376B6B780BC7B761DF9B58502807910BD20F5D117FD530E4760FC99B811AEA81F84BE733F50E",
           "time": "1537351671",
           "deduct": "120.12000000000",
           "fee": "0.12000000000",
           "node_msid": "174",
           "node_mpos": "1",
           "id": "0001:000000AE:0001"
       },
       "account": {
           "address": "0001-00000001-8B4E",
           "node": "1",
           "id": "1",
           "msid": "2",
           "time": "1537351671",
           "date": "2018-09-19 12:07:51",
           "status": "0",
           "paired_node": "0",
           "paired_id": "0",
           "local_change": "1537353728",
           "remote_change": "1537342208",
           "balance": "2153113.52866666666",
           "public_key": "6431A8580B014DA2420FF32842B0BA3CAB3B77F01D1150E5A0D34743F243B778",
           "hash": "210CF7BE22C38E11E7828C52E58E21D20CDBC80F8BC3FE2D44BA74260568D835"
       }
   }

Please, note that ``tx.data`` and ``tx.signature`` are the same as given, ``account.msid`` and ``account.hash`` are the same as read from *dry-run* response.

Generating transaction batches
------------------------------

Transaction can be created in batches.
The most important thing to remember is not to change transaction order.
Transactions for particular account must be executed in the same order as they were signed.
It is result of fact that each transaction signature is generated using hash and incremented msid of previous transaction.
