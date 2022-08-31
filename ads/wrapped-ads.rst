
Wrapped ADS
===========

ADS exists on multiple blockchain as wrapped tokens. ADS coins wrapped on another blockchain are removed from circulation and held in reserve address.
Balance of reserve address should at all time be greater or equal to amount of tokens issued on another chain.

Active blockchain gateways
--------------------------

.. list-table::
   :header-rows: 1

   * - Blockchain
     - Ethereum
     - Binance Smart Chain
   * - Contract address
     - | ``0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a``
       | `Etherscan <https://etherscan.io/token/0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a>`_
     - | ``0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a``
       | `BscScan <https://bscscan.com/token/0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a>`_
   * - Swap address
     - | ``0xe405113bfd5b988bdba4a4ca9419a18f9e2828a6``
       | `Info <https://info.uniswap.org/#/pools/0xe405113bfd5b988bdba4a4ca9419a18f9e2828a6>`_
       | `Uniswap <https://app.uniswap.org/#/swap?outputCurrency=0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a>`_
     - | ``0x0bc8c5d9cfb88cbf4f1b0e623bc8b8ea76ad960c``
       | `DexTools <https://www.dextools.io/app/pancakeswap/pair-explorer/0x0bc8c5d9cfb88cbf4f1b0e623bc8b8ea76ad960c>`_
       | `Pancake Swap <https://exchange.pancakeswap.finance/#/swap?outputCurrency=0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a>`_
   * - Reserve address
     - `0001-00000002-BB2D <https://operator.adshares.net/blockexplorer/accounts/0001-00000002-BB2D>`_
     - `0001-00000003-AB0C <https://operator.adshares.net/blockexplorer/accounts/0001-00000003-AB0C>`_
   * - Wrapping prefix
     - ``000000575241505F4554483A``
     - ``000000575241505F4253433A``


How to wrap ADS coins
---------------------

You can wrap ADS for use on other blockchain by sending it to reserve address with specially cratfed message that contains destination address on another chain. You build this message by joining wrapping prefix with destination address.

Wrap ADS on Ethereum example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to wrap ``50000 ADS`` and send it to Ethereum address ``0xba146a5c71Ca27ec03c70E448c01825584e3Bd01``

Wrapping prefix for Ethereum is ``000000575241505F4554483A``. Reserve address is ``0001-00000002-BB2D``.

We need to send ``50000 ADS`` to ``0001-00000002-BB2D`` and include message ``000000575241505F4554483ABA146A5C71CA27EC03C70E448C01825584E3BD01`` (prefix + Ethereum address without leading 0x)

We issue standard ``send_one`` transaction either using ADS Wallet extension or command line.

Tx example: https://operator.adshares.net/blockexplorer/transactions/0001:0001BF4E:0001

Once tx is confirmed it will be processed by the gateway and equal amount of ADS on Ethereum will be issued (minus costs of Ethereum transaction fee). Tx mention below was processed as:

https://etherscan.io/tx/0x9621995926b4006f32af9ac0374fea37bc7f38bc33105511e1df4fc31bb84ea6

Gateway issued ``49970 ADS`` on Ethereum, 30 ADS was taken for gas fee, which was moderately high at the moment.

Wrap ADS on Binance Smart Chain example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Process is exactly the same, but we use BSC prefix and reserve address.

Wrap Tx example: https://operator.adshares.net/blockexplorer/transactions/0001:0001BF9B:0001

It was processed as:
https://bscscan.com/tx/0x42651c4d89dafca50cc0daeee7420423a567983f26e253500b9fcf6a67a659bc

Gateway issued ``49996 ADS`` on BSC, 4 ADS was taken for gas fee, which was much cheaper than on eth.

How to unwrap ADS
^^^^^^^^^^^^^^^^^

**You can use the unwrapping tool with MetaMask: https://wallet.adshares.net/**

Each token contract has ``Unwrap`` method that can be used to burn wrapped token.
``Unwrap`` method takes ADS address as argument which allows to specify where uwrapped ADS should go to.

BSC example: https://bscscan.com/tx/0xc017a831ad41b8be01095806777f3c681cf5de61bcd0349c60c4535c33067818

It was processed as:
https://operator.adshares.net/blockexplorer/transactions/0001:0001C1DA:0001
