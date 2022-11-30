Impressions
===========

This API implements :ref:`the impressions sections of the Adshares protocol <impressions>`.

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

Find banners
------------

.. http:post:: /supply/find

    Finds banners that match the zones.

    :reqheader Accept: ``application/json``
    :resheader Content-Type: ``application/json``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 200: no error

    :<json object page: the page info
    :<json string page.iid: the impression ID
    :<json string page.url: the page URL
    :<json boolean, optional page.metamask: is the MetaMask enabled
    :<json array zones: list of zones info
    :<json string zones[].zoneId: the zone ID
    :<json string, optional zones[].types: list of accepted types
    :<json string, optional zones[].mimeTypes: list of accepted MIME types

    :>jsonarr string placementId: the banner ID
    :>jsonarr string zoneId: the zone ID
    :>jsonarr string publisherId: the publisher ID
    :>jsonarr string demandServer: the demand server account address
    :>jsonarr string supplyServer: the supply server account address
    :>jsonarr string type: the banner type: ``image``, ``video``, ``html``, ``model``
    :>jsonarr string scope: the banner scope (size)
    :>jsonarr string hash: checksum of the banner content
    :>jsonarr string serveUrl: URL to download the content of the banner
    :>jsonarr string viewUrl: view event URL
    :>jsonarr string clickUrl: click event URL
    :>jsonarr float rpm: average campaign's RPM

    **Example request**:

    .. sourcecode:: http

        POST /supply/find HTTP/1.1
        Host: app.example.com
        Accept: application/json
        Content-Type: application/json
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

        {
            "page": {
                "iid": "8ac04a70-886c-4d25-a8f8-10f1c5ed22f7",
                "url": "https://mysite.com"
            },
            "zones": [
                {
                    "zoneId": "2c81e9ed531b70c8ced43b19245aa3c3"
                }
            ]
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "placementId": "32a79fb61103aa3ef230d524cbd93e4f",
                "zoneId": "2c81e9ed531b70c8ced43b19245aa3c3",
                "publisherId": "d64bf2a15c5de2e33b20c4b6100c2d5d",
                "demandServer": "0001-00000001-8B4E",
                "supplyServer": "0001-00000002-BB2D",
                "type": "image",
                "scope": "300x250",
                "hash": "56436e1fdcb42f406760ccc9a4fe2e0519c36f46",
                "serveUrl": "https://app.example.com/serve/xed20914d13ed416ec91eb4be7b640a49.doc?v=67f4",
                "viewUrl": "https://app.example.com/l/n/view/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuZXhhbXBsZS5jb20vdmlldy9lZDIwOTE0ZDEzZWQ0MTZlYzkxZWI0YmU3YjY0MGE0OQ",
                "clickUrl": "https://app.example.com/l/n/click/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L3ZpZXcvZWM5MWViNGJlN2I2NDBhNDllZDIwOTQxNjE0ZDEzZWQ",
                "rpm": 2.13
            }
        ]

Dynamic find banners
--------------------

.. http:post:: /supply/find

    Finds banners that mach the query with automatic creation of users (if enabled) and zones.

    :reqheader Accept: ``application/json``
    :resheader Content-Type: ``application/json``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 200: no error

    :<json object page: the page info
    :<json string page.iid: the impression ID
    :<json string page.url: the page URL
    :<json string page.publisher: the publisher ID or account address (ADS or BSC)
    :<json string page.medium: the medium name
    :<json string, optional page.vendor: the vendor name
    :<json boolean, optional page.metamask: is the MetaMask enabled
    :<json array zones: list of zones info
    :<json string zones[].id: the request ID
    :<json string, optional zones[].name: name of the placement
    :<json string zones[].width: width of the placement
    :<json string zones[].height: height of the placement
    :<json string, optional zones[].depth: depth of the placement
    :<json string, optional zones[].minDpi: the minimum DPI
    :<json string, optional zones[].types: list of accepted types
    :<json string, optional zones[].mimeTypes: list of accepted MIME types

    :>jsonarr string id: the request ID
    :>jsonarr string placementId: the banner ID
    :>jsonarr string zoneId: the zone ID
    :>jsonarr string publisherId: the publisher ID
    :>jsonarr string demandServer: the demand server account address
    :>jsonarr string supplyServer: the supply server account address
    :>jsonarr string type: the banner type: ``image``, ``video``, ``html``, ``model``
    :>jsonarr string scope: the banner scope (size)
    :>jsonarr string hash: checksum of the banner content
    :>jsonarr string serveUrl: URL to download the content of the banner
    :>jsonarr string viewUrl: view event URL
    :>jsonarr string clickUrl: click event URL
    :>jsonarr float rpm: average campaign's RPM

    **Example request**:

    .. sourcecode:: http

        POST /supply/find HTTP/1.1
        Host: app.example.com
        Accept: application/json
        Content-Type: application/json
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

        {
            "page": {
                "iid": "8ac04a70-886c-4d25-a8f8-10f1c5ed22f7",
                "url": "https://mysite.com",
                "publisher": "ads:0001-00000000-9B6F"
                "medium": "metaverse",
                "vendor": "my-metaverse",
                "metamask": true
            },
            "zones": [
                {
                    "id": "1234",
                    "name": "Main gallery",
                    "width": 2.5,
                    "height": 4.75,
                    "minDpi": 10,
                    "types": [
                        "image",
                        "video"
                    ],
                    "mimeTypes": [
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

        [
            {
                "id": "1234",
                "placementId": "32a79fb61103aa3ef230d524cbd93e4f",
                "zoneId": "2c81e9ed531b70c8ced43b19245aa3c3",
                "publisherId": "d64bf2a15c5de2e33b20c4b6100c2d5d",
                "demandServer": "0001-00000001-8B4E",
                "supplyServer": "0001-00000002-BB2D",
                "type": "image",
                "scope": "300x250",
                "hash": "56436e1fdcb42f406760ccc9a4fe2e0519c36f46",
                "serveUrl": "https://app.example.com/serve/xed20914d13ed416ec91eb4be7b640a49.doc?v=67f4",
                "viewUrl": "https://app.example.com/l/n/view/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuZXhhbXBsZS5jb20vdmlldy9lZDIwOTE0ZDEzZWQ0MTZlYzkxZWI0YmU3YjY0MGE0OQ",
                "clickUrl": "https://app.example.com/l/n/click/32a79fb61103aa3ef230d524cbd93e4f?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L3ZpZXcvZWM5MWViNGJlN2I2NDBhNDllZDIwOTQxNjE0ZDEzZWQ",
                "rpm": 2.13
            }
        ]
