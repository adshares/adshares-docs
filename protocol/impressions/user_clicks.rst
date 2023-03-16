User Clicks on an Ad
====================

The following diagram presents the details of the workflow that takes place when a :ref:`User <protocol-definitions-user>` 
clicks on a :ref:`Creative <protocol-definitions-creative>`, assuming it is clickable:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"                as SSA
    participant "Supply-Side\nPlatform"             as SSP
    participant "Supply-Side\nContext Platform"     as SSCP
    participant "Demand-Side\nPlatform"             as DSP
    participant "Demand-Side\nContext Platform"     as DSCP
    participant "Demand-Side\nAgent"                as DSA

    ==Click Event==
    SSA ->      SSP     : Post Click Event
    SSP ->      SSCP    : Post Click Event\n//redirected//

    ==Click Event==
    SSA ->      DSP     : Post Click Event
    DSP ->      DSCP    : Post Click Event\n//redirected//
    DSA -->     DSP     : Post Conversion Event\n//optional//

The following process takes place when a :ref:`User <protocol-definitions-user>` clicks on a
:ref:`Creative <protocol-definitions-creative>`, assuming it is clickable:

* :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  about :ref:`Click Event <protocol-definitions-clickevent>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` redirects the :ref:`Click Event <protocol-definitions-clickevent>` 
  notification call to its :ref:`Context Platform <protocol-definitions-cp>`.
* Using the endpoint contained in :ref:`Creative Object <protocol-definitions-creativeobject>`, 
  :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Demand-Side Platform <protocol-definitions-dsp>`
  about :ref:`Click Event <protocol-definitions-clickevent>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` redirects the :ref:`Click Event <protocol-definitions-clickevent>` 
  notification call to its :ref:`Context Platform <protocol-definitions-cp>`.
* Using its internal mapping, :ref:`Demand-Side Platform <protocol-definitions-dsp>` redirects the :ref:`User <protocol-definitions-user>` 
  from the :ref:`Site <protocol-definitions-site>` to the :ref:`Target <protocol-definitions-target>`.
* Optionally, :ref:`Demand-Side Agent <protocol-definitions-dsa>` notifies :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  about :ref:`Conversion Event <protocol-definitions-conversion>`.
