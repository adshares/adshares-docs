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

Here are the general rules guiding the workflow around :ref:`Impression Events <protocol-definitions-impression>`:

* All :ref:`Impression Events <protocol-definitions-impression>` originate from :ref:`Supply-Side Agent <protocol-definitions-ssa>`,
  as this is the only entity able to observe the :ref:`User <protocol-definitions-user>` interacting with :ref:`Creatives <protocol-definitions-creative>`.
* Each :ref:`Impression Event <protocol-definitions-impression>` must be reported to both :ref:`Supply-Side Infrastructure <protocol-ssi>` 
  and :ref:`Demand-Side Infrastructure <protocol-dsi>`, so that they can stay in synch.
* Additionally, each :ref:`Impression Event <protocol-definitions-impression>` must be reported to both to 
  the :ref:`Context Platform <protocol-definitions-cp>` associated with :ref:`Supply-Side Infrastructure <protocol-ssi>` and
  the :ref:`Context Platform <protocol-definitions-cp>` associated with :ref:`Demand-Side Infrastructure <protocol-dsi>`.
* In case of :ref:`Register Event <protocol-definitions-registerevent>` and :ref:`View Event <protocol-definitions-viewevent>`,
  :ref:`Context Platform <protocol-definitions-cp>` returns a :ref:`Context Script <protocol-definitions-contextscript>`,
  and :ref:`Supply-Side Agent <protocol-definitions-ssa>` is expected to make an attempt to execute this script within its sandbox.

:ref:`Supply-Side Agent <protocol-definitions-ssa>` is free to report :ref:`Impression Events <protocol-definitions-impression>` to its 
:ref:`Supply-Side Platform <protocol-definitions-ssp>` in any way it wants, as this communication is not part of :ref:`Adshares Protocol <adshares-protocol>`.
However, regarding :ref:`Supply-Side Agent <protocol-definitions-ssa>` reporting :ref:`Impression Events <protocol-definitions-impression>` 
to :ref:`Demand-Side Platform <protocol-definitions-dsp>` the following rules apply:

* In case of :ref:`View Events <protocol-definitions-viewevent>` and :ref:`Click Events <protocol-definitions-clickevent>`, the endpoint for a notification call
  is contained in the :ref:`Creative Object <protocol-definitions-creativeobject>` payload.
* Whereas for :ref:`Register Events <protocol-definitions-registerevent>`, the endpoint for a notification call is contained in the response to the
  :ref:`View Event <protocol-definitions-viewevent>` notification call.

Regarding :ref:`Context Platform <protocol-definitions-cp>` returning :ref:`Context Scripts <protocol-definitions-contextscript>` to be executed by
:ref:`Supply-Side Agent <protocol-definitions-ssa>` within its sandbox the following rules apply:

* :ref:`Register Event <protocol-definitions-registerevent>` and :ref:`View Event <protocol-definitions-viewevent>` require 
  :ref:`Context Scripts <protocol-definitions-contextscript>` to be executed, thus :ref:`Context Platform <protocol-definitions-cp>` is expected to 
  return such a script in response to an event notification call.
* Whereas :ref:`Click Events <protocol-definitions-clickevent>` do not require :ref:`Context Scripts <protocol-definitions-contextscript>`, thus no script is 
  expected to be returned by :ref:`Context Platform <protocol-definitions-cp>` in response to a :ref:`Click Events <protocol-definitions-clickevent>` notification call.

Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
