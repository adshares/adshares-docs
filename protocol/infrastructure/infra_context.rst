.. _protocol-contextinfrastructure:

Context Infrastructure
----------------------

Both :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>`
use :ref:`Context Provider <protocol-definitions-cp>` to retrieve data about :ref:`Users <protocol-definitions-user>`,
:ref:`Sites <protocol-definitions-site>` and :ref:`Devices <protocol-definitions-device>`.

.. image:: infra_context.svg
    :align: center

:ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>` need to independently decide 
which instances of :ref:`Context Provider <protocol-definitions-cp>` they trust, and then independently query them. 
Even in case :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>` choose to trust
the same instance of :ref:`Context Provider <protocol-definitions-cp>`, they need to query it separately.

:ref:`Context Provider <protocol-definitions-cp>` needs to track :ref:`Register Events <protocol-definitions-registerevent>`. Thus,
:ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` need to share with 
:ref:`Context Provider <protocol-definitions-cp>` all the :ref:`Register Events <protocol-definitions-registerevent>` that they receive.

In response to a :ref:`Register Event <protocol-definitions-registerevent>` notification, :ref:`Context Provider <protocol-definitions-cp>` 
returns a :ref:`Context Script <protocol-definitions-contextscript>`, and then receives the results of this script being executed 
by a :ref:`Supply-Side Agent <protocol-definitions-ssa>` within its sandbox.
