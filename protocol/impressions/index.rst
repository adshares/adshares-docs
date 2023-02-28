.. _protocol-impressions:

Impressions
===========

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply Ctxt"      as SCP
    participant "Supply Agent"     as SSA
    participant "Supply Platf"     as SSP
    participant "Demand Platf"     as DSP
    participant "Demand Agent"     as DSA
    participant "Demand Ctxt"      as DCP

    ==User navigates to a Site==

    SSA -> SSP : Register Event
    SSP -> SCP : Register Event //redirected//
    SCP --> SSA: Context Scripts
    SSA -> SCP: Result of Context Scripts //optional//

    ==User browses through a Site==

    SSA -> SSP : Find Creatives
    SSP -> SCP : Get Context
    SCP --> SSP : User/Site/Device Context
    SSP --> SSA : Creatives

    loop for each Creative
        SSA -> DSP : Get Creative Content
        DSP --> SSA : Creative Content
        SSA -> SSP : View Event
        SSP -> DSP: View Event //redirected//
        DSP --> SSA: Endpoint for Register Event
        SSA -> DSP : Register Event
        DSP -> DCP: Register Event //redirected//
        DCP --> SSA: Context Scripts
        SSA -> DCP: Result of Context Scripts //optional//
    end
    
    ==User clicks on an ad==

    SSA -> SSP : Click Event
    SSP -> DSP : Click Event //redirected//
    DSP -> DSA : Click Event //redirected//
    DSA --> DSP: Click confirmation //optional//


Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
