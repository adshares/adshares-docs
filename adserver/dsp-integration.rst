
.. _adserver-dsp-integration:

DSP integration (experimental)
==============================

.. warning::
   This functionality is under development.
   Documentation can change at any time without notice.

AdServer (the supply part) can integrate with an external DSP (Demand Side Platform).
An external DSP should be understood as DSP outside the Adshares ecosystem.

This article describes interface which is required to assure communication between AdServer and external DSP.
Later in article an external DSP will be referred as Bridge, because typical solution is to prepare a bridge between AdServer and existing DSP.

General assumptions
----------------------------

- Payments are credited by AdServer's operator. Bridge can be trusted and credited payments will be paid by bridge. *This can be changed to "Payments are credited by Bridge" when Bridge will support payments on ADS blockchain*
- Bridge is a service accessible by HTTP protocol on localhost. It does not expose any public endpoint

AdServer configuration requirements
------------------------------------

AdServer configuration requires:
- Bridge's URL address
- Bridge's Adshares account address

Bridge inventory
-------------------

Bridge should expose its inventory on ``/inventory`` endpoint.
The inventory format must comply with :ref:`standard format<inventory_response_format>`.

Bridge events
--------------------

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"      as SSA
    participant "SS Context\nPlatform"    as SSCP
    participant "Supply-Side\nPlatform"   as SSP
    participant "Bridge"                  as B
    participant "External DSP"            as EDSP
    participant "DS Context\nPlatform"    as DSCP
    participant "DS\nAgent"               as DSA

    ==User Browses Through a Site==

    SSA ->   SSP  : Find Creatives
    SSP ->   SSCP : Get\nUser/Site/Device\nContext
    SSCP --> SSP  : User/Site/Device\nContext
    SSP ->   SSP  : Select best\nCreatives

    SSP  ->  B    : Get Creatives
    B    ->  EDSP : Find Creatives
    EDSP --> B    : Creatives
    B    --> SSP  : Creatives
    SSP  --> SSA  : Creatives

    loop for each Creative
        SSA  ->  EDSP : Get Creative Content
        EDSP --> SSA  : Creative Content
        SSA  -> SSP   : View Event
        SSP  -> B     : View Event\n//BE call//
        
        alt Redirection
            B    --> SSP  : Redirect\nView Event
            SSP  ->  EDSP : View Event\n//redirected//
            SSA  ->  EDSP : Register Event
            EDSP ->  DSCP : Register Event\n//redirected//
            DSCP --> SSA  : Context Scripts
        else BE confirmation
            B   ->  EDSP : View Event\nwith Context
            B   --> SSP  : View Event\nconsumed
            SSP --> SSA  : Pixel
        end

    end
    
    ==User Clicks on an Ad==

    SSA  ->  SSP  : Click Event
    SSP  ->  B    : Click Event\n//BE call//
    B    --> SSP  : Redirect Click Event
    SSP  ->  EDSP : Click Event\n//redirected//
    EDSP ->  DSA  : Click Event\n//redirected//


Bridge payments
-------------------

Bridge should expose payments' details on ``/payments-details`` endpoint.
