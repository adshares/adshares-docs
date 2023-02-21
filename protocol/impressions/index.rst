.. _protocol-impressions:

Impressions
===========

.. uml::
    :align: center

    skinparam monochrome true

    actor       "User"              as user
    participant "Supply AdServer"   as supplyServer
    participant "Supply AdUser"     as supplyUser
    participant "Demand AdServer"   as demandServer
    participant "Demand AdUser"     as demandUser
    actor       "Advertiser"        as advertiser

    ==Initialization==

    user -> supplyServer : Register event
    supplyServer -> supplyUser : Register event //redirected//
    supplyUser --> user: Return context scripts
    user -> supplyUser: Send user's context //optional//

    ==Displaying ads==

    loop periodically
        user -> supplyServer : Find creatives
        supplyServer -> supplyUser : Get user's context
        supplyUser --> supplyServer : Return user's context
        supplyServer --> user : Return creatives

        loop for each creative
            user -> demandServer : Get creative content
            demandServer --> user : Return creative content

            user -> supplyServer : View event
            supplyServer -> demandServer: View event //redirected//
            demandServer --> user: Return register URL
            user -> demandUser : Register event
            demandUser --> user: Return context scripts
            user -> demandUser: Send user's context //optional//
        end
    end

    ==Clicking==

    user -> supplyServer : Click event
    supplyServer -> demandServer : Click event //redirected//
    demandServer -> advertiser : Click event //redirected//
    advertiser --> demandServer: Click confirmation //optional//


Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
