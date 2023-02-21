User clicks on an ad
====================

The following process takes place when :ref:`User <protocol-definitions-user>` clicks on any instance of the displayed :ref:`Creatives <protocol-definitions-creative>`, assuming it is clickable:

.. container:: protocol

    * :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>` about :ref:`Click Event <protocol-definitions-clickevent>`.
    * :ref:`Supply-Side Agent <protocol-definitions-ssa>` redirects the event notification call to :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
    * Using its internal mapping, :ref:`Demand-Side Platform <protocol-definitions-dsp>` redirects the :ref:`Click Event <protocol-definitions-clickevent>` to the :ref:`Target <protocol-definitions-target>`, so that in effect :ref:`User <protocol-definitions-user>` navigates from the :ref:`Site <protocol-definitions-site>` to the :ref:`Target <protocol-definitions-target>`.
    * Optionally, :ref:`Demand-Side Agent <protocol-definitions-dsa>` responds to :ref:`Demand-Side Platform <protocol-definitions-dsp>` to notify it about :ref:`Conversion Event <protocol-definitions-conversion>`.
