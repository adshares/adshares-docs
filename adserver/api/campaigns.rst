Campaigns
===========

Campaign
--------------------------

Fetch campaign list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/campaigns

    Fetch campaigns. Response uses :ref:`Pagination<response-pagination>`.

    :query limit: (optional) maximal number of campaigns per page

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Campaign[] data: :ref:`campaign list<campaign-object>`

Fetch campaign
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/campaigns/(id)

    Fetch campaign by ID.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: campaign not found

    :>json Campaign data: :ref:`campaign<campaign-object>`

Add campaign
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    :<json CampaignTargeting campaign.targeting: :ref:`targeting<campaign-targeting-object>` (required and forbidden features)
    :<json AdvertisementInput[] campaign.ads: :ref:`banners<advertisement-input-object>`

    :>json Campaign data: :ref:`campaign<campaign-object>`

Edit campaign
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    :<json CampaignTargeting campaign.targeting: (optional) :ref:`targeting<campaign-targeting-object>` (required and forbidden features)
    :<json string bidStrategyUuid: (optional) bid strategy UUID

Delete campaign
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:delete:: /api/v2/campaigns/(id)

    Delete campaign by ID.

    :param id: campaign ID

    :statuscode 200: no error
    :statuscode 404: campaign not found

    :>json data: empty array

Banner
--------------------------

.. _upload-banner:

Upload banner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Fetch banner list
^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/campaigns/(campaignId)/banners

    Fetch banners. Response uses :ref:`Pagination<response-pagination>`.

    :param campaignId: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Banner[] data: :ref:`banner list<banner-object>`

Fetch banner
^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/campaigns/(campaignId)/banners/(bannerId)

    Fetch banner by ID.

    :param campaignId: campaign ID
    :param bannerId: banner ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: banner not found

    :>json Banner data: :ref:`banner<banner-object>`

Add banner
^^^^^^^^^^^^^^^^^^^^^^^

.. http:post:: /api/v2/campaigns/(id)/banners

    Add banner.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :request json object: banner data (:ref:`AdvertisementInput<advertisement-input-object>`)

    :>json Banner data: :ref:`banner<banner-object>`

Edit banner
^^^^^^^^^^^^^^^^^^^^^^^

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

    :>json Banner data: :ref:`banner<banner-object>`

Delete banner
^^^^^^^^^^^^^^^^^^^^^^^

.. http:delete:: /api/v2/campaigns/(campaignId)/banners/(bannerId)

    Delete banner.

    :param campaignId: campaign ID
    :param bannerId: banner ID

    :statuscode 200: no error
    :statuscode 404: banner not found

    :>json data: empty array

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

.. _campaign-object:

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
- **targeting** (:ref:`CampaignTargeting<campaign-targeting-object>`) – required and forbidden features, conforms taxonomy
- **ads** (:ref:`Banner[]<banner-object>`) – banner
- **bidStrategyUuid** (`string`) – bid strategy UUID
- **conversions[].uuid** (`string`) – conversion UUID
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

.. _campaign-targeting-object:

CampaignTargeting object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **requires** (:ref:`Targeting<targeting-object>`) – required features
- **excludes** (:ref:`Targeting<targeting-object>`) – forbidden features

.. _targeting-object:

Targeting object
^^^^^^^^^^^^^^^^^

- **user** (:ref:`TargetingFeatures<targeting-features-object>`) – (optional) user features
- **site** (:ref:`TargetingFeatures<targeting-features-object>`) – (optional) site features
- **device** (:ref:`TargetingFeatures<targeting-features-object>`) – (optional) device features

.. _targeting-features-object:

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

.. _banner-object:

Banner object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **id** (`integer`) – banner ID
- **uuid** (`string`) – banner UUID
- **createdAt** (`string`) – date of banner creation
- **updatedAt** (`string`) – date of last banner update
- **creativeType** (`string`) – banner type
- **creativeMime** (`string`) – banner MIME type
- **creativeSha1** (`string`) – SHA-1 checksum of banner content
- **creativeSize** (`string`) – space occupied by banner
- **name** (`string`) – banner name
- **status** (`integer`) – banner :ref:`status<banner-status>`
- **cdnUrl** (`string, null`) – banner content URL on CDN, may be `null` if was not uploaded to CDN
- **url** (`string`) – banner content URL

.. _advertisement-input-object:

AdvertisementInput object
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **name** (`string`) – name
- **creativeSize** (`string`) – occupied space. It should be the same as size returned during upload if was present
- **creativeType** (`string`) – type
- **url** (`string`) – (optional) temporary URL returned in response to :ref:`upload banner request<upload-banner>`. It is required for banner which needs to be uploaded, e.g. image
- **creativeContents** (`string`) – (optional) content. It is suggested for banner which does not use upload, e.g. direct links. By default content is campaign landing URL
