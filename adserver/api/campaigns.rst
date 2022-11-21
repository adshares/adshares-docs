Campaigns
===========

Campaigns list
--------------------------

.. http:get:: /api/v2/campaigns

    Fetch campaigns.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json integer data[].id: ID
    :>json string data[].uuid: UUID
    :>json string data[].createdAt: date of creation
    :>json string data[].updatedAt: date of last update
    :>json string data[].secret: conversion secret
    :>json integer data[].conversionClick: type of click conversion
    :>json string data[].conversionClickLink: click conversion callback URL
    :>json string data[].classifications[].classifier: classifier
    :>json string data[].classifications[].status: status
    :>json object data[].classifications[].keywords: classification result, conforms taxonomy
    :>json integer data[].basicInformation.status: status
    :>json string data[].basicInformation.name: name
    :>json string data[].basicInformation.targetUrl: landing URL
    :>json integer, null data[].basicInformation.maxCpc: maximal CPC
    :>json integer, null data[].basicInformation.maxCpm: maximal CPM
    :>json integer, null data[].basicInformation.budget: budget
    :>json string data[].basicInformation.medium: medium, e.g. "web"
    :>json string, null data[].basicInformation.vendor: vendor
    :>json string data[].basicInformation.dateStart: date of start
    :>json string, null data[].basicInformation.dateEnd: date of end, if `null` campaign will last forever
    :>json object data[].targeting.requires: required features, conforms taxonomy
    :>json object data[].targeting.excludes: forbidden features, conforms taxonomy
    :>json integer data[].ads[].id: banner ID
    :>json string data[].ads[].uuid: UUID
    :>json string data[].ads[].createdAt: date of banner creation
    :>json string data[].ads[].updatedAt: date of last banner update
    :>json string data[].ads[].creativeType: banner type
    :>json string data[].ads[].creativeMime: banner MIME type
    :>json string data[].ads[].creativeSha1: SHA-1 checksum of banner content
    :>json string data[].ads[].creativeSize: space occupied by banner
    :>json string data[].ads[].name: banner name
    :>json integer data[].ads[].status: banner status
    :>json string, null data[].ads[].cdnUrl: banner content URL on CDN, may be `null` if was not uploaded to CDN
    :>json string data[].ads[].url: banner content URL
    :>json string data[].bidStrategy.name: bid strategy name
    :>json string data[].bidStrategy.uuid: bid strategy UUID
    :>json string data[].conversions[].uuid: conversion UUID
    :>json string data[].conversions[].campaignId: campaign ID
    :>json string data[].conversions[].name: conversion name
    :>json string data[].conversions[].limitType: conversion limit type
    :>json string data[].conversions[].eventType: conversion event type
    :>json string data[].conversions[].type: conversion type
    :>json integer data[].conversions[].value: conversion value
    :>json boolean data[].conversions[].isValueMutable: conversion type
    :>json integer data[].conversions[].cost: conversion cost
    :>json integer data[].conversions[].occurrences: number of conversion occurrences
    :>json boolean data[].conversions[].isRepeatable: can conversion be repeated
    :>json boolean data[].conversions[].link: conversion link

.. http:get:: /api/v2/campaigns/{id}

    Fetch campaign by ID.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: campaign does not exist

Parameters
-----------------

.. http:get:: /api/v2/options/campaigns

    Fetch campaign limits.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json integer minBudget: minimal hourly budget in clicks
    :>json integer minCpm: minimal CPM in clicks
    :>json integer minCpa: minimal CPA in clicks


.. http:get:: /api/v2/options/campaigns/media

    Fetch supported media.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :response json object: Map of supported media. Key is medium ID. Value is medium name

.. http:get:: /api/v2/options/campaigns/media/(medium)/vendors

    Fetch supported vendors by medium.

    :param medium: medium ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :response json object: Map of supported vendors. Key is vendor ID. Value is vendor name

.. http:get:: /api/v2/options/campaigns/media/(medium)

    Fetch taxonomy for medium.

    :param medium: medium ID

    :query vendor: (optional) vendor ID. If omitted, default vendor will be returned

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json string name: medium ID
    :>json string label: medium name
    :>json string vendor: vendor ID
    :>json string vendorLabel: vendor name
    :>json object formats[].type: format type
    :>json array<string> formats[].mimes: array of MIME types
    :>json object formats[].scopes: map of scopes. Key is scope. Value is description
    :>json Targeting object targeting.user: user targeting
    :>json Targeting object targeting.site: site targeting
    :>json Targeting object targeting.device: device targeting

Targeting object
^^^^^^^^^^^^^^^^^

Targeting object contains features which campaign can require or forbid.
There are two types:

- dictionary - list of supported values
- custom input - values entered by advertiser

Dictionary targeting object
""""""""""""""""""""""""""""""""""""

- **type** (`string`) – constant ``dict``
- **name** (`string`) – name
- **label** (`string`) – label
- **items** (`TargetingDictionary object`) – possible values

**TargetingDictionary object**

TargetingDictionary object holds possible values.
Usually this is a map, where key is an ID and value is a label (`string`).

In general it is a nested structure. Key is an ID. Value is an object or a string.
If value is an object it has fields:

- **label** (`string`) - option label
- **values** (`TargetingDictionary object`) - possible values

**Example**

.. sourcecode:: json

    {
        "type": "dict",
        "name": "tag",
        "label": "Tags",
        "items": {
            "nft": {
                "label": "NFTs",
                "values": {
                    "nft-sports": "Sports",
                    "nft-tickets": "Tickets"
                }
            }
        }
    }

Custom input targeting object
"""""""""""""""""""""""""""""""""""

- **type** (`string`) – constant ``input``
- **name** (`string`) – name
- **label** (`string`) – label

**Example**

.. sourcecode:: json

    {
        "type": "input",
        "name": "domain",
        "label": "Domains"
    }
