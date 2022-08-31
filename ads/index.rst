
ADS Blockchain
==========================

The ADS Blockchain is a fork of the `Enterprise Service Chain (ESC) <https://github.com/EnterpriseServiceChain/esc>`_,
a blockchain software technology capable of facilitating high volumes of simple transactions which,
similarly to other cryptocurrencies, allows sending tokens between user accounts.
ESC derives its name from the concept of the Enterprise Service Bus,
where a cryptocurrency is used as the communication protocol.

The main features of the ADS Blockchain can be summarized as follows:

-	Delegated Proof of Stake as block consensus mechanism to reduce network maintenance costs
-	Small account and transaction identifiers, reduced transaction set and parallel processing of transactions to facilitate high transaction volumes (>100kHz one-one transactions, >1MHz one-many transactions)
-	Nodes are heavily penalized for double spends so most transactions can be trusted almost instantly
-	Small set of VIP nodes responsible for network integrity to facilitate incorporation of slow nodes with reduced transaction processing capabilities
-	Hash of all accounts is part of the block and enables instant synchronization with the block chain
-	Hierarchical organization of accounts and nodes facilitates KYC, AML , eID  supply and governance
-	Dividend payments to account holders and node managers to support the growth of the economy of the ESC system

Details
----------------------

The `white paper <https://adshares.net/assets/ESC.pdf>`_ provides a more detailed description of the concept of the Enterprise Service Chain which is foundation of the ADS Blockchain.

..  toctree::
    :maxdepth: 1

    how-to-use-ads-wallet
    how-to-get-ads
    burning-and-staking
    wrapped-ads
    adshares-for-metaverse
    how-to-convert-adst-tokens
    how-to-join-the-testnet

Technical
----------------------

..  toctree::
    :maxdepth: 1

    installation
    setting-up-a-local-test-net
    log-rotation
    ads-api
    how-to-generate-ads-keys
    how-to-generate-transactions-offline
    how-to-generate-transactions-offline-with-json-rpc
    how-to-check-incoming-transactions
    how-to-validate-account-address
    how-to-start-ads-node
