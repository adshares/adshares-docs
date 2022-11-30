Campaigns
===========

Fetch campaign list
--------------------------

.. http:get:: /api/v2/campaigns

    Fetch campaigns. Response uses :ref:`Pagination<response-pagination>`.

    :query limit: (optional) maximal number of campaigns per page

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Campaign[] data: campaign list

Fetch campaign
--------------------------

.. http:get:: /api/v2/campaigns/(id)

    Fetch campaign by ID.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: campaign not found

    :>json Campaign data: campaign

Upload banner
--------------------------

.. http:post:: /api/v2/campaigns/banner

    Upload banner.

    :reqheader Content-Type: ``multipart/form-data``

    :form binary file: file
    :form string medium: medium ID
    :form string vendor: (optional) vendor ID

    :statuscode 200: no error
    :statuscode 422: validation error

    :>json string data.name: temporary name
    :>json string data.url: temporary URL
    :>json string data.size: (optional) space occupied by banner, size is not present in case of resizable banners, e.g. HTML

Add campaign
--------------------

.. http:post:: /api/v2/campaigns

    Add campaign.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :<json string status: :ref:`status<campaign-status>`
    :<json string name: name
    :<json string targetUrl: landing URL
    :<json integer, null maxCpc: maximal CPC in clicks
    :<json integer, null maxCpm: maximal CPM in clicks, ``null`` for automatic
    :<json integer budget: budget in clicks
    :<json string medium: medium
    :<json string, null vendor: vendor
    :<json string dateStart: date of start in ISO 8601 format
    :<json string, null dateEnd: date of end in ISO 8601 format, `null` for interminable campaign
    :<json CampaignTargeting campaign.targeting: targeting (required and forbidden features)
    :<json Advertisement[] campaign.ads: banners

    :>json Campaign data: campaign

Edit campaign
--------------------

.. http:post:: /api/v2/campaigns/(id)

    Edit campaign.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :<json string status: (optional) :ref:`status<campaign-status>`
    :<json string name: (optional) name
    :<json string targetUrl: (optional) landing URL
    :<json integer, null maxCpc: (optional) maximal CPC in clicks
    :<json integer, null maxCpm: (optional) maximal CPM in clicks, ``null`` for automatic
    :<json integer budget: (optional) budget in clicks
    :<json string dateStart: (optional) date of start in ISO 8601 format
    :<json string, null dateEnd: (optional) date of end in ISO 8601 format, `null` for interminable campaign
    :<json CampaignTargeting campaign.targeting: (optional) targeting (required and forbidden features)
    :<json string bidStrategyUuid: (optional) bid strategy UUID

Delete campaign
--------------------

.. http:delete:: /api/v2/campaigns/(id)

    Delete campaign by ID.

    :param id: campaign ID

    :statuscode 200: no error
    :statuscode 404: campaign not found

    :>json data: empty array

Fetch banner list
--------------------------

.. http:get:: /api/v2/campaigns/(campaignId)/banners

    Fetch banners. Response uses :ref:`Pagination<response-pagination>`.

    :param campaignId: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Advertisement[] data: banner list

Fetch banner
--------------------------

.. http:get:: /api/v2/campaigns/(campaignId)/banners/(bannerId)

    Fetch banner by ID.

    :param campaignId: campaign ID
    :param bannerId: banner ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: banner not found

    :>json Advertisement data: banner

Add banner
--------------------

.. http:post:: /api/v2/campaigns/(id)/banners

    Add banner.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :request json object: banner data :ref:`(Advertisement)<advertisement-object>`

    :>json Advertisement data: banner

Edit banner
--------------------

.. http:post:: /api/v2/campaigns/(campaignId)/banners/(bannerId)

    Edit banner.

    :param campaignId: campaign ID
    :param bannerId: banner ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: banner not found
    :statuscode 422: validation error

    :<json string name: (optional) name
    :<json integer status: (optional) :ref:`status<banner-status>`

    :>json Advertisement data: banner

Delete banner
--------------------

.. http:delete:: /api/v2/campaigns/(campaignId)/banners/(bannerId)

    Delete banner.

    :param campaignId: campaign ID
    :param bannerId: banner ID

    :statuscode 200: no error
    :statuscode 404: banner not found

    :>json data: empty array

Taxonomy
-----------------

Media
^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/taxonomy/media

    Fetch supported media.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json object data: map of supported media. Key is medium ID. Value is medium name

Vendors
^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/taxonomy/media/(medium)/vendors

    Fetch supported vendors by medium.

    :param medium: medium ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json object data: map of supported vendors. Key is vendor ID. Value is vendor name

Taxonomy by medium
^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/taxonomy/media/(medium)

    Fetch taxonomy for medium.

    :param medium: medium ID
    :query vendor: (optional) vendor ID. If omitted, default vendor will be returned

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Taxonomy data: taxonomy

Data structures
--------------------

.. _campaign-status:

Campaign status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Campaign status is a string. Campaign can be in one of following states:

- draft - campaign during creation
- inactive - campaign is not active, e.g. stopped
- active - campaign is active
- suspended - campaign suspended, e.g. in case of insufficient funds to run campaign

.. _banner-status:

Banner status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Banner status is a string. Banner can be in one of following states:

- draft - banner during creation
- inactive - banner is not active, will not be displayed
- active - banner is active
- rejected - banner is permanently disabled, e.g. does not comply with terms

Campaign object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **id** (`integer`) – campaign ID
- **uuid** (`string`) – campaign UUID
- **createdAt** (`string`) – date of creation
- **updatedAt** (`string`) – date of last update
- **secret** (`string`) – conversion secret
- **conversionClick** (`string`) – type of click conversion, i.e. ``none``, ``basic``, ``advanced``
- **conversionClickLink** (`string, null`) – click conversion callback URL, may be `null` if click conversion is not set
- **classifications[].classifier** (`string`) – classifier
- **classifications[].status** (`string`) – classification status
- **classifications[].keywords** (`string`) – classification result, conforms taxonomy
- **status** (`string`) – :ref:`status<campaign-status>`
- **name** (`string`) – name
- **targetUrl** (`string`) – landing URL
- **maxCpc** (`integer, null`) – maximal CPC in clicks
- **maxCpm** (`integer, null`) – maximal CPM in clicks, ``null`` for automatic
- **budget** (`integer`) – budget in clicks
- **medium** (`string`) – medium
- **vendor** (`string, null`) – vendor
- **dateStart** (`string`) – date of start in ISO 8601 format
- **dateEnd** (`string, null`) – date of end in ISO 8601 format, `null` for interminable campaign
- **targeting** (`CampaignTargeting`) – required and forbidden features, conforms taxonomy
- **ads[].id** (`integer`) – banner ID
- **ads[].uuid** (`string`) – banner UUID
- **ads[].createdAt** (`string`) – date of banner creation
- **ads[].updatedAt** (`string`) – date of last banner update
- **ads[].creativeType** (`string`) – banner type
- **ads[].creativeMime** (`string`) – banner MIME type
- **ads[].creativeSha1** (`string`) – SHA-1 checksum of banner content
- **ads[].creativeSize** (`string`) – space occupied by banner
- **ads[].name** (`string`) – banner name
- **ads[].status** (`integer`) – banner :ref:`status<banner-status>`
- **ads[].cdnUrl** (`string, null`) – banner content URL on CDN, may be `null` if was not uploaded to CDN
- **ads[].url** (`string`) – banner content URL
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


Taxonomy object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **name** (`string`) – medium ID
- **label** (`string`) – medium name
- **vendor** (`string`) – vendor ID
- **vendorLabel** (`string`) – vendor name
- **formats[].type** (`string`) – format type
- **formats[].mimes** (`string[]`) – MIME types
- **formats[].scopes** (`object`) – map of scopes. Key is scope. Value is description
- **targeting.user** (`TargetingOption[]`) – (optional) user targeting options
- **targeting.site** (`TargetingOption[]`) – (optional) site targeting options
- **targeting.device** (`TargetingOption[]`) – (optional) device targeting options

.. _advertisement-object:

Advertisement object
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **name** (`string`) – name
- **creativeSize** (`string`) – occupied space. It should be the same as size returned during upload if was present
- **creativeType** (`string`) – type
- **url** (`string`) – (optional) temporary URL returned in response to upload banner request. It is required for banner which needs to be uploaded, e.g. image
- **creativeContents** (`string`) – (optional) content. It is suggested for banner which does not use upload, e.g. direct links. By default content is campaign landing URL
