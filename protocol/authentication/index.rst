.. _protocol-authentication:

Authentication
==============

Prerequisite: set up a blockchain account
-----------------------------------------

The :ref:`ADS Blockchain <protocol-definitions-blockchain>` is the backbone of the whole ecosystem.

Thus, the first step is to set up an :ref:`ADS Account <protocol-definitions-account>` on :ref:`ADS Blockchain <protocol-definitions-blockchain>`.
This account will be used for handling incoming and outgoing :ref:`Payments <protocol-payments>`, and sending :ref:`Broadcasts <protocol-synchronization-sendbroadcast>`.

The account can be created by the node operator, but a more convenient way is to use :ref:`ADS Wallet <protocol-definitions-wallet>`.
Detailed instruction can be found on `Setup guide <https://adshares.net/wallet#wallet-installation-steps>`_ or
:ref:`How to use ADS Wallet page <how-to-use-ads-wallet>`.

After creating an account, you will receive an **account address**, a **public key** and a **secret key**.

ADS authentication
------------------

Authentication between various entities within :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>` is performed 
by sending a signed ``Authorization`` header with the :ref:`ADS Account <protocol-definitions-account>`
address. Checking the signature allows you to verify the account address and identify the sender.

.. toctree::
    :maxdepth: 1

    auth_header
    auth_signing
    auth_verification