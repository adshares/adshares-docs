Campaigns
===========

Campaigns list
--------------------------

.. http:get:: /api/v2/campaigns

    Fetch campaigns.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Campaign[] data: campaign list

.. http:get:: /api/v2/campaigns/(id)

    Fetch campaign by ID.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: campaign does not exist

    :>json Campaign data: campaign

Parameters
-----------------

.. http:get:: /api/v2/taxonomy/media

    Fetch supported media.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :response json object: Map of supported media. Key is medium ID. Value is medium name

.. http:get:: /api/v2/taxonomy/media/(medium)/vendors

    Fetch supported vendors by medium.

    :param medium: medium ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :response json object: Map of supported vendors. Key is vendor ID. Value is vendor name

.. http:get:: /api/v2/taxonomy/media/(medium)

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
    :>json string size: (optional) space occupied by advertisement, size is not present in case of resizable advertisements, e.g. HTML

Add campaign
--------------------

.. http:post:: /api/v2/campaigns

    Add campaign.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :<json integer status: status
    :<json string name: name
    :<json string targetUrl: landing URL
    :<json integer, null maxCpc: maximal CPC
    :<json integer, null maxCpm: maximal CPM
    :<json integer budget: budget
    :<json string medium: medium
    :<json string, null vendor: vendor
    :<json string dateStart: date of start in ISO 8601 format
    :<json string, null dateEnd: date of end in ISO 8601 format, if `null` campaign will last forever
    :<json CampaignTargeting campaign.targeting: targeting (required and forbidden features)
    :<json Advertisement[] campaign.ads: advertisements

    :>json Campaign data: campaign

Edit campaign
--------------------

.. http:post:: /api/v2/campaigns/(id)

    Edit campaign.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :<json integer status: (optional) status
    :<json string name: (optional) name
    :<json string targetUrl: (optional) landing URL
    :<json integer, null maxCpc: (optional) maximal CPC
    :<json integer, null maxCpm: (optional) maximal CPM
    :<json integer budget: (optional) budget
    :<json string dateStart: (optional) date of start in ISO 8601 format
    :<json string, null dateEnd: (optional) date of end in ISO 8601 format, if `null` campaign will last forever
    :<json CampaignTargeting campaign.targeting: (optional) targeting (required and forbidden features)
    :<json string bidStrategyUuid: (optional) bid strategy UUID

Delete campaign
--------------------

.. http:delete:: /api/v2/campaigns/(id)

    Delete campaign by ID.

    :param id: campaign ID

    :statuscode 204: no error
    :statuscode 404: campaign does not exist

Add advertisement
--------------------

.. http:post:: /api/v2/campaigns/(id)/banners

    Add advertisement.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :<json integer status: status
    :<json string name: name
    :<json string targetUrl: landing URL
    :<json integer, null maxCpc: maximal CPC
    :<json integer, null maxCpm: maximal CPM
    :<json integer budget: budget
    :<json string medium: medium
    :<json string, null vendor: vendor
    :<json string dateStart: date of start in ISO 8601 format
    :<json string, null dateEnd: date of end in ISO 8601 format, if `null` campaign will last forever
    :<json CampaignTargeting campaign.targeting: targeting (required and forbidden features)
    :<json Advertisement[] campaign.ads: advertisements

Data structures
--------------------

Campaign object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **id** (`integer`) – campaign ID
- **uuid** (`string`) – campaign UUID
- **createdAt** (`string`) – date of creation
- **updatedAt** (`string`) – date of last update
- **secret** (`string`) – conversion secret
- **conversionClick** (`integer`) – type of click conversion
- **conversionClickLink** (`string`) – click conversion callback URL, may be `null` if click conversion is not set
- **classifications[].classifier** (`string`) – classifier
- **classifications[].status** (`string`) – classification status
- **classifications[].keywords** (`string`) – classification result, conforms taxonomy
- **status** (`string`) – status
- **name** (`string`) – name
- **targetUrl** (`string`) – landing URL
- **maxCpc** (`integer, null`) – maximal CPC
- **maxCpm** (`integer, null`) – maximal CPM
- **budget** (`integer`) – budget
- **medium** (`string`) – medium
- **vendor** (`string, null`) – vendor
- **dateStart** (`string`) – date of start in ISO 8601 format
- **dateEnd** (`string, null`) – date of end in ISO 8601 format, if `null` campaign will last forever
- **targeting** (`CampaignTargeting`) – required and forbidden features, conforms taxonomy
- **ads[].id** (`integer`) – advertisement ID
- **ads[].uuid** (`string`) – advertisement UUID
- **ads[].createdAt** (`string`) – date of advertisement creation
- **ads[].updatedAt** (`string`) – date of last advertisement update
- **ads[].creativeType** (`string`) – advertisement type
- **ads[].creativeMime** (`string`) – advertisement MIME type
- **ads[].creativeSha1** (`string`) – SHA-1 checksum of advertisement content
- **ads[].creativeSize** (`string`) – space occupied by advertisement
- **ads[].name** (`string`) – advertisement name
- **ads[].status** (`integer`) – advertisement status
- **ads[].cdnUrl** (`string, null`) – advertisement content URL on CDN, may be `null` if was not uploaded to CDN
- **ads[].url** (`string`) – advertisement content URL
- **bidStrategyUuid** (`string`) – bid strategy UUID
- **conversions[].uuid** (`string`) – conversion UUID
- **conversions[].campaignId** (`integer`) – campaign ID
- **conversions[].name** (`string`) – conversion name
- **conversions[].limitType** (`string`) – conversion limit type
- **conversions[].eventType** (`string`) – conversion event type
- **conversions[].type** (`string`) – conversion type
- **conversions[].value** (`integer`) – conversion value
- **conversions[].isValueMutable** (`boolean`) – indicates that value can change
- **conversions[].cost** (`integer`) – conversion cost
- **conversions[].occurrences** (`integer`) – number of conversion occurrences
- **conversions[].isRepeatable** (`boolean`) – indicates that conversion can be repeated
- **conversions[].link** (`string`) – conversion link

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

- **name** (`string`) – name
- **creativeSize** (`string`) – occupied space. It should be the same as size returned during upload if was present
- **creativeType** (`string`) – type
- **url** (`string`) – (optional) temporary URL returned in response to upload advertisement request. It is required for advertisement which needs to be uploaded, e.g. image
- **creativeContents** (`string`) – (optional) content. It is suggested for advertisement which does not use upload, e.g. direct links. By default content is campaign landing URL
