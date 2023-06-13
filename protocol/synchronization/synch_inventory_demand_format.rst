.. _protocol-synchronization-demandinventory-format:

Demand-Side Inventory Format
----------------------------

The data describing :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` implements the following JSON format:

* The values for all fields are expressed as strings, unless stated otherwise.
* Dates are in extended date and time ISO8601 format, e.g. ``2021-08-26T10:21:15+00:00``.
* Amounts are integers, denominated in clicks, as explained below:

::

    1 click === 1e-11 ADS
    1 ADS === 100,000,000,000 click

:ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` is an array of :ref:`Campaign Objects <protocol-campaign-object>`.

.. _protocol-campaign-object:

Campaign Object
~~~~~~~~~~~~~~~
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| Field              | Type                                         | Description                                                       |
+====================+==============================================+===================================================================+
| id                 | string                                       | UUID                                                              |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| landing_url        | string                                       | The URL of landing page                                           |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| date_start         | string                                       | Date of start                                                     |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| date_end           | string or null                               | Date of end, ``null`` for indeterminate                           |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| created_at         | string                                       | Date of creation                                                  |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| updated_at         | string                                       | Date of last update                                               |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| medium             | string                                       | Medium                                                            |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| vendor             | string or null                               | Vendor, ``null`` for vendor agnostic campaign                     |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| max_cpc            | integer                                      | Maximal amount which can be payed per click                       |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| max_cpm            | integer or null                              | Maximal amount which can be payed per mille (thousand views),     |
|                    |                                              | ``null`` for automatic tuning                                     |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| budget             | integer                                      | Maximal amount which can be payed for all events per hour         |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| creatives          | array of                                     | Creatives                                                         |
|                    | :ref:`Creative Objects                       |                                                                   |
|                    | <protocol-creative-object>`                  |                                                                   |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| targeting_requires | array of                                     | Required targeting                                                |
|                    | :ref:`Targeting Objects                      |                                                                   |
|                    | <protocol-targeting-object>`                 |                                                                   |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+
| targeting_excludes | array of                                     | Excluded targeting                                                |
|                    | :ref:`Targeting Objects                      |                                                                   |
|                    | <protocol-targeting-object>`                 |                                                                   |
+--------------------+----------------------------------------------+-------------------------------------------------------------------+

.. _protocol-creative-object:

Creative Object
~~~~~~~~~~~~~~~
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| Field          | Type                                                   | Description                                                  |
+================+========================================================+==============================================================+
| id             | string                                                 | UUID                                                         |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| size           | string                                                 | Space occupied by creative content                           |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| type           | string                                                 | Type: "image", "video", etc.                                 |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| mime           | string                                                 | MIME type                                                    |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| checksum       | string                                                 | SHA-1 checksum of content                                    |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| serve_url      | string                                                 | The URL of creative content                                  |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| click_url      | string                                                 | The URL of click callback                                    |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| view_url       | string                                                 | The URL of view callback                                     |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+
| classification | :ref:`Classification Object                            | Classification                                               |
|                | <protocol-classification-object>`                      |                                                              |
+----------------+--------------------------------------------------------+--------------------------------------------------------------+

.. _protocol-classification-object:

Classification Object
~~~~~~~~~~~~~~~~~~~~~

:ref:`Classification Object <protocol-classification-object>`'s key is the classifier’s ID (usually corresponding to ADS account address). 

:ref:`Classification Object <protocol-classification-object>`'s value is an object with following keys:

* keywords -- features compatible with classifier :ref:`Taxonomy <protocol-taxonomy>`
* signature -- signature of classification
* signed_at -- date of signature

.. _protocol-targeting-object:

Targeting Object
~~~~~~~~~~~~~~~~

**TODO** https://adshares.atlassian.net/browse/ACP-6

:ref:`Targeting Object <protocol-targeting-object>` matches the targeting :ref:`Taxonomy <protocol-taxonomy>`.

Example::

    [
      {
        "id": "f3339e88383a4264aa6acedd6ee00865",
        "landing_url": "https://example.com",
        "date_start": "2021-08-26T10:21:15+00:00",
        "date_end": null,
        "created_at": "2021-08-26T10:57:37+00:00",
        "updated_at": "2022-05-20T16:23:07+00:00",
        "max_cpc": 0,
        "max_cpm": null,
        "budget": 72184612500,
        "creatives": [
          {
            "id": "0c3439d1ae2c420d8864a86a660217b8",
            "size": "300x250",
            "type": "html",
            "mime": "text/html",
            "checksum": "b80f67f5b64e8327e45e02f208f0299e977e503d",
            "serve_url": "https://app.example.com/serve/x0c3439d1ae2c420d8864a86a660217b8.doc?v=b80b",
            "click_url": "https://app.example.com/click/0c3439d1ae2c420d8864a86a660217b8",
            "view_url": "https://app.example.com/view/0c3439d1ae2c420d8864a86a660217b8",
            "classification": {
              "0001000000081a67": {
                "keywords": {
                  "quality": [
                    "high"
                  ],
                  "category": [
                    "crypto"
                  ]
                },
                "signature": "0dfe07f3134007f0deec9a16d9d3ad8c32d2de887df10b8861f416277f6fa4bc454814adba40fd2aad8216b7a7c4f5325a25e3c2984a4a64ea8317c9852afe0b",
                "signed_at": "2022-02-10T14:08:02+00:00"
              }
            }
          }
        ],
        "targeting_requires": {
          "site": {
            "quality": [
              "high"
            ]
          }
        },
        "targeting_excludes": {
          "user": {
            "country": [
              "us"
            ]
          }
        }
      }
    ]
