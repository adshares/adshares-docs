Taxonomy
========

This API is based on :ref:`the taxonomy sections of the Adshares protocol <taxonomy>`.

First, read about :ref:`authorization<api-authorization>` and :ref:`error handling<api-response-errors>`.

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

    :>json Taxonomy data: :ref:`taxonomy<api-taxonomy-object>`

Data structures
---------------


.. _api-taxonomy-object:

Taxonomy object
^^^^^^^^^^^^^^^

- **name** (*string*) – :ref:`medium<taxonomy-media>` name
- **label** (*string*) – :ref:`medium<taxonomy-media>` label
- **vendor** (*string*) – :ref:`vendor<taxonomy-media>` name
- **vendorLabel** (*string*) – :ref:`vendor<taxonomy-media>` label
- **formats[].type** (*string*) – :ref:`format type<taxonomy-formats>`
- **formats[].mimes** (*string[]*) – :ref:`MIME types<taxonomy-formats>`
- **formats[].scopes** (*object*) – map of :ref:`scopes<taxonomy-scopes>`. Key is the scope. Value is a label
- **targeting.user** (*TargetingOption[]*) – (optional) user targeting options
- **targeting.site** (*TargetingOption[]*) – (optional) site targeting options
- **targeting.device** (*TargetingOption[]*) – (optional) device targeting options
