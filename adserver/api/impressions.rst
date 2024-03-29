Impressions
===========

This API implements :ref:`the impressions sections of the Adshares protocol <protocol-impressions>`.

First, read about :ref:`error handling<api-response-errors>`.

Register
--------

.. http:get:: /supply/register

    Register user's context.

    The response will return scripts to run on the client side (optional).

    :query iid: the impression ID (unique, eg. `UUID v4 <https://www.rfc-editor.org/rfc/rfc4122.html>`_)
    :query stid: optional transaction ID seed (eg., internal user ID, wallet account address)
    :reqheader Accept: ``application/html``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 302: and then redirects to AdUser service
    :statuscode 200: no error

    **Example request**:

    .. sourcecode:: http

        GET /supply/register?iid=8ac04a70-886c-4d25-a8f8-10f1c5ed22f7 HTTP/1.1
        Host: app.example.com
        Accept: application/html
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: text/html; charset=UTF-8

        <!DOCTYPE html>
        <html lang="en">
        <head>
        </head>
        <body>
            <script type="text/javascript">
                parent.postMessage({"insertElem":[{"type": "iframe", "url": "https://au.example.com/fg/30b05fd441208ed758307bfd2e293b71/27b35445.html"}]}, "*");
            </script>
        </body>
        </html>

Find creatives
--------------

.. http:post:: /supply/find

    Finds creatives that fit the placements.

    :reqheader Accept: ``application/json``
    :resheader Content-Type: ``application/json``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 200: no error

    :<json object context: the :ref:`impression's context<api-impression-context>`
    :<json array placements: a list of :ref:`placement requests<api-placement-request>` with mandatory ``placementId`` attributes

    :>json Creative[] data: :ref:`creative list<api-creative-object>`. Creative and placement can be matched by the request ID. If response does not contain entry for request ID, AdServer does not have suitable creative.

    **Example request**:

    .. sourcecode:: http

        POST /supply/find HTTP/1.1
        Host: app.example.com
        Accept: application/json
        Content-Type: application/json
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

        {
            "context": {
                "iid": "8ac04a70-886c-4d25-a8f8-10f1c5ed22f7",
                "url": "https://mysite.com"
            },
            "placements": [
                {
                    "id": "1234",
                    "placementId": "2c81e9ed531b70c8ced43b19245aa3c3"
                }
            ]
        }

    .. _api-find-creatives-response:

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                {
                    "id": "1234",
                    "creativeId": "32a79fb61103aa3ef230d524cbd93e4f",
                    "placementId": "2c81e9ed531b70c8ced43b19245aa3c3",
                    "siteId": "ccc0c4b6109a4fe2ee2eb103a20c2d5d",
                    "publisherId": "d64bf2a15c5de2e33b20c4b6100c2d5d",
                    "demandServer": "0001-00000001-8B4E",
                    "supplyServer": "0001-00000002-BB2D",
                    "type": "image",
                    "mime": "image/png",
                    "scope": "300x250",
                    "hash": "56436e1fdcb42f406760ccc9a4fe2e0519c36f46",
                    "serveUrl": "https://app.example.com/serve/xed20914d13ed416ec91eb4be7b640a49.doc?v=67f4",
                    "viewUrl": "https://app.example.com/l/n/view/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuZXhhbXBsZS5jb20vdmlldy9lZDIwOTE0ZDEzZWQ0MTZlYzkxZWI0YmU3YjY0MGE0OQ",
                    "clickUrl": "https://app.example.com/l/n/click/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L3ZpZXcvZWM5MWViNGJlN2I2NDBhNDllZDIwOTQxNjE0ZDEzZWQ",
                    "rpm": 2.13
                }
            ]
        }

Dynamic find creatives
----------------------

.. http:post:: /supply/find

    Finds creatives that match the query with automatic creation of users (if enabled) and placements.

    :reqheader Accept: ``application/json``
    :resheader Content-Type: ``application/json``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 200: no error

    :<json object context: the :ref:`impression's context<api-impression-context>` with mandatory ``publisher``, ``medium`` and ``uid`` attributes
    :<json array placements: a list of :ref:`placement requests<api-placement-request>` with mandatory ``width``, and ``height`` attributes
    :>json Creative[] data: :ref:`creative list<api-creative-object>`. Creative and placement can be matched by the request ID. If response does not contain entry for request ID, AdServer does not have suitable creative.

    **Example request**:

    .. sourcecode:: http

        POST /supply/find HTTP/1.1
        Host: app.example.com
        Accept: application/json
        Content-Type: application/json
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

        {
            "context": {
                "iid": "8ac04a70-886c-4d25-a8f8-10f1c5ed22f7",
                "url": "https://mysite.com",
                "publisher": "ads:0001-00000000-9B6F"
                "medium": "metaverse",
                "vendor": "my-metaverse",
                "uid": "0x2dc37ed4780c5b826d8D71f629581791F9f36e7a",
                "metamask": true
            },
            "placements": [
                {
                    "id": "1234",
                    "name": "Main gallery",
                    "width": 300,
                    "height": 225,
                    "types": [
                        "image",
                        "video"
                    ],
                    "mimes": [
                        "image/jpeg",
                        "image/png",
                        "video/mp4"
                    ],
                }
            ]
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                {
                    "id": "1234",
                    "creativeId": "32a79fb61103aa3ef230d524cbd93e4f",
                    "placementId": "2c81e9ed531b70c8ced43b19245aa3c3",
                    "siteId": "ccc0c4b6109a4fe2ee2eb103a20c2d5d",
                    "publisherId": "d64bf2a15c5de2e33b20c4b6100c2d5d",
                    "demandServer": "0001-00000001-8B4E",
                    "supplyServer": "0001-00000002-BB2D",
                    "type": "image",
                    "mime": "image/png",
                    "scope": "300x250",
                    "hash": "56436e1fdcb42f406760ccc9a4fe2e0519c36f46",
                    "serveUrl": "https://app.example.com/serve/xed20914d13ed416ec91eb4be7b640a49.doc?v=67f4",
                    "viewUrl": "https://app.example.com/l/n/view/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuZXhhbXBsZS5jb20vdmlldy9lZDIwOTE0ZDEzZWQ0MTZlYzkxZWI0YmU3YjY0MGE0OQ",
                    "clickUrl": "https://app.example.com/l/n/click/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L3ZpZXcvZWM5MWViNGJlN2I2NDBhNDllZDIwOTQxNjE0ZDEzZWQ",
                    "rpm": 2.13
                }
            ]
        }


Data structures
---------------

.. _api-impression-context:

Impression context object
^^^^^^^^^^^^^^^^^^^^^^^^^

- **iid** (*string*) - the impression ID
- **publisher** (*string*) - (optional) the publisher ID or account address (ADS or BSC)
- **url** (*string*) - the site URL
- **medium** (*string*) - (optional) the site :ref:`medium<taxonomy-media>`
- **vendor** (*string*) - (optional) the site :ref:`vendor<taxonomy-media>`
- **uid** (*string*) - (optional) the user ID (eg. a wallet address)
- **metamask** (*boolean*) - (optional) is the MetaMask enabled

.. _api-placement-request:

Placement request object
^^^^^^^^^^^^^^^^^^^^^^^^

- **id** (*string*) - the request ID
- **placementId** (*string*) - the placement ID (omit if ``width`` and ``height`` are provided)
- **name** (*string*) - (optional) name of the placement
- **width** (*int*) - width of the placement (omit if ``placementId`` is provided)
- **height** (*int*) - height of the placement (omit if ``placementId`` is provided)
- **depth** (*int*) - (optional) depth of the placement
- **types** (*string[]*) - (optional) a list of accepted :ref:`types<taxonomy-formats>`
- **mimes** (*string[]*) - (optional) a list of accepted :ref:`MIME types<taxonomy-formats>`
- **topframe** (*boolean*) - (optional) indicates if placement is in the top frame (`true`) as opposed to an iframe (false)

.. _api-creative-object:

Creative object
^^^^^^^^^^^^^^^

- **id** (*string*) – the request ID
- **creativeId** (*string*) – the creative ID
- **placementId** (*string*) – the placement ID
- **siteId** (*string*) – the site ID
- **publisherId** (*string*) – the publisher ID
- **demandServer** (*string*) – the demand server account address
- **supplyServer** (*string*) – the supply server account address
- **type** (*string*) – the :ref:`creative type<taxonomy-formats>`.
- **mime** (*string*) – the :ref:`creative MIME type<taxonomy-formats>`.
- **scope** (*string*) – the :ref:`creative scope<taxonomy-scopes>` (size).
- **hash** (*string*) – checksum of the creative content
- **serveUrl** (*string*) – URL to download the content of the creative
- **viewUrl** (*string*) – view event URL
- **clickUrl** (*string*) - click event URL
- **rpm** (*float*) – average campaign's RPM
