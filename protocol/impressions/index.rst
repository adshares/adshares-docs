.. _protocol-impressions:

Impressions
===========

The following diagram presents an overview of the interactions between 
:ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` and :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>`
regarding :ref:`Impression Events <protocol-definitions-impression>` and :ref:`Conversion Events <protocol-definitions-conversion>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nContext Platf"    as SSCP
    participant "Supply-Side\nAgent"            as SSA
    participant "Supply-Side\nPlatform"         as SSP
    participant "Demand-Side\nPlatform"         as DSP
    participant "Demand-Side\nAgent"            as DSA
    participant "Demand-Side\nContext Platf"    as DSCP

    ==User Navigates to a Site==

    SSA -> SSP : Register Event
    SSP -> SSCP : Register Event\n//redirected//
    SSCP --> SSA: Context Scripts
    SSA -> SSA: Execute\nContext Scripts
    SSA -> SSCP: Result of\nContext Scripts\n//optional//

    ==User Browses Through a Site==

    SSA -> SSP : Find Creatives
    SSP -> SSCP : Get Context
    SSCP --> SSP : User/Site/Device Context
    SSP --> SSA : Creatives

    loop for each Creative
        SSA -> DSP : Get Creative Content
        DSP --> SSA : Creative Content
        SSA -> SSP : View Event
        SSP -> DSP: View Event\n//redirected//
        DSP --> SSA: Demand-Side endpoint\nfor Register Event
        SSA -> DSP : Register Event
        DSP -> DSCP: Register Event\n//redirected//
        DSCP --> SSA: Context Scripts
        SSA -> SSA: Execute\nContext Scripts
        SSA -> DSCP: Result of\nContext Scripts\n//optional//
    end
    
    ==User Clicks on an Ad==

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
