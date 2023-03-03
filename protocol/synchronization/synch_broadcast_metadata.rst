.. _protocol-synchronization-metadata:

Metadata Format
---------------

The :ref:`Platform Metadata <protocol-definitions-metadata>` should be located under a publicly accessible URL.

The :ref:`Platform Metadata <protocol-definitions-metadata>` should be in the in JSON format.

All fields should be using string values, unless stated otherwise.

Metadata Fields
"""""""""""""""

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

Metadata Example
""""""""""""""""

::

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
