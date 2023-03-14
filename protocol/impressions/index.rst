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

    ==User Navigates to a Site==

    SSA ->      SSP     : Post Register Event
    SSP ->      SSCP    : Post Register Event\n//redirected//

    ==User Browses Through a Site==

    SSA ->      SSP     : Get Creatives

    loop for each Creative
        SSA ->      DSP     : Get Creative Content
        SSA ->      SSP     : Post View Event
        SSP ->      SSCP    : Post View Event\n//redirected//
        SSA ->      DSP     : Post View Event
        DSP ->      DSCP    : Post View Event\n//redirected//
        SSA ->      DSP     : Post Register Event
        DSP ->      DSCP    : Post Register Event\n//redirected//
    end
    
    ==User Clicks on an Ad==

    SSA ->      SSP     : Post Click Event
    SSP ->      SSCP    : Post Click Event\n//redirected//
    SSA ->      DSP     : Post Click Event
    DSP ->      DSCP    : Post Click Event\n//redirected//

Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
