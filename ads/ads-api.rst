
.. _ads-api:

ADS API
=======

This document describes the format of the communication with the ADS wallet program (``ads``).


Command line parameters and config file options
-----------------------------------------------

Run ``ads -h`` to get the list of command line options and config file parameters.

.. code-block::

   > ads -h
   Usage: ads [settings]
   Generic options:
     -w [ --work-dir ] arg (=$HOME/.ads) working directory
     -v [ --version ]                    print version string
     -h [ --help ]                       produce help message

   Configuration [command_line + config_file]:
     -P [ --port ] arg (=6511)      node port (for clients)
     -H [ --host ] arg (=127.0.0.1) node hostname or ip
     -A [ --address ] arg           address (don't use with --bank, --user)
     -b [ --bank ] arg              node id (don't use with --address)
     -u [ --user ] arg              user id (don't use with --address)
     -i [ --msid ] arg (=0)         last message id
     -n [ --nice ] arg (=1)         request pretty json
     -o [ --olog ] arg (=1)         record submitted transactions in log file
     -d [ --dry-run ] arg (=0)      dry run (do not submit to network)
     -x [ --hash ] arg              last hash [64chars in hex format / 32bytes]
     -s [ --secret ] [=arg(=-)]     passphrase or private key [64chars in hex
                                    format / 32bytes]

The default config file is ``settings.cfg``.
You can store authentication data inside ``settings.cfg`` file or pass them as parameters.

Sample content of settings.cfg file:

.. code-block::

   port=6511
   host=127.0.0.1
   address=0001-00000000-XXXX
   secret=0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF

is equivalent to following parameters:

.. code-block::

   --port=6511 --host=127.0.0.1 --address=0001-00000000-XXXX --secret=0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF

Config file should be placed in **working directory**,
where cached data is stored as well.
Default location is ``$HOME/.ads`` directory.

If ``--secret`` parameter is used, but has default value ``-``, private key will be read from stdin.


.. _ads-api-methods:

Methods
-------

Methods are defined using the ``run`` input parameter.

.. list-table::
   :header-rows: 1

   * - name
     - description
   * - :ref:`broadcast <broadcast>`
     - broadcast a message on the network
   * - :ref:`change_account_key <change_account_key>`
     - change public key of my account
   * - :ref:`change_node_key <change_node_key>`
     - change public key of a node
   * - :ref:`create_account <create_account>`
     - create new user account
   * - :ref:`create_node <create_node>`
     - create new node
   * - :ref:`decode_raw <decode_raw>`
     - decode transaction
   * - :ref:`get_account <get_account>`
     - get account info by address
   * - :ref:`get_blocks <get_blocks>`
     - download and store block headers
   * - :ref:`get_broadcast <get_broadcast>`
     - download broadcast messages
   * - :ref:`get_log <get_log>`
     - download and store transaction log
   * - :ref:`get_me <get_me>`
     - get my account info
   * - :ref:`get_transaction <get_transaction>`
     - get info about a single transaction
   * - :ref:`get_vipkeys <get_vipkyes>`
     - get list of public keys of VIP nodes
   * - :ref:`get_signatures <get_signatures>`
     - get signatures of a block
   * - :ref:`get_block <get_block>`
     - get block header and list of nodes
   * - :ref:`get_accounts <get_accounts>`
     - get account of a node
   * - :ref:`get_message_list <get_message_list>`
     - get list of messages in a block
   * - :ref:`get_message <get_message>`
     - get message in a block
   * - :ref:`log_account <log_account>`
     - record account state in network
   * - :ref:`retrieve_funds <retrieve_funds>`
     - retrieve funds from a remote node
   * - :ref:`send_again <send_again>`
     - resend a transaction
   * - :ref:`send_one <send_one>`
     - send payment to one destination
   * - :ref:`send_many <send_many>`
     - send payment to many destinations
   * - :ref:`set_account_status <set_account_status>`
     - set status bits of a user account
   * - :ref:`set_node_status <set_node_status>`
     - set status bits of a node
   * - :ref:`unset_account_status <unset_account_status>`
     - unset status bits of a user account
   * - :ref:`unset_node_status <unset_node_status>`
     - unset status bits of a node


Input values
------------

Input should be provided in json format (other available input options are obsolete, incomplete and depreciated).
The input for a single transaction should be in a single line (this can be overwritten by startup settings).
Multiple input lines will be interpreted as independent method calls.
The main input parameter (``run``) is the definition of the requested transaction method.

Example:

.. code-block::

    "run" : "get_me"

Binary input data must be provided in hexadecimal format without leading '0x' and with even number of characters (hexadecimal digits).

Example:

.. code-block::

    "public_key" : "2D1FC97FA56B785E0FDAE5752DE613BAD7FBBB5EBBB46DAEE5DBFA822F976B63"

Integer values (for example amount of coins) must be provided in decimal format.
Time values must be provided in seconds since the beginning of current epoch.
Special formats are used for account addresses, transaction ID, message and block ids.

Example:

* ``address``: "00FF-0AB01234-XXXX" (16 hexadecimal characters separate with 2 '-', 'XXXX' is allowed as last part of string).
* ``txid``: "00FF:000000AB:000C" (16 hexadecimal characters separated by 2 ':').
* ``message_id``: "000F:000000AB" (12 hexadecimal characters separated by ':').
* ``block_id``: "5B695BA0" (8 hexadecimal characters).


Return values
-------------

In case of success ``ads`` returns json formatted objects.
In case of error json response has an ``error`` field.

Before submission of the transaction to the node some transaction input values are returned:

* ``tx.data`` complete transaction byte stream (data) as hexadecimal string.
* ``tx.account_hashin`` last account transaction hash used in this transaction as input for signing.
* ``tx.account_hashout`` new account transaction hash after signing the new transaction.
* ``tx.deduct`` calculated cost of the transaction (deduction from balance).
* ``tx.fee`` calculated fee of the transaction (part of ``tx.deduct``).
* ``tx.account_msid`` current transaction number of the account.
* ``tx.account_public_key`` current public key of the account.

Some of the above parameters are returned only for specific methods or in specific cases
(for example the public key is returned only if there was never a transaction submitted from this account).
Further processing of the transaction stops if the ``--dry-run`` switch is set and the transaction is not submitted to the node.

If the transaction was submitted to the node and is scheduled for broadcast on the network, the node returns a transaction identifier:

* ``tx.id`` in format ``NNNN:MMMMMMMM:PPPP`` (NNNN: node id, MMMMMMMM: node message number, PPPP: position).
* ``tx.node_msid`` node message number [integer].
* ``tx.node_mpos`` transaction position in message [integer].

If the transaction was successful the node returns the updated local :ref:`user account object <user-account-object>`.
If the transaction requested info about the account the local and the global :ref:`user account object <user-account-object>` is returned.

Currently node id and account id are often returned as integer, while fixed length hexadecimal format is used as input. This will be changed in the future to have consistent fixed length hexadecimal representation also in the output.

.. _user-account-object:

User account object
^^^^^^^^^^^^^^^^^^^

The local account object is the state of the account as seen by the node after committing last transaction.
The global account object is the state of the account as seen by the network, possible before submission of the transaction.
Both objects are handled independently and can differ if the node processed a transaction
but the message containing the transaction was not yet created, submitted or processed.
Both objects can also differ if there is a transaction from the network (deposit) that was not yet processed and committed in the local database.

Local account object includes following fields:

* ``account.address`` account id in the standard format "NNNN-UUUUUUUU-XXXX".
* ``account.node`` node id as integer.
* ``account.id`` user id of the account (number of account in node).
* ``account.msid`` last transaction number (number of submitted transactions + 1).
* ``account.time`` time of last transaction in second since epoch (integer).
* ``account.date`` time as date string.
* ``account.status`` 16 status bits as integer.
* ``account.paired_node`` node of a linked account (account with same public key) as integer
* ``account.paired_id`` user id of the linked account.
* ``account.paired_address`` address of the cousin account, displayed only if there is a linked account. A linked account info is recorded in this account if a new account was created as result of a request from this account or if an account from a different node requested fund retrieval from this account.
* ``account.local_change`` block time of an outgoing transaction request.
* ``account.remote_change`` block time of an incoming transaction from a remote host.
* ``account.balance`` account balance.
* ``account.public_key`` public key of the account.
* ``account.hash`` account hash after last outgoing transaction (private block-chain).

Global account objects returns the same parameters in the ``network_account`` container.
In addition a checksum verification result (``checksum``) is returned, which can be ignored.


.. _ads-api-fees:

Fees
----

Fees are expressed in ``clicks``.

``1 click`` = ``1e-11 ADS`` = ``0.00000000001 ADS`` (the main ADS network token)

Most transaction have a fixed fee. The minimum transaction fee is :ref:`TXS_MIN_FEE <def-txs-min-fee>`.
Broadcast transactions have a variable fee part proportional to the length of the broadcasted data string.
Wire transfer transactions have a variable fee proportional to the transferred amount.

.. list-table::
   :header-rows: 1

   * - name
     - amount
     - description
   * - .. _def-txs-min-fee:

       ``TXS_MIN_FEE``
     - 10,000
     - minimum fee per transaction
   * - .. _def-txs-div-fee:

       ``TXS_DIV_FEE``
     - (600,000,000/year = 0.006 ADS/year)
     - staking fee collected every staking block
   * - .. _def-txs-key-fee:

       ``TXS_KEY_FEE``
     - 10,000,000
     - change account key fee
   * - .. _def-txs-bro-fee:

       ``TXS_BRO_FEE(x)``
     - ``TXS_MIN_FEE`` if length<=32 bytes, 1000 for each next byte
     - broadcast message fee, x is message length in bytes
   * - .. _def-txs-put-fee:

       ``TXS_PUT_FEE(x)``
     - x * 0.05%
     - local wires fee (weight), x is transferred amount
   * - .. _def-txs-lng-fee:

       ``TXS_LNG_FEE(x)``
     - x * 0.05%
     - additional remote wires fee (weight), x is transferred amount
   * - .. _def-txs-mpt-fee:

       ``TXS_MPT_FEE(x)``
     - x * 0.05%
     - local multiple wires fee (weight), x is transferred amount
   * - .. _def-txs-get-fee:

       ``TXS_GET_FEE``
     - 1,000,000
     - retrieve funds from remote/dead bank request fee (each retrieve_funds function call)
   * - .. _def-txs-gok-fee:

       ``TXS_GOK_FEE(x)``
     - x * 0.1%
     - retrieve funds from remote/dead bank fee, x is retrieved amount, also TXS_LNG_FEE is charged by receiving node
   * - .. _def-txs-usr-fee:

       ``TXS_USR_FEE``
     - 100,000,000
     - create user fee
   * - .. _def-txs-rus-fee:

       ``TXS_RUS_FEE``
     - 100,000,000
     - additional create user fee for remote applications
   * - .. _def-txs-sus-fee:

       ``TXS_SUS_FEE``
     - 10,000,000
     - set user status bits fee
   * - .. _def-txs-sbs-fee:

       ``TXS_SBS_FEE``
     - 10,000,000
     - set bank status bits fee
   * - .. _def-txs-uus-fee:

       ``TXS_UUS_FEE``
     - 10,000,000
     - unset user status bits fee
   * - .. _def-txs-ubs-fee:

       ``TXS_UBS_FEE``
     - 10,000,000
     - unset bank status bits fee
   * - .. _def-txs-sav-fee:

       ``TXS_SAV_FEE``
     - 10,000,000
     - record account status in chain fee
   * - .. _def-txs-bnk-fee:

       ``TXS_BNK_FEE``
     - 100,000,000,000,000 (=1000 ADS)
     - create new bank fee
   * - .. _def-txs-bky-fee:

       ``TXS_BKY_FEE``
     - 10,000,000,000 (=0.1 ADS)
     - change bank key fee
   * - .. _def-bank-user-fee:

       ``BANK_USER_FEE(x)``
     - (60,000,000/year = 0.0006 ADS/year) * x
     - bank user fee, charged every block, x is a number of users created in a bank
   * - .. _def-message-fee:

       ``MESSAGE_FEE(x)``
     - x + 4,096
     - fee for each bank message sent to network, payed by bank operator, x is message length in bytes


Methods reference
-----------------

Comment on examples
^^^^^^^^^^^^^^^^^^^^

Many examples below start with the :ref:`get_me <get_me>` method call.
This call is needed for ``ads`` to load the latest account data (the account msid and hash) to correctly sign the next transaction.
This call is not needed if the account msid and hash is provided as command line option or is set in the settings.cfg file.

.. _broadcast:

broadcast
^^^^^^^^^

Broadcast a message on the network.

**Parameters**


* ``message`` hexadecimal string (without leading '0x', with even number of character). Maximum size of message is 32000 bytes. It means that maximum length of message string is 64000, because every byte is encoded as two characters.
* ``message_ascii`` ASCII string. Maximum size of message is 32000 bytes. It means that at maximum 32000 characters can be sent. This parameter can be used as alternative for ``message``. Using both parameters will generate an error.

**Fees**

``fee`` = `TXS_BRO_FEE(message_size) <#def-txs-bro-fee>`_

Fee depends on the length of the broadcasted string (message size in bytes).

**Returns**

On success returns the updated local :ref:`user account object <user-account-object>`.

**Errors**


* time of the transaction (set by the ``ads`` program) must not be bigger than node's current clock time + 1 second
* parameter ``message`` and ``message_ascii`` cannot be used together in one request

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"broadcast","message":"D69BCCF69C2D0F6CED025A05FA7F3BA687D1603AC1C8D9752209AC2BBF2C4D17"}') | ads

.. _change_account_key:

change_account_key
^^^^^^^^^^^^^^^^^^

Change public key of my account.
The transaction takes as argument the signature of an empty string signed with the new private key.
The signature is used only as the checksum of the new private key.
The signature is only verified by ``ads``.
The signature is not verified by ``adsd``.

**Parameters**


* ``public_key`` new public key as hexadecimal string
* ``confirm`` signature (as hexadecimal string) of an empty string signed with the new private key

**Fees**

``fee`` = `TXS_KEY_FEE <#def-txs-key-fee>`_

**Returns**

On success returns JSON response with field ``result`` equal ``PKEY changed``.

**Errors**


* in case of signature error ``ads`` returns "ERROR, bad new KEY empty string signature".

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"change_account_key","public_key":"2D1FC97FA56B785E0FDAE5752DE613BAD7FBBB5EBBB46DAEE5DBFA822F976B63","confirm":"D050CCFC88086A13BC6633BF8267523E2E51607EE01D60AF40A3A1AA12E6F078B6AD9231335D774AE37E7CCF48401B7D9D7D1D68FB3BBB22508685BB31368905"}') | ads


.. _change_node_key:

change_node_key
^^^^^^^^^^^^^^^

Change public key of the node I manage.
After broadcast of this transaction to the network the node will look for a new matching private key in the key file of the node (``key/key.txt``).
If the key is found, the node will continue signing future messages with the new key. If the key is not found the transaction is rejected.
Node key changes are expensive and complicated procedures that modify core parameters of the network. It is advised to do this rarely.
If the ``node`` parameter is provided, the transactions attempts to set a new key for a remote double-spend node.
Only the master VIP node has the right to do this and only keys of double-spend nodes can be changed remotely.

**Parameters**


* ``public_key`` new public key
* ``node`` node id [optional]

**Fees**

``fee`` = `TXS_BKY_FEE <#def-txs-bky-fee>`_

**Returns**

On success returns the updated local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"change_node_key","public_key":"2D1FC97FA56B785E0FDAE5752DE613BAD7FBBB5EBBB46DAEE5DBFA822F976B63"}') | ads
   (echo '{"run":"get_me"}'; echo '{"run":"change_node_key","public_key":"2D1FC97FA56B785E0FDAE5752DE613BAD7FBBB5EBBB46DAEE5DBFA822F976B63","node":"16"}') | ads


.. _create_account:

create_account
^^^^^^^^^^^^^^

Create new user account.
If no ``node`` parameter is provided or ``node`` is 0 the node will assume I request a new local account managed by the same node.
If the ``node`` parameter is not 0 and not equal to the local node id, the node will assume that I request the creation of an account by a remote node (remote account).
Local account creation requests are cheaper and are processed immediately by the node (accepted or rejected).
In case of success the node will modify the local account and modify the paired account id.
Remote account creation requests are expensive and the success of the process depends on the response of the remote node.
The result of the process will be stored in my log kept by my node.
The logs need to be examined to extract the new account id created by the remote node.
In both cases (local and remote) the new account will have the same public key as the original account.
By default created account has the same key as user who requested operation. It can be changed with passing new public key and signature of empty string.

**Parameters**


* ``node`` node id in decimal format [optional]
* to set account key [optional] two parameters are needed:

  * ``public_key`` public key of account
  * ``confirm`` empty string signed with secret key

**Fees**

For local accounts:

``fee`` = `TXS_USR_FEE <#def-txs-usr-fee>`_

For remote accounts the fee is larger:

``fee`` = `TXS_USR_FEE <#def-txs-usr-fee>`_ + `TXS_RUS_FEE <#def-txs-rus-fee>`_

In addition to the fees the "minimum account creation balance" (``USER_MIN_MASS`` = 0.00020000000 ADS) is deducted from the sending account and credited to the new account.
In case of failure the balance is returned to the sending account.
In case of remote account creation requests the network will return the "minimum account creation balance" to the sending account if the remote node fails to accept the request within the same block period.

**Returns**

On success returns the updated local :ref:`user account object <user-account-object>`.
For local account creation the updated local :ref:`user account object <user-account-object>` contains the paired account id, that can be used to obtain the id of the newly created account.
For remote account creation future logs must be examined to check for the id of the created account.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"create_account"}') | ads
   (echo '{"run":"get_me"}'; echo '{"run":"create_account","node":"16"}') | ads
   (echo '{"run":"get_me"}'; echo '{"run":"create_account","public_key":"D69BCCF69C2D0F6CED025A05FA7F3BA687D1603AC1C8D9752209AC2BBF2C4D17", "confirm":"7A1CA8AF3246222C2E06D2ADE525A693FD81A2683B8A8788C32B7763DF6037A5DF3105B92FEF398AF1CDE0B92F18FE68DEF301E4BF7DB0ABC0AEA6BE24969006"}') | ads


.. _create_node:

create_node
^^^^^^^^^^^

Create new node.
Node creation is a process that requires synchronized effort of the network.
The process can fail if range of available ids is exhausted and there are no available zombie nodes.
The new node id will be recorded in the logs of the sending account after the completion of the block.

**Parameters**

none

**Fees**

``fee`` = `TXS_BNK_FEE`` <#def-txs-bnk-fee>`_

In addition to the fees the "minimum bank account creation balance" (``BANK_MIN_UMASS`` = 1 ADS) is deducted from the sending account and credited to the new account. In case of failure the balance is returned to the sending account.

**Returns**

On success returns the updated local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"create_node"}') | ads


.. _decode_raw:

decode_raw
^^^^^^^^^^

Decodes transaction encoded as hexadecimal string.

All transactions are binary encoded before sending to network. This encoded string in hexadecimal format is returned to user in reponse field ``tx.data``.
Function ``decode_raw`` allows user to decode transaction back if needed.

**Parameters**


* ``data`` transaction encoded as hexadecimal string. Length of string depends on transaction type,
* ``signature`` signature of the transaction [optional].

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

On success returns decoded transaction in JSON format.

**Errors**

No errors specific to this method are returned.

**Example**

.. code-block::

   {"run":"decode_raw","data":"040100000000000D0000008F56605B01000100000000A0724E180900000000000000000000000000000000000000000000000000000000000000000000","signature":"59707836D82E184546D243F3F61D8DFA12F9A7DF45EC61CE04B33C15788660A08DE32D697A6AC06635D719EA393DCA10896A1F0BC96C4C63DA193D298A61E50A"}

.. _get_account:

get_account
^^^^^^^^^^^

Get account data by address.

**Parameters**


* ``address`` account address in the standard format "NNNN-UUUUUUUU-XXXX" [optional]:

  * "NNNN" indicates the node id (4 hexadecimal characters).
  * "UUUUUUUU" is the id of the user account (8 hexadecimal characters).
  * "XXXX" is the account address checksum (4 hexadecimal characters). If the checksum is not known the string "XXXX" can be used.

If account address is not provided, data for current account is returned.

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

On success returns the local and the global :ref:`user account object <user-account-object>`.
The local version of the object represents the status of the object after committing all transactions submitted to the node.
The global version of the object represents the status of the object after processing messages available on the network.
Both objects may differ if local transactions submitted from the account are not yet processed by the network or if there are transactions generated by the network (for example remote account creation or staking reward payments) that have not yet been fully processed by the local node (local office).

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   echo '{"run":"get_account","address":"000F-0000000F-XXXX"}' | ads


.. _get_blocks:

get_blocks
^^^^^^^^^^

Download, process and store a range of block headers in local archive.
While downloading, the blocks signatures are validated.
Changes in the VIP public keys are also validated and recorded.
Block headers are stored in 'blk/'. VIP keys are stored in 'vip/'.
Local block header ('blk/') repository contains only hashes of blocks validated by confirming the correctness of the signing signature sequence.
The repository will grow approximately only by 32 bytes with every new block and, due to its small size, should fit on a mobile device.

**Parameters**


* ``from`` first block time in seconds since epoch as hexadecimal string [optional].
  If parameter is missing ``ads`` will request the download starting after the last locally stored block header.
  If local block header repository is empty 0 will be passed to the node and the node will set this parameter to the time of the first block it knows.
* ``to`` block time of the last block to download, in seconds since epoch as hexadecimal string [optional].
  If parameter is missing the node will send all blocks from the starting block until the last known block on the network.
  In a single request the node will only return a range of blocks for which the set of VIP keys did not change.
  A second request (transaction call) is needed to download the subsequent range of blocks.

In the most common use case no parameters are provided.

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

Nothing is returned except errors and debug messages.
Local block and VIP keys repository is updated.

**Errors**

Most common error message is ``No new blocks to download``. It means that all blocks were updated.
It is advised to call ``get_block`` function until this error occurs.

``ads`` will report many communication and validation errors specific for the method.

Communication errors include:

* ``ERROR, failed to read VIP keys for first hash``
* ``ERROR, failed to read blocks since ...``
* ``ERROR, failed to check ... VIP keys for hash ...``
* ``ERROR, failed to confirm first header hash, fatal``
* ``ERROR, failed to get correct block ..., fatal``
* ``ERROR, failed to get signatures for header ...``
* ``ERROR, failed to check VIP keys for hash ...``

Validation errors include:

* ``ERROR opening vip/....vip, fatal``
* ``ERROR failed to match viphash for header ..., fatal``
* ``ERROR failed to match oldhash for header ..., fatal``
* ``ERROR failed to confirm nowhash for header ..., fatal``
* ``ERROR vipkey (...) not found ...`` [not fatal]
* ``ERROR vipkey (...) failed ...`` [not fatal]

In case of error local block archive (block headers) will not be updated.

**Example**

.. code-block::

   echo '{"run":"get_blocks"}' | ads


.. _get_broadcast:

get_broadcast
^^^^^^^^^^^^^

Display broadcast messages log from a block.
If no block time is provided the last completed block is assumed.
The node does not guaranty the completeness, consistency nor order of broadcast messages stored in the log.
It is expected that different nodes have different order of broadcast messages in log files.
It is possible that broadcast messages are duplicated or copies of them are in different log files on different nodes.
The node guaranties that at least one copy of the broadcast message is in the log file of the block in which the broadcast message is included.
Logs from older blocks are expected to remain unchanged on a node, unless the node will resync these blocks again.

``ads`` keeps a local archive of broadcast message log files in the 'bro/' directory. ``ads`` will automatically request missing log files from the node.
If the downloaded log file is from an uncompleted block the log file will not be saved in local archive.

**Parameters**

* ``from`` block time in seconds since epoch as hexadecimal string [optional].
  If block time is not provided (is equal zero) the node will return the log file from the last committed block.
  It is expected that this log file will not change in the future on this node, unless the node will resync the block again.

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

The method returns info about the log file:


* ``log_file`` archive|new|pending

  * archive: reporting previously reported broadcast log
  * new: reporting new broadcast log
  * pending: reported broadcast log is not final

* ``block_time`` time of the block in seconds since epoch
* ``block_time_hex`` time of the block in seconds since epoch in hexadecimal format, compatible with filename format in 'bro/' archive directory

The method returns info about the broadcast transactions in the log file. The transactions are stored in the json ``blocktree`` array and contain:

* ``block_time`` block time of the transaction in seconds (integer)
* ``block_date`` block time of the transaction as date string
* ``node`` node of the sender (integer)
* ``account`` account id of the sender (integer)
* ``address`` account address of the sender (address format)
* ``account_msid`` message number of the sender (integer)
* ``time`` time of the transaction in seconds (integer)
* ``date`` time of the transaction ad date string
* ``message`` broadcasted message in hexadecimal format
* ``data`` transaction data string in hexadecimal format
* ``signature`` transaction signature in hexadecimal format
* ``input_hash`` transaction input hash used when signing in hexadecimal format
* ``public_key`` public key of the sender when signing in hexadecimal format
* ``verify`` failed|passed , result of the verification of the signature
* ``node_msid`` node message number of the message
* ``node_mpos`` position of the broadcast transaction in message
* ``id`` id of the transaction (transaction id format)

If the supplied block time is in an unknown, future block the node will return an empty broadcast log file.

**Errors**

* ``Broadcast not ready, try again later`` Broadcast messages are not ready. Need to wait and retry,
* ``No broadcast file to send`` Block has not messages. Need to check next block.

**Example**

.. code-block::

   echo '{"run":"get_broadcast", "from":"5B9BC820")' | ads


.. _get_log:

get_log
^^^^^^^

Download and store transaction log. The log includes incoming and outgoing transactions.
With every ``get_log`` method call ``ads`` will read the local log archive of the user to load the time of the latest downloaded log entry.
``ads`` will then request from the node log entries not earlier than the time loaded from the archive.
Downloaded entries will be checked for duplicates and appended to the local archive.
After download and store the method will print all entries starting from the time provided in the ``from`` parameter.

Using default settings the node will purge its the log file of the user frequently keeping at least a 4kB block of latest logs.
However log entries that are younger than 0x800 blocks (MAX_LOG_AGE) will not be deleted.

**Parameters**


* ``address`` address of an account which log will be read [optional]. Account must be in the same node as an account issuing the request
* ``from`` earliest time of the log entry in seconds since epoch as decimal number [optional].
  If time is not provided (is equal zero) the full log will be returned
* ``type`` return only transaction of specified type eg. ``send_one``, ``create_account`` [optional].
  If type is not provided all transaction types will be returned
* ``full`` allows to access log of deleted accounts. For 1 full log is returned, for 0 (default) only current user log is returned. This parameter is useful when one account was deleted and another user has received it. By default user can only see events from time of his account creation. When full option is set to 1, user can see events before his account creation, if there were any.

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

The transaction log will be returned in the json array ``log``.
Each transaction can have following fields:


* ``time`` time, the log entry was created by the server, in seconds since epoch
* ``date`` time as date string
* ``type_no`` transaction type (method) as integer including status bits. Currently 2 bits are OR'ed to transaction number:

  * 0x4000 indicating log error (restart of the node with forced resync of older blocks),
  * 0x8000 indicating transaction originating from the network

* ``confirmed`` placeholder, always equal 1, depreciated
* ``type`` transaction type (method) as string (without status bits)

Depending on the type of transaction entry different additional parameters are provided.
The list below is grouped by types.

The following transactions are incoming transactions initiated by the network:

``node_started`` with error 0x4000:


* ``account.error`` always equal 'logerror'
* ``account.newtime`` server starting new sync from this time in the past (in seconds)
* ``account.newdate`` server starting new sync from this time in the past (as date string)
* ``account.badtime`` server failed at this time (in seconds)
* ``account.baddate`` server failed at this time (as date string)
* ``account.badblock`` server failed after this block time (in seconds)

``node_started`` without error:


* ``node_start_msid`` node message number when node started
* ``node_start_block`` block time when node started (in seconds)
* ``dividend`` added staking reward
  Info about my account is returned at node start
* ``account.balance`` balance
* ``account.local_change`` time of last local (outgoing) transaction
* ``account.remote_change`` time of last remote transaction
* ``account.hash_prefix_8`` first 8 bytes of account message hash
* ``account.public_key_prefix_6`` first 6 bytes of public key
* ``account.status`` status bits as integer
* ``account.msid`` last local (outgoing) transaction number
* ``account.node`` node of the account as integer
* ``account.id`` user id of the account
* ``account.address`` address of the account

``dividend`` record:


* ``node_msid`` node message number
* ``node_block`` staking block time (in seconds)
* ``dividend`` added staking

``bank_profit`` from a message


* ``profit`` profit for the node
* ``node`` node sending the message
* ``node_msid`` node message number
* ``profit_fee`` fees on local transactions (if my node's message)
* ``profit_div`` fees on account maintenance (if my node's message)

``bank_profit`` from network transactions and maintenance at block end


* ``profit`` profit for the node
* ``node_block`` block time of accounting (in seconds)
* ``profit_div`` fees on account maintenance
* ``profit_usr`` fees on remote user account creation
* ``profit_get`` fees on retrieve_funds transactions
* ``fee`` bank fee on number of accounts

``account_created`` remote account creation request response


* ``node`` node creating the account
* ``node_block`` block time (in seconds)
  if successful
* ``account`` user id of the new account
* ``address`` of the new account
* ``request`` failed|accepted|late

  * failed: node did not create the account
  * accepted: node created the account
  * late: node created the account in the next block after account creation request transaction

* ``amount`` amount returned on failure (0 or (``USER_MIN_MASS``))
* ``public_key`` public key of the new account (hexadecimal)

``create_node`` create node request response


* ``node_block`` block time (in seconds)
* ``node`` id of the created node
* ``request`` accepted|failed

  * accepted: node created
  * failed: node creation failed

* ``amount`` amount returned on failure (0 or (``BANK_MIN_TMASS``))

The remaining transactions were initiated by users.
The list of returned fields includes those listed below.
For some transaction some fields are not available.


* ``node`` node id of the sender or receiver (as integer)
* ``account`` user id of the sender or receiver
* ``address`` account address of the sender or receiver
* ``node_block`` block time of the transaction
* ``node_msid`` node message number of the transaction
* ``account_msid`` transaction id of the sender
* ``amount`` amount transferred
* ``sender_fee`` fee paid
* ``message`` message info as 32 byte hexadecimal string
* ``sender_balance`` account balance of the sender
* ``sender_amount`` total cost of the transaction
* ``sender_fee`` fee of the transaction
* ``sender_fee_total`` total fee of complete MPT transaction
* ``sender_public_key_prefix_5`` first 5 bytes of sender public key
* ``sender_public_key_prefix_6`` first 6 bytes of sender public key
* ``sender_status`` status bits of the sending account
* ``inout`` in|out

  * in: incoming transaction
  * out: outgoing transaction

* ``id`` id of the transaction

**Errors**


* ``ERROR reading log length`` failed to communicate with the node, fatal.
* ``ERROR reading log`` failed to read the log after reading log length, fatal.
* ``No new log entries`` is reported if no log entries with time not earlier than provided were downloaded from the node

**Example**

.. code-block::

   echo '{"run":"get_log","from":1491210824}' | ads


.. _get_me:

get_me
^^^^^^

Returns the same as :ref:`get_account <get_account>` with no account address.
Returns info about my account.

.. _get_transaction:

get_transaction
^^^^^^^^^^^^^^^

Get info about a single transaction.
The transaction info is loaded from local archive or downloaded from the node if missing.
The transaction is verified by validating the hash path and comparing the result with the block hash stored in local archive.
If the block hash is missing from the archive the transaction can not be validated and an error is returned.
Update local block hash archive to resolve this problem (:ref:`get_blocks <get_blocks>`);
Only validated transactions are stored in local archive.

**Parameters**


* ``txid`` in format 'NNNN:MMMMMMMM:PPPP' (NNNN: node id, MMMMMMMM: node message number, PPPP: position)

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

A transaction object is returned.


* ``network_tx.id`` transaction id in format 'NNNN:MMMMMMMM:PPPP'
* ``network_tx.block_id`` block id
* ``network_tx.node_id`` node id
* ``network_tx.node_msid`` node message number
* ``network_tx.position`` position in message
* ``network_tx.len`` length of the transaction data
* ``network_tx.hash_path_len`` number of hashes in hash path (path to block hash)
* ``network_tx.hextstring`` transaction data as hexadecimal string
* ``network_tx.hashpath`` hash path to block hash
* ``network_tx.type`` transaction type (method)
* ``network_tx.abank`` sender node id
* ``network_tx.auser`` sender user id
* ``network_tx.amsid`` sender transaction number
* ``network_tx.ttime`` time of the transaction
* ``network_tx.bbank`` target node id
* ``network_tx.buser`` target user id
* ``network_tx.amount`` amount
* ``network_tx.message`` transaction memo (32 byte message)
* ``network_tx.signature`` transaction signature

For some transaction type the meaning of the reported fields (abank, auser, amsid, ttime, bbank, buser, amount, message) can differ.

**Errors**


* ``ERROR, failed to read transaction path for txid ...`` communication error, fatal.
* ``ERROR, got empty block for txid ...`` missing transaction data, fatal.
* ``ERROR, got wrong transaction ...`` wrong transaction data, fatal.
* ``ERROR, failed to load hash for block ...`` missing block info in local archive. The requested transaction can not be verified because it is included in a block that is not stored in local block archive. Local archive should be updated to fix this problem. See: :ref:`get_blocks <get_blocks>`.
* ``ERROR, failed to confirm first hash for txid ...`` wrong transaction data, incorrect (first) hash, fatal.
* ``ERROR, failed to confirm nowhash for txid ...`` wrong transaction data, incorrect hash tree, fatal.
* ``ERROR opening txs/...`` error opening transaction archive file. Transaction will not be archived.

**Example**

.. code-block::

   echo '{"run":"get_transaction","txid":"0001:00000002:0001"}' | ads


.. _get_vipkyes:

get_vipkyes
^^^^^^^^^^^

Get list of public keys of VIP nodes.
These sets are usually downloaded during block download (:ref:`get_blocks <get_blocks>`).
Running this method will overwrite the data for the provided hash if it exists in the archive.

**Parameters**


* ``viphash`` 32 bytes long hexadecimal string representing the hash of the VIP keys set.

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**


* ``viphash`` requested hash of VIP keys set
* ``vipkeys`` keys of VIP servers, first key is the key of the master VIP server

**Errors**


* ``ERROR, failed to read VIP keys for hash ...`` set not found by node, fatal
* ``ERROR, failed to check VIP keys for hash ...`` incorrect data received, fatal
* ``ERROR opening vip/..., fatal`` failed to store vip set in archive, fatal

**Example**

.. code-block::

   echo '{"run":"get_vipkeys","viphash":"D3FD529F6305F574BA22F3BDF761B4778094CB38958300ACDF21D35BE03BDC4F"}' | ads


.. _get_signatures:

get_signatures
^^^^^^^^^^^^^^

Get list of signatures of a block.

**Parameters**


* ``block`` block time as hexadecimal string [optional].
  If not provided previous block time will be used (last closed block)

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**

The function returns array of signatures.


* ``signatures.node`` node id confirming the block
* ``signatures.signature`` signature of the node
* ``fork_signatures.node`` node id confirming a different block
* ``fork_signatures.signature`` signature of the node

**Errors**


* ``ERROR, bad block number ...`` node returned different block than requested

**Example**

.. code-block::

   echo '{"run":"get_signatures","block":"5B2B5B00"}' | ads


.. _get_block:

get_block
^^^^^^^^^

Get the block header and the list of nodes.

**Parameters**


* ``block`` block time as hexadecimal string [optional].
  If not provided previous block time will be used (last closed block)

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**


* ``block.id`` block time as hex
* ``block.time`` block time as decimal
* ``block.message_count`` number of messages
* ``block.oldhash`` old block hash
* ``block.minhash`` input block hash
* ``block.msghash`` hash of messages
* ``block.nodhash`` hash of nodes
* ``block.viphash`` hash of vip public keys
* ``block.nowhash`` block hash
* ``block.vote_yes`` confirming signatures
* ``block.vote_no`` forking signatures
* ``block.vote_total`` total number of signatures
* ``block.node_count`` number of nodes (includes technical node ``0000``)
* ``block.dividend_balance`` staking
* ``block.dividend_pay`` is true if this is the first block in the liquid staking period

Array of nodes is returned as well.


* ``block.nodes.id`` node id
* ``block.nodes.public_key`` public key of the node
* ``block.nodes.hash`` hash of accounts
* ``block.nodes.message_hash`` hash of last message
* ``block.nodes.msid`` number of last message
* ``block.nodes.mtim`` time of last message
* ``block.nodes.balance`` sum of account balances
* ``block.nodes.status`` status
* ``block.nodes.account_count`` number of accounts
* ``block.nodes.port`` port number for blockchain messaging
* ``block.nodes.ipv4`` ip of the node

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   echo '{"run":"get_block","block":"5B2B5B00"}' | ads


.. _get_accounts:

get_accounts
^^^^^^^^^^^^

Print accounts of a node.
Currently, the node will refuse to send accounts from a different block than the (default) previous one.
In the future only accounts from blocks used for staking calculations will be returned.
In the future the hash of the accounts should be returned as well.

**Parameters**


* ``node`` id of the node
* ``block`` block time as hexadecimal string [optional].
  If not provided previous block time will be used (last closed block)

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**


* ``accounts.`` list of accounts in the same format as reported by :ref:`get_account <get_account>`

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   echo '{"run":"get_accounts","block":"5B2B5B00","node":1}' | ads


.. _get_message_list:

get_message_list
^^^^^^^^^^^^^^^^

Get list of messages in a block.

**Parameters**


* ``block`` block time as hexadecimal string [optional].
  If not provided previous block time will be used (last closed block)

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**


* ``msghash`` hash of messages in the block
* ``messages`` list of message ids in the block in format ``NNNN:MMMMMMMM`` ``node:msid``
* ``msghash_calculated`` hash calculated by ``ads`` returned if different from ``msghash``
* ``confirmed`` confirmation of the correct hash calculation (yes|no)

**Errors**


* ``error_bad_length`` node returned data in wrong format

**Example**

.. code-block::

   echo '{"run":"get_message_list","block":"5B2B5B00"}' | ads


.. _get_message:

get_message
^^^^^^^^^^^

Print message.

**Parameters**


* ``message_id`` message id as returned by ``get_message_list``
* ``block`` block time as hexadecimal string [optional].
  If not provided previous block time will be automatically calculated

**Fees**

This transaction is not sent to the network, so there is no network fee.

**Returns**


* ``block_id`` block in which message was included
* ``message_id`` message id assigned by network
* ``node`` id of the node
* ``node_msid`` message number assigned by node
* ``time`` time of the message as integer
* ``length`` length of the message in bytes
* ``hash`` hash of the message
* ``network_txs.id`` transaction id in format 'NNNN:MMMMMMMM:PPPP'
* ``network_txs.type`` transaction type (method)
* ``network_txs.abank`` sender node id
* ``network_txs.auser`` sender user id
* ``network_txs.amsid`` sender transaction number
* ``network_txs.ttime`` time of the transaction
* ``network_txs.bbank`` target node id
* ``network_txs.buser`` target user id
* ``network_txs.amount`` amount
* ``network_txs.message`` transaction memo (32 byte message)
* ``network_txs.signature`` transaction signature
* ``network_txs.size`` size of the transaction in bytes

**Errors**


* ``error_bad_length`` node returned data in wrong format
* ``error_parse`` error parsing the message

**Example**

.. code-block::

   echo '{"run":"get_message","message_id":"0005:000017A6"}' | ads


.. _log_account:

log_account
^^^^^^^^^^^

Record account state in network.
Account data from moment of executing transaction can be read like every other transaction by ``tx.id``.

**Parameters**

This function takes no parameters.

**Fees**

``fee`` = `TXS_SAV_FEE <#def-txs-sav-fee>`_

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}';echo '{"run":"log_account"}') | ads


.. _retrieve_funds:

retrieve_funds
^^^^^^^^^^^^^^

Retrieve funds from a remote node.
The public key of the account on the remote node must match the key of my account.
This method must be called 2 times to retrieve funds.
The remote account must be silent for 2048 blocks before executing the first transaction (initiation).
Another 2048 blocks must pass after initiation to finally retrieve the funds with the second call.
All funds from the remote account will be transferred.
This method does not require the intervention of the remote node.
This method is useful in case of node failure or dispute with the node.

**Parameters**


* ``address`` account id in the standard format "NNNN-UUUUUUUU-XXXX".

**Fees**

``fee`` = 2 * `TXS_GET_FEE <#def-txs-get-fee>`_ + `TXS_GOK_FEE(funds) <#def-txs-gok-fee>`_ + `TXS_LNG_FEE(funds-TXS_GOK_FEE(funds)) <#def-txs-lng-fee>`_

Fixed part is charged for both calls (retrieve request and actual retrieve). Variable part is for second call (retrieve) and is proportional to retrieved funds.

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"retrieve_funds","address":"0002-00000001-XXXX"}') | ads


.. _send_again:

send_again
^^^^^^^^^^

Send (resend) a raw transaction.

**Parameters**


* ``data`` full transaction data as hexadecimal string.

**Fees**

The fees of the original transaction apply.
The resubmission process implies that the original transaction was not received or accepted by the network so the total fees remain unchanged.

**Returns**

Returns the results as expected from the original transaction.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"send_again","data":"05010000000000010000004A3CC9580200020000000000204E0000000000000300000000003075000000000000521B9E6932FD4973EC8364662B898249635C777BB0AA801F7DA5E9423C920EAECC39AD7B519FF6C6D27E43B9B294C0504816CE20735F11E9D8A252CF8A686806"}') | ads


.. _send_one:

send_one
^^^^^^^^

Send payment to one destination account.
Payments to account managed by a different node are more expensive.

**Parameters**


* ``address`` destination account id in the standard format "NNNN-UUUUUUUU-XXXX".
* ``amount`` in ``ADS``.
* ``message`` a 32 bytes long message in hexadecimal format [optional].

**Fees**

Fee for (local) transaction within a node is:

``fee`` = `TXS_PUT_FEE(amount) <#def-txs-put-fee>`_

Fee for (remote) transaction to a different node is:

``fee`` = `TXS_PUT_FEE(amount) <#def-txs-put-fee>`_ + `TXS_LNG_FEE(amount) <#def-txs-lng-fee>`_

Due to rounding the order of operations is important while calculating remote fee. Total fee is sum of rounded fees for local and remote node.

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"send_one","address":"0003-00000000-XXXX","amount":2.1,"message":"000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"}') | ads


.. _send_many:

send_many
^^^^^^^^^

Send payment to many destinations.
Payments to account managed by a different node are more expensive.
The transaction does not have a ``message`` field compared to ``send_one``.

**Parameters**


* ``wires`` json array with key value pairs.
  Keys are destination accounts in standard account address format and values are amounts to be wired in ``ADS``. All destination must be unique.

**Fees**

Fee for each (local) wire within a node is:

``local_fee`` = `TXS_MPT_FEE(amount) <#def-txs-mpt-fee>`_

Fee for each (remote) wire to a different node is:

``remote_fee`` = `TXS_MPT_FEE(amount) <#def-txs-mpt-fee>`_ + `TXS_LNG_FEE(amount) <#def-txs-lng-fee>`_

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

``Duplicated target`` when any destination appears in the wires array more than once.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"send_many","wires":{"0002-00000000-XXXX":20000.0,"0003-00000000-XXXX":0.003}}') | ads


.. _set_account_status:

set_account_status
^^^^^^^^^^^^^^^^^^

Set status bits of a user account.
Any user is authorized to change the second, the third and the fourth status bits of another account in the same node.
The first status bit is reserved and indicates a deleted account.
Other bits can be changed only by the owner of the destination account or the administrator of the node.
Changes of user status bits on remote nodes are not allowed.

**Parameters**


* ``address`` destination account id in the standard format "NNNN-UUUUUUUU-XXXX".
* ``status`` bits to set as unsigned integer 16 bit.

**Fees**

``fee`` = `TXS_SUS_FEE <#def-txs-sus-fee>`_

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"set_account_status","address":"0001-00000000-XXXX","status":"10"}') | ads


This transaction will set the 2nd and the 4th bit of the destination account status to 1.


.. _set_node_status:

set_node_status
^^^^^^^^^^^^^^^

Set status bits of a node.
The node status bits can be changed by the administrator of the node or by the administrator of a VIP node.
First 3 bits are reserved and can not be changed using this transaction:


* 1st bit – node is deleted
* 2nd bit – node belongs to the vip group
* 3rd bit – node has most funds in network

The administrator of a node can change bits 4-16 of the status of the managed node.
VIP node administrators can change bits 17-24 of any node.
The last 8 bits of any node can be changed only if more than 50% of the VIP node administrators send the node status change transaction in one block. The 50% minimum is required for any of the last 8 bits.

**Parameters**


* ``node`` node number as decimal number
* ``status`` bits to set as unsigned integer 32 bit.

**Fees**

``fee`` = `TXS_SBS_FEE <#def-txs-sbs-fee>`_

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"set_node_status","node":"1","status":"8"}') | ads


This transaction will set the 4th bit of the destination node status to 1.

.. _unset_account_status:

unset_account_status
^^^^^^^^^^^^^^^^^^^^

Unset status bits of a user account.
Any user is authorized to change the second, the third and the fourth status bits of another account in the same node.
The first status bit is reserved and indicates a deleted account.
Other bits can be changed only by the owner of the destination account or the administrator of the node.
Changes of user status bits on remote nodes are not allowed.

**Parameters**


* ``address`` destination account id in the standard format "NNNN-UUUUUUUU-XXXX".
* ``status`` bits to unset as unsigned integer 16 bit.

**Fees**

``fee`` = `TXS_UUS_FEE <#def-txs-uus-fee>`_

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"unset_account_status","address":"0001-00000000-XXXX","status":"10"}') | ads


This transaction will set the 2nd and the 4th bit of the destination account status to 0.


.. _unset_node_status:

unset_node_status
^^^^^^^^^^^^^^^^^

Unset status bits of a node.
The node status bits can be changed by the administrator of the node or by the administrator of a VIP node.
First 3 bits are reserved and can not be changed using this transaction:


* 1st bit – node is deleted
* 2nd bit – node belongs to the vip group
* 3rd bit – node has most funds in network

The administrator of a node can change bits 4-16 of the status of the managed node.
VIP node administrators can change bits 17-24 of any node.
The last 8 bits of any node can be changed only if more than 50% of the VIP node administrators send the node status change transaction in one block. The 50% minimum is required for any of the last 8 bits.

**Parameters**


* ``node`` node number as decimal number
* ``status`` bits to unset as unsigned integer 32 bit.

**Fees**

``fee`` = `TXS_UBS_FEE <#def-txs-ubs-fee>`_

**Returns**

On success returns the local :ref:`user account object <user-account-object>`.

**Errors**

No errors specific to this method are returned by ``ads``.

**Example**

.. code-block::

   (echo '{"run":"get_me"}'; echo '{"run":"unset_node_status","node":"1","status":"8"}') | ads


This transaction will set the 4th bit of the destination node status to 0.
