
.. _adserver-conversions:

Conversions
===========

Conversion link
---------------

A crucial part of conversion is passing information that the conversion took place.
This can be achieved by making a HTTP request to the adserver.
The common way to do it is to create an image element on a site.
This image is usually a 1x1 px gif, which points to an adserver resource.
The other option is to make a direct API call.

Each conversion has a unique conversion link.

In the *basic mode*, the link has only one (optional) parameter *value*.
Such a link could be used as an src attribute of a HTML element.
It could be used only once per impression.

Here are sample links.

.. code-block::

   https://example.com/kw/6d0bd92b28aa4deb811d6f9cf8aff96b.gif
   https://example.com/kw/6d0bd92b28aa4deb811d6f9cf8aff96b.gif?value=1.2

In the *advanced mode*, the link has placeholders that should be filled.

Here’s a sample link.

.. code-block::

   https://example.com/kw/6d0bd92b28aa4deb811d6f9cf8aff96b.gif?value=value&nonce=nonce&ts=timestamp&sig=signature

Parameters:

* value - how much the conversion is worth in US Dollars. This parameter is optional if the value was defined during the conversion
* nonce - unique random value, which is used to distinguish two conversions of the same type
* ts – the timestamp of the conversion creation
* sig – the signature of passed parameters

Preparation of the conversion link in the advanced mode
-------------------------------------------------------

Helper methods
^^^^^^^^^^^^^^

The  ``urlSafeBase64Encode`` function encodes data to base64 format and replaces characters that are not allowed in the URL.

.. code-block:: php

   public static function urlSafeBase64Encode($string): string
   {
       return str_replace(
           [
               '/',
               '+',
               '=',
           ],
           [
               '_',
               '-',
               '',
           ],
           base64_encode($string)
       );
   }

The ``urlSafeBase64Decode`` function is a reverse function to the ``urlSafeBase64Encode``. It replaces non-standard base64 characters and decodes base64 string.

.. code-block:: php

   public static function urlSafeBase64Decode(string $string): string
   {
       return base64_decode(
           str_replace(
               [
                   '_',
                   '-',
               ],
               [
                   '/',
                   '+',
               ],
               $string
           )
       );
   }

Generating the conversion link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here’s a piece of code that generates the conversion link.
This link must be generated for each conversion event.

.. code-block:: php

   private const CONVERSION_LINK_TEMPLATE = 'https://example.com/kw/6d0bd92b28aa4deb811d6f9cf8aff96b.gif?value=value&nonce=nonce&ts=timestamp&sig=signature';
   private const CONVERSION_SECRET = 'gKH9a3UDEGn7F71NOWfuvw';

   /**
    * @param string $value conversion value in US Dollars. If decimal part is needed, it should be separated with a dot
    *
    * @return string conversion link
    * @throws \Exception when function random_bytes is not available
    */
   private function generateLink(string $value = ''): string
   {
       $uuidStart = strrpos(self::CONVERSION_LINK_TEMPLATE, '/') + 1;
       $uuid = substr(self::CONVERSION_LINK_TEMPLATE, $uuidStart, 32);
       $nonce = Utils::urlSafeBase64Encode(random_bytes(16));
       $timestamp = time();

       $signature = Utils::urlSafeBase64Encode(
           hash('sha256', $uuid.Utils::urlSafeBase64Decode($nonce).$timestamp.$value.self::CONVERSION_SECRET, true)
       );

       return str_replace(
           [
               $value ? '=value' : 'value=value&',
               '=nonce',
               '=timestamp',
               '=signature',
           ],
           [
               $value ? '='.$value : '',
               '='.$nonce,
               '='.$timestamp,
               '='.$signature,
           ],
           self::CONVERSION_LINK_TEMPLATE
       );
   }

The ``CONVERSION_LINK_TEMPLATE`` and ``CONVERSION_SECRET`` constants should be read from the conversion definition.
They are unique for each conversion.
The ``$value`` parameter is optional, in case it was defined in the conversion.

Direct API call
^^^^^^^^^^^^^^^

The direct API call from the advertiser’s backend to the adserver needs another parameter: ``cid``.
The ``cid`` parameter can be obtained during the first user visit on the advertiser’s site.
It is the advertiser’s responsibility to store ``cid`` and connect it with a proper user.
The ``cid`` parameter should be attached to other GET parameters of the advanced conversion link.
