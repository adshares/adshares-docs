Authorization
===================

AdServer authorizes API users with JWT access token.
Access token is generated according to OAuth2.
AdServer has a built-in OAuth2 server thanks to `Laravel Passport <https://laravel.com/docs/passport>`_.

AdServer supports three methods of acquiring an access token:

- ``personal access token`` - for users which want to interact directly with API, prepare machine access, e.g. third party integrations
- ``authorization code grant`` - for server applications with user interaction, e.g. AdController
- ``client credentials grant`` - for machine access, e.g. maintenance


Personal Access Token
--------------------------

Personal Access Token can be used by user to directly interact with API.
Token can be generated in AdPanel by authenticated user.

To create a token:

#. Log in to AdPanel
#. Go to **Account Settings** page
#. Scroll down to **Access tokens** section
#. Input name. Name is only for your convenience
#. Select scopes. Good practice is to choose as few privileges as needed
#. Click [Create] button
#. Copy displayed access token

Token is long-lived, but can be revoked in case of compromise.
To revoke a token go to **Account tokens** section and click [Delete] button.


Authorization code grant
--------------------------

Below is the sample flow in which AdController is the client server.
This flow is divided into sections but represents single authentication process.
Diagram could be simplified when user interacts with AdPanel and is still logged in.
In this situation user does not have to log in once again.

.. uml::
    :align: center

    skinparam monochrome true

    actor       "User"         as user
    participant "AdController" as adcontroller
    participant "AdPanel"      as adpanel
    participant "AdServer"     as adserver

    ==Fetch data (no token)==
    user -> adcontroller: Open page
    adcontroller -> adserver: Fetch data
    adserver -> adcontroller: Unauthenticated 401
    ==Fetch code==
    adcontroller -> adserver: Fetch code
    adserver -> adpanel: Display log in form
    adpanel -> user: Log in form
    user -> adpanel: Log in credentials
    adpanel -> adserver: Log in
    adserver -> adpanel: Do redirect
    adpanel -> adserver: Redirect
    adserver -> adcontroller: Code

    ==Fetch access token==
    adcontroller -> adserver: Fetch token
    adserver -> adcontroller: Token
    ==Fetch data (token)==
    adcontroller -> adserver: Fetch data
    adserver -> adcontroller: Data
    adcontroller -> user: Display page

.. http:post:: /auth/login

    Logs user in to the AdServer. Returns API token.

    :statuscode 200: no error
    :statuscode 422: invalid credentials

    :<json string email: user's e-mail
    :<json string password: user's password

    :>json string apiToken: API token

    **Example response**:

    .. sourcecode::

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            ...
            "apiToken": "WQQ6KU37jqgsnamUhkMRzpMmyY44C8c4db7i7HFeRC5xJQTNaVtrWRaH8YxQ",
            ...
        }


.. http:get:: /auth/authorize

    Generates authorization code.

    :reqheader Authorization: authorization header should contain API token ``Bearer <API_TOKEN>``

    :statuscode 200: no error, code in response body
    :statuscode 302: no error, redirection to callback URI
    :statuscode 422: error

    :query client_id: **CLIENT_ID**
    :query no_redirect: (optional) if present server will return code in body, default action is redirection to callback URI
    :query redirect_uri: code callback URI
    :query response_type: (constant) ``code``
    :query scope: (optional) a space delimited list of scopes
    :query state: (optional) CSRF token, will be returned in callback

    :>json string location: callback URI (containing code in query). Present if `no_redirect` param was set

    **Example response if no_redirect param is present**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "location": "https://example.com/callback?code=349834jbgtbgbdsd&state=3WJPbImynfEzj34ggMOD7%27hsXrT6Tbjl"
        }

.. http:post:: /oauth/token

    Acquires access token.

    :statuscode 200: no error
    :statuscode 422: error

    :<json string client_id: **CLIENT_ID**
    :<json string client_secret: **CLIENT_SERVER**
    :<json string code: authorization code from previous request
    :<json constant, string grant_type: ``authorization_code``
    :<json string redirect_uri: code callback URI, must match previous request

    :>json constant, string token_type: "Bearer"
    :>json integer expires_in: token TTL in seconds
    :>json string access_token: token
    :>json string refresh_token: refresh token

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "token_type": "Bearer",
            "expires_in": 31536000,
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJtZXNzYWdlIjogIkJlZXIgYW5kIGNoZWVzZSBteSBmcmllbmQifQ.A2lO5mO7R8LLAKAXNvmAsVAPOJBc",
            "refresh_token": "d936cc8586ead4b5"
        }


Client credentials grant
--------------------------

This flow consist of single request for token.

.. http:post:: /oauth/token

    Acquires access token.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 422: error

    :<json constant, string grant_type: (constant) ``client_credentials``
    :<json string client_id: **CLIENT_ID**
    :<json string client_secret: **CLIENT_SERVER**
    :<json string scope: (optional) a space delimited list of token's scopes

    :>json constant, string token_type: "Bearer"
    :>json integer expires_in: token TTL in seconds
    :>json string access_token: token

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "token_type": "Bearer",
            "expires_in": 31536000,
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJtZXNzYWdlIjogIkJlZXIgYW5kIGNoZWVzZSBteSBmcmllbmQifQ.A2lO5mO7R8LLAKAXNvmAsVAPOJBc"
        }
