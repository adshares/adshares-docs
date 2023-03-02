.. _protocol-impressions:

Impressions
===========

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply\nContext"      as SCP
    participant "Supply\nAgent"        as SSA
    participant "Supply\nPlatform"     as SSP
    participant "Demand\nPlatform"     as DSP
    participant "Demand\nAgent"        as DSA
    participant "Demand\nContext"      as DCP

    ==User navigates to a Site==

    SSA -> SSP : Register Event
    SSP -> SCP : Register Event\n//redirected//
    SCP --> SSA: Context Scripts
    SSA -> SCP: Result of\nContext Scripts\n//optional//

    ==User browses through a Site==

    SSA -> SSP : Find Creatives
    SSP -> SCP : Get Context
    SCP --> SSP : User/Site/Device Context
    SSP --> SSA : Creatives

    loop for each Creative
        SSA -> DSP : Get Creative Content
        DSP --> SSA : Creative Content
        SSA -> SSP : View Event
        SSP -> DSP: View Event\n//redirected//
        DSP --> SSA: Endpoint for\nRegister Event
        SSA -> DSP : Register Event
        DSP -> DCP: Register Event\n//redirected//
        DCP --> SSA: Context Scripts
        SSA -> DCP: Result of\nContext Scripts\n//optional//
    end
    
    ==User clicks on an ad==

    SSA -> SSP : Click Event
    SSP -> DSP : Click Event\n//redirected//
    DSP -> DSA : Click Event\n//redirected//
    DSA --> DSP: Click confirmation\n//optional//


Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
