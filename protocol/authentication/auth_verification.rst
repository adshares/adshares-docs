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
