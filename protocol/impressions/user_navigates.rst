User Navigates to a Site
========================

The following diagram presents the details of the workflow that takes place when a :ref:`User <protocol-definitions-user>`
initially navigates to a :ref:`Site <protocol-definitions-site>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"                as SSA
    participant "Supply-Side\nPlatform"             as SSP
    participant "Supply-Side\nContext Provider"     as SSCP

    SSA ->      SSP     : Post Register Event
    SSP -->     SSA     : Context Scripts
    SSA ->      SSA     : Execute\nContext Scripts
    SSA ->      SSCP    : Post Register Event
    SSCP -->     SSA    : Context Scripts
    SSA ->      SSA     : Execute\nContext Scripts
    SSA ->      SSCP    : Result of Context Scripts\n//optional//

Here are the main steps of the above workflow:

* :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  about :ref:`Register Event <protocol-definitions-registerevent>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` returns its :ref:`Context Script <protocol-definitions-contextscript>`,
  and :ref:`Supply-Side Agent <protocol-definitions-ssa>` makes an attempt to execute this script within its sandbox.
* Using an endpoint contained in the :ref:`Context Script <protocol-definitions-contextscript>`, :ref:`Supply-Side Agent <protocol-definitions-ssa>`
  notifies :ref:`Context Provider <protocol-definitions-cp>` about :ref:`Register Event <protocol-definitions-registerevent>`.
* In response to the :ref:`Register Event <protocol-definitions-registerevent>` notification call, :ref:`Context Provider <protocol-definitions-cp>` 
  returns its :ref:`Context Script <protocol-definitions-contextscript>`, and :ref:`Supply-Side Agent <protocol-definitions-ssa>` 
  makes an attempt to execute this script within its sandbox.

At this stage :ref:`Register Event <protocol-definitions-registerevent>` is only reported within :ref:`Supply-Side Platform <protocol-definitions-ssp>`.
To keep both sides in synch, :ref:`Register Event <protocol-definitions-registerevent>` will be distributed to
:ref:`Demand-Side Platform <protocol-definitions-dsp>` in the next step.