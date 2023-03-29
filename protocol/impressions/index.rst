.. _protocol-impressions:

Impressions
===========

The following diagram presents a simplified overview of the interactions between 
:ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
regarding :ref:`Impression Events <protocol-definitions-impression>` and :ref:`Conversion Events <protocol-definitions-conversion>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"                as SSA
    participant "Supply-Side\nPlatform"             as SSP
    participant "Supply-Side\nContext Provider"     as SSCP
    participant "Demand-Side\nPlatform"             as DSP
    participant "Demand-Side\nContext Provider"     as DSCP
    participant "Demand-Side\nAgent"                as DSA

    ==User Navigates to a Site==

    SSA ->      SSP     : Post Register Event
    SSA ->      SSCP    : Post Register Event

    ==User Browses Through a Site==

    SSA ->      SSP     : Get Creatives

    loop for each Creative
        SSA ->      DSP     : Get Creative Content
        SSA ->      DSP     : Post View Event
        SSA ->      DSCP    : Post Register Event
    end
    
    ==User Clicks on an Ad==

    SSA ->      SSP     : Post Click Event
    SSP ->      DSP     : Post Click Event\n//redirected//
    DSP ->      DSA     : Post Click Event\n//redirected//

General rules
-------------

Here are general rules guiding the workflow around :ref:`Impression Events <protocol-definitions-impression>`:

* All :ref:`Impression Events <protocol-definitions-impression>` originate from :ref:`Supply-Side Agent <protocol-definitions-ssa>`,
  as this is the only entity able to observe the :ref:`User <protocol-definitions-user>` interacting with :ref:`Creatives <protocol-definitions-creative>` 
  within the :ref:`Site <protocol-definitions-site>`.
* All :ref:`Conversion Events <protocol-definitions-conversion>` originate from :ref:`Demand-Side Agent <protocol-definitions-dsa>`,
  as this is the only entity able to observe the :ref:`User <protocol-definitions-user>` performing actions within the :ref:`Target <protocol-definitions-target>`.
* Each :ref:`Impression Event <protocol-definitions-impression>` must be reported to both :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  and :ref:`Demand-Side Platform <protocol-definitions-dsp>`, so that they can stay in synch.
* Additionally, each :ref:`Register Event <protocol-definitions-registerevent>` must be reported to both to 
  the :ref:`Context Provider <protocol-definitions-cp>` associated with :ref:`Supply-Side Platform <protocol-definitions-ssp>` and
  the :ref:`Context Provider <protocol-definitions-cp>` associated with :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
* In case of :ref:`Register Events <protocol-definitions-registerevent>`, :ref:`Context Provider <protocol-definitions-cp>` returns
  a :ref:`Context Script <protocol-definitions-contextscript>`, and :ref:`Supply-Side Agent <protocol-definitions-ssa>` is expected 
  to make an attempt to execute this script within its sandbox.

:ref:`Supply-Side Agent <protocol-definitions-ssa>` is free to report :ref:`Impression Events <protocol-definitions-impression>` to its 
:ref:`Supply-Side Platform <protocol-definitions-ssp>` in any way it wants, as this communication is not part of :ref:`Adshares Protocol <adshares-protocol>`.
However, reporting :ref:`Impression Events <protocol-definitions-impression>` to :ref:`Demand-Side Platform <protocol-definitions-dsp>` is based on the following rules:

* In case of :ref:`View Events <protocol-definitions-viewevent>` and :ref:`Click Events <protocol-definitions-clickevent>`, the endpoint for notification calls
  is contained in the :ref:`Creative Object <protocol-definitions-creativeobject>` payload.
* Whereas for :ref:`Register Events <protocol-definitions-registerevent>`, the endpoint for notification calls is contained in the 
  :ref:`Context Scripts <protocol-definitions-contextscript>` returned in response to the :ref:`View Event <protocol-definitions-viewevent>` notification call.

Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
