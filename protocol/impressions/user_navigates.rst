User Navigates to a Site
========================

The following diagram presents the details of the workflow:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"       as SSA
    participant "SS Context\nPlatform"     as SSCP
    participant "Supply-Side\nPlatform"    as SSP

    SSA -> SSP : Register Event
    SSP -> SSCP : Register Event\n//redirected//
    SSCP --> SSA: Context Scripts
    SSA -> SSA: Execute\nContext Scripts
    SSA -> SSCP: Result of Context Scripts\n//optional//

The following process takes place when :ref:`User <protocol-definitions-user>` initially navigates to a :ref:`Site <protocol-definitions-site>`:

* :ref:`Supply-Side Agent <protocol-definitions-ssa>` notifies :ref:`Supply-Side Platform <protocol-definitions-ssp>` about :ref:`Register Event <protocol-definitions-registerevent>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` redirects the :ref:`Register Event <protocol-definitions-registerevent>` notification call to its :ref:`Context Platform <protocol-definitions-cp>`.
* In response to the :ref:`Register Event <protocol-definitions-registerevent>` notification call, :ref:`Context Platform <protocol-definitions-cp>` returns its :ref:`Context Script <protocol-definitions-contextscript>`, and :ref:`Supply-Side Agent <protocol-definitions-ssa>` makes an attempt to execute this script within its sandbox.
