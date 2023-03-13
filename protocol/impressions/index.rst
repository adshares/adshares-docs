.. _protocol-impressions:

Impressions
===========

The following diagram presents a simplified overview of the interactions between 
:ref:`Supply-Side Infrastructure <protocol-ssi>` and :ref:`Demand-Side Infrastructure <protocol-dsi>`
regarding :ref:`Impression Events <protocol-definitions-impression>` and :ref:`Conversion Events <protocol-definitions-conversion>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"       as SSA
    participant "Supply-Side\nPlatform"    as SSP
    participant "SS Context\nPlatform"     as SSCP
    participant "Demand-Side\nPlatform"    as DSP
    participant "DS Context\nPlatform"     as DSCP
    participant "Demand-Side\nAgent"       as DSA

    ==User Navigates to a Site==

    SSA ->      SSP     : Send Register Event
    SSP ->      SSCP    : Register Event\n//redirected//
    SSCP -->    SSA     : Context Scripts

    ==User Browses Through a Site==

    SSA ->      SSP     : Find Creatives
    SSP ->      SSCP    : Get\nUser/Site/Device\nContext
    SSCP -->    SSP     : User/Site/Device\nContext
    SSP -->     SSA     : Creatives

    loop for each Creative
        SSA ->      DSP     : Get Creative Content
        DSP -->     SSA     : Creative Content
        SSA ->      SSP     : Send View Event
        SSP ->      DSP     : Send View Event\n//redirected//
        SSA ->      DSP     : Send Register Event
        DSP ->      DSCP    : Send Register Event\n//redirected//
        DSCP -->    SSA     : Context Scripts
    end
    
    ==User Clicks on an Ad==

    SSA ->      SSP     : Send Click Event
    SSP ->      DSP     : Send Click Event\n//redirected//
    DSP ->      DSA     : Send Click Event\n//redirected//


Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
