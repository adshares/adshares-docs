.. _api-response-pagination:

Pagination
----------

All endpoints returning lists support pagination. The response is divided into 3 objects:
    - ``data`` - containing list of resources
    - ``links`` - containing pagination links
    - ``meta``- containing list's metadata

.. http:get:: /resources

    Return paginated resources.

    :query integer, optional limit: maximal number of entries per page
    :query integer, optional page: fetched page number
    :query string, optional cursor: paging cursor

    :>json array data: list of resources

    :>json string links.first: URL of first page
    :>json string links.last: URL of last page
    :>json string, null links.prev: URL of previous page, may be `null` if current page is first
    :>json string, null links.next: URL of next page, may be `null` if current page is last

    :>json string meta.path: URL of request
    :>json string meta.cursor: paging cursor
    :>json integer meta.total: total number of resources
    :>json integer meta.from: position of the first element on page
    :>json integer meta.to: position of the last element on page
    :>json integer meta.perPage: maximal number of resources on page
    :>json integer meta.currentPage: current page number
    :>json integer meta.lastPage: last page number

    **Example request**:

    .. sourcecode:: http

        GET /api/v2/resources?limit=10&page=2 HTTP/1.1
        Host: app.example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": ["..."],
            "links": {
                "first": "https://app.example.com/api/v2/resources?cursor=eyJpZCI6MzkzLCJfcG9pbnRzVG9OZXh0SXRlbXMiOnRydWV9&page=1",
                "last": "https://app.example.com/api/v2/resources?cursor=eyJpZCI6MzkzLCJfcG9pbnRzVG9OZXh0SXRlbXMiOnRydWV9&page=4",
                "prev": "https://app.example.com/api/v2/resources?cursor=eyJpZCI6MzkzLCJfcG9pbnRzVG9OZXh0SXRlbXMiOnRydWV9&page=1",
                "next": "https://app.example.com/api/v2/resources?cursor=eyJpZCI6MzkzLCJfcG9pbnRzVG9OZXh0SXRlbXMiOnRydWV9&page=3"
            },
            "meta": {
                "path": "https://app.example.com/api/v2/resources",
                "cursor": "eyJpZCI6MzkzLCJfcG9pbnRzVG9OZXh0SXRlbXMiOnRydWV9",
                "total": 35
                "from": 11,
                "to": 20,
                "perPage": 10,
                "currentPage": 2,
                "lastPage": 4,
            }
        }
