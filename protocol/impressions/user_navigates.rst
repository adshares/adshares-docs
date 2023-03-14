User Navigates to a Site
========================

The following diagram presents the details of the workflow that takes place when a :ref:`User <protocol-definitions-user>`
initially navigates to a :ref:`Site <protocol-definitions-site>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"                as SSA
    participant "Supply-Side\nPlatform"             as SSP
    participant "Supply-Side\nContext Platform"     as SSCP

    SSA ->      SSP     : Post Register Event
    SSP ->      SSCP    : Post Register Event\n//redirected//
    SSCP -->    SSA     : Context Scripts
    SSA ->      SSA     : Execute\nContext Scripts
    SSA ->      SSCP    : Result of Context Scripts\n//optional//

The following process takes place when a :ref:`User <protocol-definitions-user>` initially navigates to a :ref:`Site <protocol-definitions-site>`:

* :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  about :ref:`Register Event <protocol-definitions-registerevent>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` redirects the :ref:`Register Event <protocol-definitions-registerevent>` 
  notification call to its :ref:`Context Platform <protocol-definitions-cp>`.
* In response to the :ref:`Register Event <protocol-definitions-registerevent>` notification call, :ref:`Context Platform <protocol-definitions-cp>` 
  returns its :ref:`Context Script <protocol-definitions-contextscript>`, and :ref:`Supply-Side Agent <protocol-definitions-ssa>` 
  makes an attempt to execute this script within its sandbox.

At this stage :ref:`Register Event <protocol-definitions-registerevent>` is only reported within :ref:`Supply-Side Infrastructure <protocol-ssi>`.
To keep both sides in synch, :ref:`Register Event <protocol-definitions-registerevent>` will be distributed to
:ref:`Demand-Side Infrastructure <protocol-dsi>` in the next step.