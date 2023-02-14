
Be visible for others – send broadcast
======================================
To become a part of the network the adserver has to inform others that it is accessible.
It should be done by broadcasting an URL to adserver meta data using ADS blockchain.

.. _adserver_metadata:

Adserver's metadata
-------------------
Prepare the metadata.
The metadata should be in JSON format.
All fields are enlisted below.
They have string values unless stated otherwise.

Metadata fields:

+-------------------+-------------------------------+-------------------------------------------------------------------+
| Field             | Type                          | Description                                                       |
+===================+===============================+===================================================================+
| module            | constant "adserver"           | The ID of the module                                              |
|                   |                               |                                                                   |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| name              | string                        | The name of the adserver. It should be a unique string            |
|                   |                               | inside the entire network                                         |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| version           | string                        | The version of adserver                                           |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| capabilities      || array of constants:          | List of adserver's capabilities:                                  |
|                   || "ADV", "PUB"                 |                                                                   |
|                   |                               | - "ADV" for advertising                                           |
|                   |                               | - "PUB" for publishing                                            |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| serverUrl         | string                        | The URL of the adserver's backend                                 |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| panelUrl          | string                        | The URL of the adserver's frontend                                |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| landingUrl        | string                        | The URL of the adserver's landing page                            |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| privacyUrl        | string                        | The URL of the privacy policy                                     |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| termsUrl          | string                        | The URL of the terms of use                                       |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| inventoryUrl      | string                        | The URL which leads to adserver inventory (active campaigns)      |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| adsAddress        | string                        | The address of adserver's ADS blockchain account                  |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| registrationMode  | one of constants: "public",   | Openness to new users:                                            |
|                   | "restricted", "private"       |                                                                   |
|                   |                               | - public - users can register freely                              |
|                   |                               | - restricted - users can register if they have invitation,        |
|                   |                               |   e.g. using referral link                                        |
|                   |                               | - private - no new users are accepted                             |
|                   |                               |                                                                   |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| supportEmail      | string                        | The e-mail where users can find help                              |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| demandFee         | float                         | The fraction of advertiser's expenses taken by adserver's         |
|                   |                               | operator                                                          |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| supplyFee         | float                         | the fraction of payments for ads publishing taken by adserver's   |
|                   |                               | operator                                                          |
+-------------------+-------------------------------+-------------------------------------------------------------------+
| statistics        | object                        | The object holding adserver's statistics. It has integer fields:  |
|                   |                               |                                                                   |
|                   |                               | - users – number of active users                                  |
|                   |                               | - campaigns – number of active campaigns                          |
|                   |                               | - sites – number of registered sites                              |
|                   |                               |                                                                   |
+-------------------+-------------------------------+-------------------------------------------------------------------+

Example::

  {
    "module": "adserver",
    "name": "Example",
    "version": "v1.17.0",
    "capabilities": ["ADV", "PUB"],
    "serverUrl": "https:\/\/app.example.net",
    "panelUrl": "https:\/\/example.net",
    "privacyUrl": "https:\/\/app.example.net\/policies\/privacy.html",
    "termsUrl": "https:\/\/app.example.net\/policies\/terms.html",
    "inventoryUrl": "https:\/\/app.example.net\/adshares\/inventory\/list",
    "adsAddress": "0001-00000000-9B6F",
    "registrationMode": "public",
    "supportEmail": "support@example.net",
    "demandFee": 0.109,
    "supplyFee": 0.109,
    "statistics": {
      "users": 847,
      "campaigns": 20,
      "sites": 223
    }
  }

Broadcast
----------
The metadata must be located by publicly accessible URL.
Encode this URL to uppercase hex string.
Most programming languages have an utility to convert ASCII string to it's hexadecimal representation.
Online converters can be used also.

Example URL::

  https://app.example.com/info.json

Example URL after encoding::

  68747470733A2F2F6170702E6578616D706C652E636F6D2F696E666F2E6A736F6E

The encoded URL is the message to be broadcast.
Broadcast should be done twice a day, i.e. every 12 hours.

.. note::

    Broadcast must be sent from the account set as ``adsAddress`` in metadata.

**TODO** Do we want to show details of ads (install, set up, send message)?
Instruction how to broadcast using *ads* client:
:ref:`ADS API broadcast <broadcast>`

We provide a PHP client for the ADS blockchain.
Source code is available on GitHub: https://github.com/adshares/ads-php-client.
Install package with Composer

::

    composer require adshares/ads-client

We provide a JSON RPC client.
Source code is available on GitHub: https://github.com/adshares/ads-json-rpc.