Impressions
===========

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

    The posts tagged with `tag` that the user (`user_id`) wrote.

    :reqheader Accept: ``application/json``
    :resheader Content-Type: ``application/json``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 200: no error

    :<json object page: the page info
    :<json string page.iid: the impression ID
    :<json string page.url: the page URL
    :<json boolean, optional page.metamask: is the MetaMask enabled
    :<json array zones: list of zones info
    :<json string zones[].id: the zone ID

    :>jsonarr string id: the banner ID
    :>jsonarr string publisher_id: the publisher ID
    :>jsonarr string zone_id: the zone ID
    :>jsonarr string pay_from: the demand server account address
    :>jsonarr string pay_to: the supply server account address
    :>jsonarr string type: the banner type: ``image``, ``video``, ``html``, ``model``
    :>jsonarr string size: the banner size
    :>jsonarr string serve_url: URL to download the content of the banner
    :>jsonarr string creative_sha1: checksum of the banner content
    :>jsonarr string click_url: click event URL
    :>jsonarr string view_url: view event URL
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
                    "id": "45aa32c81e9d43b19ed531b70c8ce2c3"
                }
            ]
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": "3aa3ef230d524f32a79fb4cbd93e6110",
                "publisher_id": "2e33b20c4bd64bf2a15c5de6100c2d5d",
                "zone_id": "45aa32c81e9d43b19ed531b70c8ce2c3",
                "pay_from": "0001-00000028-3E05",
                "pay_to": "0001-00000050-C19A",
                "type": "image",
                "size": "300x250",
                "serve_url": "https://app.example.com/serve/xec91eb4be7b640a49ed20941614d13ed.doc?v=42f4",
                "creative_sha1": "42f406760ccc9a4fe2e0519c56436e1fdcb36f46",
                "click_url": "https://app.example.com/l/n/click/3aa3ef230d524f32a79fb4cbd93e6110?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L2NsaWNrL2VjOTFlYjRiZTdiNjQwYTQ5ZWQyMDk0MTYxNGQxM2Vk",
                "view_url": "https://app.example.com/l/n/view/3aa3ef230d524f32a79fb4cbd93e6110?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L3ZpZXcvZWM5MWViNGJlN2I2NDBhNDllZDIwOTQxNjE0ZDEzZWQ",
                "rpm": 2.13
            }
        ]

Dynamic find banners
--------------------

.. http:post:: /supply/find

    The posts tagged with `tag` that the user (`user_id`) wrote.

    :reqheader Accept: ``application/json``
    :resheader Content-Type: ``application/json``
    :reqheader User-Agent: the user agent originating the request
    :statuscode 200: no error

    :<json object page: the page info
    :<json string page.iid: the impression ID
    :<json string page.url: the page URL
    :<json boolean, optional page.metamask: is the MetaMask enabled
    :<json array zones: list of zones info
    :<json string zones[].pay_to: the publisher account address
    :<json string, optional zones[].medium: the medium name
    :<json string, optional zones[].vendor: the vendor name
    :<json string zones[].width: width of the placement
    :<json string zones[].height: height of the placement
    :<json string, optional zones[].depth: depth of the placement
    :<json string, optional zones[].min_dpi: the minimum DPI
    :<json string, optional zones[].type: list of accepted types
    :<json string, optional zones[].mime_type: list of accepted MIME types

    :>jsonarr string id: the banner ID
    :>jsonarr string publisher_id: the publisher ID
    :>jsonarr string zone_id: the zone ID
    :>jsonarr string pay_from: the demand server account address
    :>jsonarr string pay_to: the supply server account address
    :>jsonarr string type: the banner type: ``image``, ``video``, ``html``, ``model``
    :>jsonarr string size: the banner size
    :>jsonarr string serve_url: URL to download the content of the banner
    :>jsonarr string creative_sha1: checksum of the banner content
    :>jsonarr string click_url: click event URL
    :>jsonarr string view_url: view event URL
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
                "metamask": true
            },
            "zones": [
                {
                    "pay_to": "ads:0001-00000000-9B6F"
                    "medium": "metaverse",
                    "vendor": "my-metaverse",
                    "name": "Main gallery",
                    "width": 2.5,
                    "height": 4.75,
                    "min_dpi": 10,
                    "type": [
                        "image",
                        "video"
                    ],
                    "mime_type": [
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
                "id": "3aa3ef230d524f32a79fb4cbd93e6110",
                "publisher_id": "2e33b20c4bd64bf2a15c5de6100c2d5d",
                "zone_id": "45aa32c81e9d43b19ed531b70c8ce2c3",
                "pay_from": "0001-00000028-3E05",
                "pay_to": "0001-00000050-C19A",
                "type": "image",
                "size": "300x250",
                "serve_url": "https://app.example.com/serve/xec91eb4be7b640a49ed20941614d13ed.doc?v=42f4",
                "creative_sha1": "42f406760ccc9a4fe2e0519c56436e1fdcb36f46",
                "click_url": "https://app.example.com/l/n/click/3aa3ef230d524f32a79fb4cbd93e6110?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L2NsaWNrL2VjOTFlYjRiZTdiNjQwYTQ5ZWQyMDk0MTYxNGQxM2Vk",
                "view_url": "https://app.example.com/l/n/view/3aa3ef230d524f32a79fb4cbd93e6110?r=aHR0cHM6Ly9hcHAuYWRhcm91bmQubmV0L3ZpZXcvZWM5MWViNGJlN2I2NDBhNDllZDIwOTQxNjE0ZDEzZWQ",
                "rpm": 2.13
            }
        ]