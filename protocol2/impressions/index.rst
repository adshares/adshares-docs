Impressions
===========

.. _protocol-impressions:

User navigates to Site
----------------------

The following process takes place when a :ref:`User <protocol-definitions-user>` initially navigates to a :ref:`Site <protocol-definitions-site>`.

* :ref:`SSA <protocol-definitions-ssa>` notifies :ref:`SSP <protocol-definitions-ssp>` about a :ref:`Register Event <protocol-definitions-registerevent>`.
* In response to the event notification call, :ref:`SSP <protocol-definitions-ssp>` returns an endpoint of its trusted instances of :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>`.
* Using the above endpoint, :ref:`SSA <protocol-definitions-ssa>` notifies :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` about a :ref:`Register Event <protocol-definitions-registerevent>`.
* In response to the event notification call, :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` returns :ref:`Context Scripts <protocol-definitions-contextscript>`, and :ref:`SSA <protocol-definitions-ssa>` makes an attempt to execute those scripts.

User browses through Site
-------------------------

The following process takes place when a :ref:`User <protocol-definitions-user>` browses through a :ref:`Site <protocol-definitions-site>`.

Loop1: invoked periodically
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This loop ensures that :ref:`Creatives <protocol-definitions-creative>` are swapped periodically within the same :ref:`Placement <protocol-definitions-placement>`. The goal is to maximize utilization of :ref:`Placements <protocol-definitions-placement>` by displaying multiple :ref:`Creatives <protocol-definitions-creative>` sequentially to the same :ref:`User <protocol-definitions-user>`.

* :ref:`SSA <protocol-definitions-ssa>` calls :ref:`SSP <protocol-definitions-ssp>` to get a list of :ref:`Creatives <protocol-definitions-creative>` to be displayed in a given time interval across all available :ref:`Placements <protocol-definitions-placement>`.
* Before generating the requested list of :ref:`Creatives <protocol-definitions-creative>`, :ref:`SSP <protocol-definitions-ssp>` calls :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` to retrieve :ref:`Context Data <protocol-definitions-contextdata>`.
* :ref:`SSA <protocol-definitions-ssa>` receives a list of metadata for :ref:`Creatives <protocol-definitions-creative>`. Among other things, each item in the list contains three :ref:`DSP <protocol-definitions-dsp>` endpoints:
    * an endpoint for retrieving :ref:`Creative Content <protocol-definitions-creativecontent>`,
    * an endpoint for notifying that a :ref:`View Event <protocol-definitions-viewevent>` has occurred,
    * an endpoint for notifying that a :ref:`Click Event <protocol-definitions-clickevent>` has occurred.

.. note::
    Each :ref:`Creative <protocol-definitions-creative>` in the list can be associated with a unique :ref:`DSP <protocol-definitions-dsp>`. This implies that :ref:`Creatives <protocol-definitions-creative>` managed by various :ref:`DSPs <protocol-definitions-dsp>` can be displayed next to each other within the same :ref:`Site <protocol-definitions-site>`.

.. note::
    At this stage, the metadata for all :ref:`Creatives <protocol-definitions-creative>` is already retrieved, but none of them is rendered yet, as :ref:`SSA <protocol-definitions-ssa>` does not have :ref:`Creative Content <protocol-definitions-creativecontent>` - this will be done in the subsequent step.

.. note::
    This part of the process is based on information cached in :ref:`SSP <protocol-definitions-ssp>`, without engaging any :ref:`DSP <protocol-definitions-dsp>`. This is possible due to the fact that :ref:`SSP <protocol-definitions-ssp>` “knows” the currently available :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`, as this information has already been retrieved during the synchronization stage.

Loop2: invoked for each Creative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This loop ensures that each :ref:`Creative Content <protocol-definitions-creativecontent>` is displayed in the appropriate :ref:`Placement <protocol-definitions-placement>`, and both :ref:`SSP <protocol-definitions-ssp>` and :ref:`DSP <protocol-definitions-dsp>` are simultaneously notified about this fact, so that their states remain synchronized. The following loop runs for each :ref:`Creative <protocol-definitions-creative>` within *Loop1*.

* Using the endpoint contained in the metadata, :ref:`SSA <protocol-definitions-ssa>` calls :ref:`DSP <protocol-definitions-dsp>` to retrieve :ref:`Creative Content <protocol-definitions-creativecontent>`.
* SSA receives the requested :ref:`Creative Content <protocol-definitions-creativecontent>`, but before a :ref:`Creative <protocol-definitions-creative>` is actually rendered, :ref:`SSA <protocol-definitions-ssa>` compares the hash of the received :ref:`Creative Content <protocol-definitions-creativecontent>` with the hash contained in the metadata - to ensure that the :ref:`Creative Content <protocol-definitions-creativecontent>` matches what was initially approved when the :ref:`Campaign <protocol-definitions-campaign>` was launched.
* Assuming the above hashes match, :ref:`SSA <protocol-definitions-ssa>` renders the :ref:`Creative <protocol-definitions-creative>` on the screen, so that the :ref:`User <protocol-definitions-user>` can see it.
* :ref:`SSA <protocol-definitions-ssa>` notifies :ref:`SSP <protocol-definitions-ssp>` about a :ref:`View Event <protocol-definitions-viewevent>`.
* Using the endpoint contained in the metadata, :ref:`SSA <protocol-definitions-ssa>` calls :ref:`DSP <protocol-definitions-dsp>` to notify it that a :ref:`View Event <protocol-definitions-viewevent>` has occurred.
* In response to the event notification call, :ref:`DSP <protocol-definitions-dsp>` returns endpoints of its trusted instances of :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>`.
* Using the above endpoint, :ref:`SSA <protocol-definitions-ssa>` notifies :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` about a :ref:`Register Event <protocol-definitions-registerevent>`.
* In response to the event notification call, :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` return :ref:`Context Scripts <protocol-definitions-contextscript>`, and :ref:`SSA <protocol-definitions-ssa>` makes an attempt to execute those scripts.

User clicks on a Creative
-------------------------

The following process takes place when a :ref:`User <protocol-definitions-user>` clicks on any of the displayed :ref:`Creatives <protocol-definitions-creative>`, assuming they are clickable.

* :ref:`SSA <protocol-definitions-ssa>` notifies :ref:`SSP <protocol-definitions-ssp>` about a :ref:`Click Event <protocol-definitions-clickevent>`.
* Using the endpoint contained in the metadata, :ref:`SSA <protocol-definitions-ssa>` calls :ref:`DSP <protocol-definitions-dsp>` to notify it that a :ref:`Click Event <protocol-definitions-clickevent>` has occurred.
* Using its internal mapping, :ref:`DSP <protocol-definitions-dsp>` redirects the click event to :ref:`DSA <protocol-definitions-dsa>`, so that in effect :ref:`User <protocol-definitions-user>` navigates from the :ref:`Site <protocol-definitions-site>` to :ref:`DSA <protocol-definitions-dsa>`. Optionally, :ref:`DSA <protocol-definitions-dsa>` responds to :ref:`DSP <protocol-definitions-dsp>` to report that a conversion event has occurred.

