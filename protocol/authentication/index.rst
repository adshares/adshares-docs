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

.. _protocol-authentication-header:

Authentication header
^^^^^^^^^^^^^^^^^^^^^

.. code::

    ADS account="<string>", nonce="<string>", created="<string>", signature="<string>"

* ``account`` - the ADS account address
* ``nonce`` - a cryptographically random string encoded in `Base64 <https://datatracker.ietf.org/doc/html/rfc4648.html>`_
* ``created`` - a datetime in `W3C (ISO 8601) <https://www.w3.org/TR/NOTE-datetime>`_ format
* ``signature`` - a signature of the nonce and the timestamp from ``created`` datetime signed with the the ADS private key

Example::

    Authorization: ADS account="0001-00000001-8B4E", nonce="YTVlM2NmZWVlOTBkMzI4NA==", created="2022-10-10T14:42:37+00:00", signature="fd0ae5f6978b6af35a5fff98fc7311a4d56faf5f1b3c6aa13574b631f295934c7af96696b3f7024800dc6e6e4f409dddb4bfcc9d79cf3e07603a8f18e5a62000"

.. _protocol-authentication-signing:

Header signing
^^^^^^^^^^^^^^

To sign the header you need an :ref:`ADS Account <protocol-definitions-account>` address, the appropriate secret/private key and a sodium library.

To test signatures you can use :ref:`command line tool <signing-message>`.

PHP example code:

.. code:: php

    $adsAccount = '0001-00000001-8B4E'; // change this
    $adsPrivateKey = 'DF7C4188C7F77A182FA7655D5E971863D600A770858804735AFB1B667D2D055A'; // change this

    $nonce = random_bytes(32);
    $created = new DateTimeImmutable();
    $message = $nonce . $created->format('U');
    $keyPair = sodium_crypto_sign_seed_keypair(hex2bin($adsPrivateKey));
    $secretKey = sodium_crypto_sign_secretkey($keyPair);
    $signature = bin2hex(sodium_crypto_sign_detached($message, $secretKey));

    $header = sprintf(
        'ADS account="%s", nonce="%s", created="%s", signature="%s"',
        $adsAccount,
        base64_encode($nonce),
        $created->format('c'),
        $signature
    );

.. _protocol-authentication-verification:

Header verification
^^^^^^^^^^^^^^^^^^^

To verify the signature, you need to :ref:`validate the account address <how-to-validate-account-address>`,
:ref:`get the public key from the ADS blockchain <get_account>`, and use the sodium library.

Additionally, you should verify that the ``Created`` header value is valid within five minutes and that the ``Nonce``
header value is unique within five minutes.

To test verification you can use :ref:`command line tool <verify-signature>`.

PHP example code:

.. code:: php

    use Adshares\Ads\AdsClient;

    $header = $request->headers->get('authorization'); // depends on the framework
    $adsClient = new AdsClient(...); // initialize client

    $adsRegex = '/ADS account="(?P<account>[^"]+)", nonce="(?P<nonce>[a-zA-Z0-9+\/]+={0,2})", created="(?P<created>[^"]+)", signature="(?P<signature>[^"]+)"/';
    if (1 === preg_match($adsRegex, $header, $matches)) {
        $adsAccount = $matches['account'];
        // Check if the account is valid
        $nonce = base64_decode($matches['nonce']);
        // Check if the nonce is not used before
        $created = new DateTimeImmutable($matches['created']);
        // Check if the timestamp is not obsolete
        $signature = $matches['signature'];
        $publicKey = $adsClient->getAccount($adsAccount)->getPublicKey();
        $message = $nonce . $created->format('U');

        $verified = sodium_crypto_sign_verify_detached(hex2bin($signature), $message, hex2bin($publicKey));
    }