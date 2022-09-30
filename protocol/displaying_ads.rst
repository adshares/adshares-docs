
.. _displaying-ads:

Displaying ads
==============


Events flow
-----------

.. uml::

    skinparam defaultFontName "Segoe UI,Arial,sans-serif"
    skinparam shadowing false
    skinparam monochrome false

    actor       "Browser"           as browser
    participant "Supply AdServer"   as supplyServer
    participant "Supply AdUser"     as supplyUser
    participant "Demand AdServer"   as demandServer
    participant "Demand AdUser"     as demandUser
    actor       "Advertiser"        as advertiser

    == Initialization ==

    browser -> supplyServer : Register event
    supplyServer -> supplyUser : Register event (redirected)
    supplyUser --> browser: Return context scripts
    browser -> supplyUser: Send user's context

    == Displaying ==

    loop 30s
        browser -> supplyServer : Fetch banners
        supplyServer -> supplyUser : Get user's context
        supplyUser --> supplyServer : Return user's context
        supplyServer --> browser : Return banners

        loop for each banner
            browser -> demandServer : Get banner content
            demandServer --> browser : Return banner content

            browser -> supplyServer : View event
            supplyServer -> demandServer: View event (redirected)
            demandServer --> browser: Return register URL
            browser -> demandUser : Register event
            demandUser --> browser: Return context scripts
            browser -> demandUser: Send user's context
        end
    end

    == Clicking ==

    browser -> supplyServer : Click event
    supplyServer -> demandServer : Click event (redirected)
    demandServer -> advertiser : Click event (redirected)

    == Conversion ==

    advertiser -> demandServer : Conversion event
    demandServer --> supplyServer: Additional payment