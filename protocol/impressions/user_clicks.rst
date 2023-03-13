User Clicks on an Ad
====================

The following diagram presents the details of the workflow that takes place when a :ref:`User <protocol-definitions-user>` 
clicks on a :ref:`Creative <protocol-definitions-creative>`, assuming it is clickable:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"            as SSA
    participant "Supply-Side\nPlatform"         as SSP
    participant "Demand-Side\nPlatform"         as DSP
    participant "Demand-Side\nAgent"            as DSA

    SSA ->      SSP     : Send Click Event
    SSP ->      DSP     : Send Click Event\n//redirected//
    DSP ->      DSA     : Send Click Event\n//redirected//
    DSA -->     DSP     : Confirm Click Event\n//optional//

The following process takes place when a :ref:`User <protocol-definitions-user>` clicks on a
:ref:`Creative <protocol-definitions-creative>`, assuming it is clickable:

* :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  about :ref:`Click Event <protocol-definitions-clickevent>`.
* :ref:`Supply-Side Agent <protocol-definitions-ssa>` redirects the event notification call to :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
* Using its internal mapping, :ref:`Demand-Side Platform <protocol-definitions-dsp>` redirects the :ref:`Click Event <protocol-definitions-clickevent>` 
  to the :ref:`Target <protocol-definitions-target>`, so that in effect :ref:`User <protocol-definitions-user>` navigates 
  from the :ref:`Site <protocol-definitions-site>` to the :ref:`Target <protocol-definitions-target>`.
* Optionally, :ref:`Demand-Side Agent <protocol-definitions-dsa>` responds to :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  to notify it about :ref:`Conversion Event <protocol-definitions-conversion>`.
