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
