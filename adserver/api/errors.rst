.. _api-response-errors:

Error responses
===============

In case of an error (HTTP status code >= 400) the response contains information about the error (``error`` object).
Some errors may contain additional data (e.g. resource validation).

.. http:any:: /resource

    Return error info.

    :>json integer error.code: error code
    :>json string error.message: error message

    **Example request**:

    .. sourcecode:: http

        GET /api/v2/resources/dummy HTTP/1.1
        Host: app.example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 404 Not Found
        Content-Type: application/json

        {
            "error": {
                "code": 404,
                "message": "Cannot find dummy resource"
            }
        }
