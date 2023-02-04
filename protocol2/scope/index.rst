Scope
=====

.. _protocol-scope:

The following four areas are handled by :ref:`Adshares Protocol <adshares-protocol2>`.

Authentication
--------------
How various entities participating in :ref:`Adshares Protocol <adshares-protocol2>` authenticate each other.

Synchronization
---------------
#. How :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` and :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` announce their current availability:
    * published by: :ref:`SSP <protocol-definitions-ssp>` and :ref:`DSP <protocol-definitions-dsp>`
    * retrieved by: :ref:`SSP <protocol-definitions-ssp>` and :ref:`DSP <protocol-definitions-dsp>`
    * medium: :ref:`Adshares Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` exposes its inventory data:
    * exposed by: :ref:`DSP <protocol-definitions-dsp>`
    * consumed by: :ref:`SSP <protocol-definitions-ssp>`
    * returns: :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`

#. How :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` exposes its inventory data:
    * exposed by: :ref:`SSP <protocol-definitions-ssp>`
    * consumed by: :ref:`DSP <protocol-definitions-dsp>`
    * returns: :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`

Impressions
-----------
#. How :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` exposes context data:
    * exposed by: :ref:`UCP <protocol-definitions-ucp>`, :ref:`SCP <protocol-definitions-scp>`, :ref:`DCP <protocol-definitions-dcp>`
    * consumed by: :ref:`SSP <protocol-definitions-ssp>` and :ref:`DSP <protocol-definitions-dsp>`
    * returns: :ref:`Context Data<protocol-definitions-contextdata>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` exposes content data:
    * exposed by: :ref:`DSP <protocol-definitions-dsp>`
    * consumed by: :ref:`SSA<protocol-definitions-ssa>`
    * returns: :ref:`Creative Content<protocol-definitions-creativecontent>`

#. How :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` accepts notifications about :ref:`Register Events <protocol-definitions-registerevent>`:
    * exposed by: :ref:`UCP <protocol-definitions-ucp>`, :ref:`SCP <protocol-definitions-scp>`, :ref:`DCP <protocol-definitions-dcp>`
    * consumed by: :ref:`SSA<protocol-definitions-ssa>`
    * returns: :ref:`Context Script <protocol-definitions-contextscript>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` accepts notifications about :ref:`View Events <protocol-definitions-viewevent>` or :ref:`Click Events <protocol-definitions-clickevent>`:
    * exposed by: :ref:`DSP <protocol-definitions-dsp>`
    * consumed by: :ref:`SSA<protocol-definitions-ssa>`
    * returns: endpoints for :ref:`UCP <protocol-definitions-ucp>`, :ref:`SCP <protocol-definitions-scp>`, :ref:`DCP <protocol-definitions-dcp>`

Payments
--------
#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` sends payments to :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`:
    * payer: :ref:`DSP <protocol-definitions-dsp>`
    * payee: :ref:`SSP <protocol-definitions-ssp>`
    * medium: :ref:`Adshares Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` exposes payment reports:
    * exposed by: :ref:`DSP <protocol-definitions-dsp>`
    * consumed by: :ref:`SSP <protocol-definitions-ssp>`
    * returns: :ref:`Payment Report <protocol-definitions-paymentreport>`