
.. _how-to-join-the-testnet:

How to join the Testnet
=========================

The Testnet
-----------

Testnet is Adshares' testing environment.
It is a place where all applications will be deployed before the production phase.
Adshares' intention is to run production-ready code in the Testnet
and make it available to master node operators and exchanges who wish to try out Adshares’ solutions.
Everyone is invited to take part.
Testnet block explorer is available here:

https://operator.e11.click/blockexplorer

Testnet comparison with the production environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although applications in the Testnet are ready for production deployment,
this environment cannot be used for commercial purposes.
Stability (thus security) of the Testnet is lower.
Adshares does not assure continuity of services.
It is possible that the Testnet will be restarted and some data will be lost.

**We strongly advise NOT TO USE the same credentials (secret keys) in the Testnet and in the production environment.**

Test network structure
^^^^^^^^^^^^^^^^^^^^^^

Currently, there are five ADS blockchain nodes.
The next chapter describes how to join blockchain network.
Standard `ads client <https://github.com/adshares/ads>`_ can be used to connect.
It is important to use host from the Testnet.

In the table below are listed initial nodes.

.. list-table::
   :header-rows: 1

   * - Node Id
     - Host
     - Port
   * - 0001
     - t01.e11.click
     - 6511
   * - 0002
     - t02.e11.click
     - 6511
   * - 0003
     - t03.e11.click
     - 6511
   * - 0004
     - t04.e11.click
     - 6511
   * - 0005
     - t05.e11.click
     - 6511


Creating an account
-------------------

ADS Testnet account can be created automatically using :ref:`browser Wallet <how-to-use-ads-wallet>`.

After the installation you should switch to the Testnet, configure ADS Wallet and click "Get free account" button.
Now you can copy your account address.

Get free test coins
^^^^^^^^^^^^^^^^^^^

You can get coins using Twitter.
Simply, tweet a message containing `#adsTestnet <https://twitter.com/hashtag/adsTestnet>`_ hashtag and your account address.
Don’t forget to mention `@adsharesNet <https://twitter.com/adsharesNet>`_.

Below is the sample tweet.

.. code-block::

   @adsharesNet fill up my account 0003-0000000B-6E87 in #adsTestNet

You should receive a response with success info within a few minutes.
Your account will have 1024 ADS, which is sufficient to perform tests.
Three accounts per user can be created at most.
