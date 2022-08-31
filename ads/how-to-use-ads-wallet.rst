
.. _how-to-use-ads-wallet:

How to use ADS Wallet
========================

What is ADS wallet
------------------

ADS Wallet is a secure identity vault for Adshares, that was designed to store keys and provide cryptographic transaction signing.
It can also be used to create or import accounts and send basic transactions.
Our wallet provides integration with internal and external services connected to Adshares network.
It is a convenient, free, open-source client-side tool.

There are two versions of the plugin - the first one works with Chrome and Opera browsers
(install via `Chrome Web Store <http://adshar.es/ADSwallet>`_),
while the other one was designed for Mozilla Firefox
(install via `Firefox Add-ons <http://adshar.es/WalletFirefox>`_).

Installing ADS Wallet web browser plugin is a recommended step to join Adshares network as an advertiser or a publisher.

Who can use ADS Wallet
----------------------

ADS Wallet can be used by three types of users:

* those who don't have an account and a key - i.e. new users
* those who already have an account and a key that is not based on a seed phrase
* those who already have a key based on a seed phrase

What is important, ADS Wallet also supports :ref:`Testnet <how-to-join-the-testnet>`,
so each user can try it prior to handling actual transactions or storing real keys.
The plugin operated in Testnet mode uses Testnet accounts.

How to configure ADS Wallet
---------------------------

Let's start with the main panel.
Depending on whether you already have a seed phrase, you can either create a new vault or recover the one you already have.
Please note that you can use ADS Wallet both in mainnet and testnet mode.

I don’t have a seed phrase
^^^^^^^^^^^^^^^^^^^^^^^^^^

In case you don’t have a seed phrase, you need to follow the procedure described below:

* Hit the start button. The plugin will ask you to enter and confirm the password. After accepting the Terms of Use,
  the plugin will assign a seed phrase. As soon as you write down the seed phrase and store it in a safe place, you are good to go.


.. image:: /_static/images/plugin1.png
   :target: /_static/images/plugin1.png
   :alt: Configuration



* Choose between setting a new free account (green button) and importing account that you already have (blue button).


.. image:: /_static/images/plugin2.png
   :target: /_static/images/plugin2.png
   :alt: Free account



* If you choose "Get free account" a set of keys will be generated based on your seed phrase.
  All keys, which are cryptographically protected by the password, are stored locally on a device and are not archived or sent anywhere.
  It's important to keep that in mind, as the seed phrase is the only way of recovering the vault.
  If you want to view your keys you need to go into Main Menu -> Settings -> and click the orange icon next to the account address.


.. image:: /_static/images/plugin3.png
   :target: /_static/images/plugin3.png
   :alt: Settings



* If you choose "Import account" you will be asked to enter the account name and account address and hit "Import" key.
  In case you want to add another account to ADS Wallet,
  you need to go into Main Menu -> Settings -> hit the "Add account" button,
  provide account name & address and authenticate the operation with your password.
  Once your account is added, you can use the plugin to sign ADS Operator transactions.

I already have a seed phrase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case you are one of the users who already have a seed phrase,
you have to begin with clicking "Restore the vault from a seed" button.
The next step requires entering your seed phrase and setting a password.
Once you are done, you have to import your account.
The procedure is the same for users who have a seed phrase as well as for the ones who don't.


.. image:: /_static/images/plugin4.png
   :target: /_static/images/plugin4.png
   :alt: Restore the vault


----

The plugin can serve up to 20 accounts.
In order to switch to a different wallet you need to click the account name on the top of the plugin
and select the one you want to use from a dropdown list.

Apart from transferring assets to other accounts, users can view their account balance in real time.


.. image:: /_static/images/plugin5.jpg
   :target: /_static/images/plugin5.jpg
   :alt: Dashboard


How to transfer assets
----------------------

In order to transfer funds you just need to hit "Send Transaction" button in the main panel,
provide the ID of the account you want to transfer your ADS to,
enter the amount and write a message in hexadecimal format (0–9; A-F; up to 64 characters)
or alternatively a regular text (up to 32 characters).

In the next step, you need to review transfer data.
At this point, you can also tick "Advanced data" to view all information that will be sent to the blockchain.
Once you accept the transaction, you'll get a transaction ID along with the fee information.
The blockchain charges 0.1% fee in case of transactions between nodes and 0.05% in case of transactions within the same node.

Once you click the transaction ID, you are transferred to the Block Explorer, where you can check your account balance.
It's visible after approx. 15 minutes, as soon as the blockchain scans it.
It is also possible to access Block Explorer from the main panel after clicking the "Details" button.

If you want to know how to transfer your funds from the Adshares platform to your ADS Wallet,
click `here <https://github.com/adshares/adserver/wiki/How-to-use-Advertising-Ecosystem#how-to-withdraw-ads-coins-from-the-platform>`_.

Importing private keys
----------------------

ADS Wallet also offers private keys import.
To import your private key, you need to access the menu from the main panel, then go into Settings.
Next, you simply hit "Manage keys" and "Import new key". It's necessary to type in your key name and private key.
The plugin can also check if the private key is correct. It's possible to verify it using your public key.
You can view your keys once you click the yellow icon.
The plugin can handle up to 20 imported private keys.


.. image:: /_static/images/plugin6.png
   :target: /_static/images/plugin6.png
   :alt: Importing private keys


**Please keep in mind that it is not possible to recover private keys that were imported manually after uninstalling the plugin, as all private keys are stored only locally. In case of accounts with such keys (e.g. genesis block accounts), we recommend changing keys to seed-phrase-based keys. For security reasons we also advise not to use the master key and to use one key with one account only.**

General remarks
---------------

ADS Wallet uses our own JSON-RPC to communicate with blockchain.
It is publicly available on our `GitHub <https://github.com/adshares/ads-browser-wallet>`_ along with the documentation.

For some users, it may be more convenient to use the plugin in a separate browser window.
In order to switch to this mode you just need to click "Expand view" in the Main Menu.

The Chrome version of our plugin supports Google Chrome synchronization,
which means it can be synchronized across many devices.

How to restore ADS Wallet from seed phrase
------------------------------------------

To restore your old ADS Wallet account, prepare two things:

#. Seed phrase
#. Account address

Having problems with finding your account address?
Try to find your account by the amount of available funds and activity.
Use this link to search accounts.
https://operator.adshares.net/blockexplorer/accounts?page=3&sort=balance&order=desc

When you prepare seed and address, follow the instruction:

* Download ADS Wallet as browser extension
* In the first view, click ‘Restore the vault from a seed’
* Enter seed phrase (in small letters, divided by spaces)
* Set new password
* Click ‘Import account’
* Set account name
* Provide account address (in format: XXXX-XXXXXXXX-XXXX)
* Click ‘import’

Success! Your account is restored now, dear ADS hodler.
