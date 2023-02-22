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

