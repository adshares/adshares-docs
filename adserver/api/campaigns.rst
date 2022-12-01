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
    :<json CreativeInput[] campaign.creatives: :ref:`creatives<creative-input-object>`

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

Creative
--------------------------

.. _upload-creative:

Upload creative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:post:: /api/v2/campaigns/creative

    Upload creative.

    :reqheader Content-Type: ``multipart/form-data``

    :form binary file: file
    :form string medium: medium ID
    :form string vendor: (optional) vendor ID

    :statuscode 200: no error
    :statuscode 422: validation error

    :>json string data.name: temporary name
    :>json string data.url: temporary URL
    :>json string data.size: (optional) space occupied by creative, size is not present in case of resizable creatives, e.g. HTML

Fetch creative list
^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/campaigns/(campaignId)/creatives

    Fetch creatives. Response uses :ref:`Pagination<response-pagination>`.

    :param campaignId: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Creative[] data: :ref:`creative list<creative-object>`

Fetch creative
^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/v2/campaigns/(campaignId)/creatives/(creativeId)

    Fetch creative by ID.

    :param campaignId: campaign ID
    :param creativeId: creative ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: creative not found

    :>json Creative data: :ref:`creative<creative-object>`

Add creative
^^^^^^^^^^^^^^^^^^^^^^^

.. http:post:: /api/v2/campaigns/(id)/creatives

    Add creative.

    :param id: campaign ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: validation error

    :request json object: creative data (:ref:`CreativeInput<creative-input-object>`)

    :>json Creative data: :ref:`creative<creative-object>`

Edit creative
^^^^^^^^^^^^^^^^^^^^^^^

.. http:post:: /api/v2/campaigns/(campaignId)/creatives/(creativeId)

    Edit creative.

    :param campaignId: campaign ID
    :param creativeId: creative ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: creative not found
    :statuscode 422: validation error

    :<json string name: (optional) name
    :<json integer status: (optional) :ref:`status<creative-status>`

    :>json Creative data: :ref:`creative<creative-object>`

Delete creative
^^^^^^^^^^^^^^^^^^^^^^^

.. http:delete:: /api/v2/campaigns/(campaignId)/creatives/(creativeId)

    Delete creative.

    :param campaignId: campaign ID
    :param creativeId: creative ID

    :statuscode 200: no error
    :statuscode 404: creative not found

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

.. _creative-status:

Creative status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creative status is a string. Creative can be in one of following states:

- draft - creative during creation
- inactive - creative is not active, will not be displayed
- active - creative is active
- rejected - creative is permanently disabled, e.g. does not comply with terms

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
- **creatives** (:ref:`Creative[]<creative-object>`) – creative
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

.. _creative-object:

Creative object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **id** (`integer`) – creative ID
- **uuid** (`string`) – creative UUID
- **createdAt** (`string`) – date of creative creation
- **updatedAt** (`string`) – date of last creative update
- **creativeType** (`string`) – creative type
- **creativeMime** (`string`) – creative MIME type
- **creativeSha1** (`string`) – SHA-1 checksum of creative content
- **creativeSize** (`string`) – space occupied by creative
- **name** (`string`) – creative name
- **status** (`integer`) – creative :ref:`status<creative-status>`
- **cdnUrl** (`string, null`) – creative content URL on CDN, may be `null` if was not uploaded to CDN
- **url** (`string`) – creative content URL

.. _creative-input-object:

CreativeInput object
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **name** (`string`) – name
- **creativeSize** (`string`) – occupied space. It should be the same as size returned during upload if was present
- **creativeType** (`string`) – type
- **url** (`string`) – (optional) temporary URL returned in response to :ref:`upload creative request<upload-creative>`. It is required for creative which needs to be uploaded, e.g. image
- **creativeContents** (`string`) – (optional) content. It is suggested for creative which does not use upload, e.g. direct links. By default content is campaign landing URL
