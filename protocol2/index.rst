
.. _adshares-protocol2:

Adshares Protocol2
==================
:ref:`Adshares Protocol <adshares-protocol2>` describes interactions between the following pieces of infrastructure within the :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`
* :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>`
* :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>`
* :ref:`Tagging Infrastructure <protocol-definitions-tagginginfrastructure>`

The following diagram illustrates the components making up the above infrastructure and the relationships between them:

.. image:: index.png

.. Check out the :doc:`Definitions <definitions/index>` section.

The following areas are handled by :ref:`Adshares Protocol <adshares-protocol2>`:

Authentication
--------------
How various entities participating in :ref:`Adshares Protocol <adshares-protocol2>` authenticate each other.

Synchronization
---------------
#. How :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` and :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` announce their current availability:
    * published by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * retrieved by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * medium: :ref:`Adshares Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` exposes its inventory data:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`

#. How :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` exposes its inventory data:
    * exposed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * consumed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`

Impressions
-----------
#. How :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` exposes context data:
    * exposed by: :ref:`Context Platform <protocol-definitions-cp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Context Data<protocol-definitions-contextdata>`

#. How :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` accepts notifications about :ref:`Register Events <protocol-definitions-registerevent>`:
    * exposed by: :ref:`Context Platform <protocol-definitions-cp>`
    * consumed by: :ref:`Supply-Side Agent<protocol-definitions-ssa>`
    * returns: :ref:`Context Script <protocol-definitions-contextscript>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` exposes content data:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Agent<protocol-definitions-ssa>`
    * returns: :ref:`Creative Content<protocol-definitions-creativecontent>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` accepts notifications about :ref:`View Events <protocol-definitions-viewevent>`:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Agent<protocol-definitions-ssa>`
    * returns: :ref:`Context Platform <protocol-definitions-cp>` endpoint

Payments
--------
#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` sends payments to :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`:
    * payer: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * payee: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * medium: :ref:`Adshares Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` exposes payment reports:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: :ref:`Payment Report <protocol-definitions-paymentreport>`

Contents
^^^^^^^^
.. toctree::
    :maxdepth: 1
    
    definitions/index
    authentication/index
    synchronization/index
    impressions/index
    payments/index
