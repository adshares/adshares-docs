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
    :>json CampaignBasicInformation data[].basicInformation: basic information
    :>json CampaignTargeting data[].targeting: required and forbidden features, conforms taxonomy
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

.. http:delete:: /api/v2/campaigns/{id}

    Delete campaign by ID.

    :statuscode 204: no error
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
    :>json TargetingOption[] targeting.user: (optional) user targeting options
    :>json TargetingOption[] targeting.site: (optional) site targeting options
    :>json TargetingOption[] targeting.device: (optional) device targeting options

Upload advertisement
--------------------------

.. http:post:: /api/v2/campaigns/banner

    Upload advertisement.

    :reqheader Content-Type: ``multipart/form-data``

    :form binary file: file
    :form string medium: medium ID
    :form string vendor: (optional) vendor ID

    :statuscode 200: no error

    :>json string name: temporary name
    :>json string url: temporary URL
    :>json string size: space occupied by advertisement

Add campaign
--------------------

.. http:post:: /api/v2/campaigns

    Add campaign.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :<json CampaignBasicInformation campaign.basicInformation: basic information
    :<json CampaignTargeting campaign.targeting: targeting (required and forbidden features)
    :<json Advertisement[] campaign.ads: advertisements

Data structures
--------------------

CampaignBasicInformation object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **status** (`integer`) – status
- **name** (`string`) – name
- **targetUrl** (`string`) – landing URL
- **maxCpc** (`integer, null`) – maximal CPC
- **maxCpm** (`integer, null`) – maximal CPM
- **budget** (`integer`) – budget
- **medium** (`string`) – medium
- **vendor** (`string, null`) – vendor
- **dateStart** (`string`) – date of start
- **dateEnd** (`string, null`) – date of end, if `null` campaign will last forever

CampaignTargeting object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **requires** (`Targeting`) – required features
- **excludes** (`Targeting`) – forbidden features

Targeting object
^^^^^^^^^^^^^^^^^

- **user** (`TargetingFeatures`) – (optional) user features
- **site** (`TargetingFeatures`) – (optional) site features
- **device** (`TargetingFeatures`) – (optional) device features

TargetingFeatures object
^^^^^^^^^^^^^^^^^^^^^^^^^^

TargetingFeatures object has selected features.
It is a map in which key is a name of TargetingOption, and value is array of selected items.
Both key and value must match taxonomy.

**Example**

.. sourcecode:: json

    {
        "quality": ["high"],
        "domain": ["example.com"]
        "tag": ["nft", "nft-sports", "nft-tickets"]
    }


TargetingOption object
^^^^^^^^^^^^^^^^^^^^^^^^^^

TargetingOption object contains features which campaign can require or forbid.

There are two types:

- dictionary - list of supported values
- custom input - values entered by advertiser

Dictionary targeting object
""""""""""""""""""""""""""""""""""""

- **type** (`string`) – constant ``dict``
- **name** (`string`) – name
- **label** (`string`) – label
- **items** (`TargetingDictionary`) – possible values

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


Advertisement object
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **status** (`integer`) – status
- **name** (`string`) – name
- **creativeSize** (`string`) – occupied space
- **creativeType** (`string`) – type
- **url** (`string`) – (optional) temporary URL returned in response to upload advertisement request. It is required for advertisement which needs to be uploaded, e.g. image
- **creativeContents** (`string`) – (optional) content. It is suggested for advertisement which does not use upload, e.g. direct links. By default content is campaign landing URL
