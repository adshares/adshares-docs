User Clicks on an Ad
====================

The following diagram presents the details of the workflow that takes place when a :ref:`User <protocol-definitions-user>` 
clicks on a :ref:`Creative <protocol-definitions-creative>`, assuming it is clickable:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"                as SSA
    participant "Supply-Side\nPlatform"             as SSP
    participant "Demand-Side\nPlatform"             as DSP
    participant "Demand-Side\nAgent"                as DSA

    SSA ->      SSP     : Post Click Event
    SSP ->      DSP     : Post Click Event\n//redirected//
    DSP ->      DSA     : Post Click Event\n//redirected//
    DSA -->     DSP     : Post Conversion Event\n//optional//

Here are the main steps of the above workflow:

* Using the endpoint contained in :ref:`Creative Object <protocol-definitions-creativeobject>`, 
  :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>`
  about :ref:`Click Event <protocol-definitions-clickevent>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` redirects the :ref:`Click Event <protocol-definitions-clickevent>` 
  notification call to the corresponding :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` redirects the :ref:`Click Event <protocol-definitions-clickevent>` 
  notification call to its :ref:`Demand-Side Agent <protocol-definitions-dsa>`. 
  Simultaneously, using its internal mapping, :ref:`Demand-Side Platform <protocol-definitions-dsp>` redirects the :ref:`User <protocol-definitions-user>` 
  from the :ref:`Site <protocol-definitions-site>` to the :ref:`Target <protocol-definitions-target>`.
* Optionally, :ref:`Demand-Side Agent <protocol-definitions-dsa>` notifies :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  about :ref:`Conversion Event <protocol-definitions-conversion>`.
