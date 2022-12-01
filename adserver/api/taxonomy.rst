Taxonomy
========

Media
-----

.. http:get:: /api/v2/taxonomy/media

    Fetch supported media.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json object data: map of supported media. Key is medium ID. Value is medium name

Vendors
-------

.. http:get:: /api/v2/taxonomy/media/(medium)/vendors

    Fetch supported vendors by medium.

    :param medium: medium ID

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json object data: map of supported vendors. Key is vendor ID. Value is vendor name

Taxonomy by medium
------------------

.. http:get:: /api/v2/taxonomy/media/(medium)

    Fetch taxonomy for medium.

    :param medium: medium ID
    :query vendor: (optional) vendor ID. If omitted, default vendor will be returned

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json Taxonomy data: :ref:`taxonomy<taxonomy-object>`

Data structures
---------------

.. _taxonomy-object:

Taxonomy object
^^^^^^^^^^^^^^^

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
