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

General rules
-------------

* All :ref:`Impression Events <protocol-definitions-impression>` originate from :ref:`Supply-Side Agent <protocol-definitions-ssa>`,
  as this is the only entity able to observe the :ref:`User <protocol-definitions-user>` interactacting with :ref:`Creatives <protocol-definitions-creative>`.
* Each :ref:`Impression Event <protocol-definitions-impression>` must be reported to both :ref:`Supply-Side Infrastructure <protocol-ssi>` 
  and :ref:`Demand-Side Infrastructure <protocol-dsi>`, so that they can stay in synch.
* Additionally, each :ref:`Impression Event <protocol-definitions-impression>` must be reported to both to 
  the :ref:`Context Platform <protocol-definitions-cp>` associated with :ref:`Supply-Side Infrastructure <protocol-ssi>` and
  the :ref:`Context Platform <protocol-definitions-cp>` associated with :ref:`Demand-Side Infrastructure <protocol-dsi>`.
* In case of :ref:`Register Event <protocol-definitions-registerevent>` and :ref:`View Event <protocol-definitions-viewevent>`,
  :ref:`Context Platform <protocol-definitions-cp>` returns a :ref:`Context Script <protocol-definitions-contextscript>`,
  and :ref:`Supply-Side Agent <protocol-definitions-ssa>` is expected to make an attempt to execute this script within its sandbox.

Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
