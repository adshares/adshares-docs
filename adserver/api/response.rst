Response
========

.. _response-pagination:

Errors
------

In case of an error (HTTP status code >= 400) the response contains information about the error (``error`` object).
Some errors may contain additional data (e.g. resource validation).

.. http:any:: /resource

    Return error info.

    :>json integer error.code: error code
    :>json string error.message: error message


Pagination
----------

All endpoints returning lists support pagination. The response is divided into 3 objects:
    - ``data`` - containing list of resources
    - ``links`` - containing pagination links
    - ``meta``- containing list's metadata

.. http:get:: /resource

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
