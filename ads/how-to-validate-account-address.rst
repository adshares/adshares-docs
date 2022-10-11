
.. _how-to-validate-account-address:

How to validate account address
===============================

Address format
--------------

The standard format of an account address is ``NNNN-UUUUUUUU-XXXX``:


* ``NNNN`` indicates the node id (4 hexadecimal characters).
* ``UUUUUUUU`` is the id of the user account (8 hexadecimal characters).
* ``XXXX`` is the account address CRC-16/AUG-CCITT checksum (4 hexadecimal characters). If the checksum is not known the string "XXXX" can be used.

Examples:

* ``0001-00000000-9B6F``
* ``0001-00000000-XXXX``
* ``0015-00000002-3671``
* ``FFFF-FFFFFFFF-A6E1``

CRC calculation
---------------

JavaScript
^^^^^^^^^^

.. code-block:: js

   function calculateCrc(nodeId, accountId) {
     const d = `${nodeId}${accountId}`;
     let crc = 0x1D0F;
     for (let i = 0, len = d.length; i < len; i += 2) {
       let x = (crc >> 8) ^ parseInt(d.substr(i, 2), 16);
       x ^= x >> 4;
       crc = ((crc << 8) ^ ((x << 12)) ^ ((x << 5)) ^ (x)) & 0xFFFF;
     }
     return crc.toString(16).toUpperCase().padStart(4, '0');
   }

PHP
^^^

.. code-block:: php

   function calculateCrc(string $nodeId, string $accountId): string
   {
     $chars = hex2bin($nodeId . $accountId);
     $crc = 0x1D0F;
     for ($i = 0; $i < strlen($chars); $i++) {
       $x = ($crc >> 8) ^ ord($chars[$i]);
       $x ^= $x >> 4;
       $crc = (($crc << 8) ^ ($x << 12) ^ ($x << 5) ^ ($x)) & 0xFFFF;
     }
     return sprintf('%04X', $crc);
   }

Validation
----------

JavaScript
^^^^^^^^^^

.. code-block:: js

   function validateAddress(address) {
     const r = /^([0-9A-F]{4})-([0-9A-F]{8})-([0-9A-F]{4}|XXXX)$/;
     const m = r.exec((address || '').toUpperCase());
     if (!m) return false;
     return m[3] === 'XXXX' || m[3] === calculateCrc(m[1], m[2]);
   }

PHP
^^^

.. code-block:: PHP

   function validateAddress(string $address): bool
   {
     $r = '/^([0-9A-F]{4})-([0-9A-F]{8})-([0-9A-F]{4}|XXXX)$/';
     $m = [];
     if (!preg_match($r, strtoupper($address), $m)) {
       return false;
     }
     return $m[3] === 'XXXX' || $m[3] === calculateCrc($m[1], $m[2]);
   }
