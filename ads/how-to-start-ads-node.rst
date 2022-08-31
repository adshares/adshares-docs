
How to start ADS node
=====================

This manual will show how to start ADS node and change key of main (technical) account.

Node is the basic element of blockchain network.
Every node can have multiple user accounts.
At least one account is always present.
It is main (technical) account, which number is 0.
By default secret key of node and main account are the same, so it is suggested to change one of them.

Requirements
------------

Node data
^^^^^^^^^

To setup the ADS node, you will need to provide a node identifier (4 hexadecimal characters) and a secret key which consist of 64 hexadecimal characters.
Usually you will also need to specify an IP address.

If you participate in genesis, you can find your node id on `Genesis Block page <https://genesis.adshares.net/genesis>`_.
Just look for your public key on nodes list and get node id bind with this key.
On the same page you can check your account address and it's balance.
By default first account has the same key as node.

Tools
^^^^^

Install ADS binaries from official PPA.

.. code-block::

   sudo add-apt-repository ppa:adshares/releases -y
   sudo apt-get update
   sudo apt-get install ads ads-tools

Check if ``ads`` is installed.

.. code-block::

   ads --version

Above command should return working directory and ``ads`` version.

Open ports
^^^^^^^^^^

The ADS node uses two TCP ports: 6510 and 6511 (by default).
First is used to communicate with other nodes.
Second is needed for clients' connections.

Open both ports.

.. code-block::

   sudo apt-get install -y ufw
   sudo ufw allow 6510,6511/tcp

More information can be found on `Ubuntu Uncomplicated Firewall <https://help.ubuntu.com/community/UFW>`_ documentation page.

Synchronize time
^^^^^^^^^^^^^^^^

It is crucial to synchronize time between nodes.
Time difference should not exceed one second.
We advise to set synchronization with NTP servers.
For more information check official Ubuntu documentation on `Time Synchronization <https://ubuntu.com/server/docs/network-ntp>`_.

Setup the node
--------------

Configure the node.
You will be asked for node's secret key (64 hexadecimal characters), id (4 hexadecimal characters), and host IP address.

.. code-block::

   ads-service configure

Start the node.

.. code-block::

   ads-service start

Check the node status.

.. code-block::

   ads-monitor status -v

If node works, you should see current time, block time (or time to genesis block) and node number.

Change account key
------------------

After genesis block all nodes can receive transaction requests. In general, if you want to execute transaction, you should know authentication data:


* for account which will send transaction: address ``$ADDRESS`` and secret key ``$SECRET``;
* for node in which above account is: host name or IP address ``$HOST`` and port for clients connections ``$PORT`` (default is 6511);

Change of key also requires new credential data for account.
For security reasons secret key is not send.
Instead you need to provide public key ``$NEW_PUBLIC_KEY`` and signature of empty string ``$NEW_CONFIRM``.
To create this data please use ``key`` program described in :ref:`How to generate ADS keys <how-to-generate-ads-keys>` instruction.

When you collect all needed data, execute ``change_account_key`` command. Exchange all placeholders starting with "$" with real parameters.

.. code-block::

   (echo '{"run":"get_me"}';echo '{"run":"change_account_key", "public_key":"$NEW_PUBLIC_KEY", "confirm":"$NEW_CONFIRM"}') | ads --address=$ADDRESS --secret=$SECRET --host=$HOST --port=$PORT

Alternatively, you can store authentication parameters in ``settings.cfg`` for future use.
This method as well as other transactions are described on :ref:`ADS API page <ads-api>`.

Please, note that ``change_account_key`` and every other transaction sent to network is paid.
Besides, there is group of free transactions which read blockchain network status.
All fees are enlisted in :ref:`fees table <ads-api-fees>`.
