Response
===========

Pagination
--------------------------

All endpoints returning lists support pagination.
Below are enlisted all fields related to pagination.

.. http:get:: /resource

    Return paginated resources.

    :>json integer currentPage: number of current page
    :>json array data: array of resources
    :>json string firstPageUrl: URL of first page
    :>json integer from: number of first element on page
    :>json integer lastPage: number of last page
    :>json string lastPageUrl: URL of last page
    :>json string path: URL of request
    :>json integer perPage: maximal number of resources on page
    :>json string cursor: cursor
    :>json string, null nextPageUrl: URL of next page, may be `null` if current page is last
    :>json string, null prevPageUrl: URL of previous page, may be `null` if current page is first
    :>json integer to: number of last element on page
    :>json integer total: total number of resources
