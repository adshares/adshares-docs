
.. _adshares-protocol:

Adshares Protocol
=================
:ref:`Adshares Protocol <adshares-protocol>` describes interactions between the following components:

* :ref:`Supply-Side Infrastructure <protocol-ssi>`
* :ref:`Demand-Side Infrastructure <protocol-dsi>`
* :ref:`Context Infrastructure <protocol-contextinfrastructure>`
* :ref:`Tagging Infrastructure <protocol-tagginginfrastructure>`

The following diagram presents the main components taking part in :ref:`Adshares Protocol <adshares-protocol>` and the relationships between them:

.. image:: index.svg
    :align: center

The following diagram presents an overview of interactions defined by :ref:`Adshares Protocol <adshares-protocol>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "SS Context\nInfrastructure"      as SSCI
    participant "Supply-Side\nInfrastructure"     as SSI
    participant "ADS\nBlockchain"                 as blockchain
    participant "Demand-Side\nInfrastructure"     as DSI
    participant "DS Context\nInfrastructure"      as DSCI
    
    ==Synchronization==

    SSI -> blockchain: Send Broadcast
    DSI -> blockchain: Send Broadcast
    SSI -> blockchain: Fetch Broadcast
    DSI -> blockchain: Fetch Broadcast
    SSI -> DSI: Fetch Demand-Side Inventory
    DSI -> SSI: Fetch Supply-Side Inventory

    ==Impressions==

    SSI -> DSI: Get Creative Content
    SSI -> DSI: Post Impression Events
    SSI -> SSCI: Post Impression Events
    SSI -> DSCI: Post Impression Events

    ==Payments==

    DSI -> blockchain: Send payment
    SSI -> blockchain: Fetch transactions
    SSI -> DSI: Fetch Payment Report

Scope
^^^^^

:doc:`Authentication <authentication/index>`
""""""""""""""""""""""""""""""""""""""""""""
How various entities participating in :ref:`Adshares Protocol <adshares-protocol>` authenticate each other.

:doc:`Synchronization <synchronization/index>`
""""""""""""""""""""""""""""""""""""""""""""""
#. How :ref:`Supply-Side Infrastructure <protocol-ssi>` and :ref:`Demand-Side Infrastructure <protocol-dsi>` announce their current availability:
    * published by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * retrieved by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * medium: :ref:`ADS Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Infrastructure <protocol-dsi>` exposes its inventory data:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`

#. How :ref:`Supply-Side Infrastructure <protocol-ssi>` exposes its inventory data:
    * exposed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * consumed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`

:doc:`Impressions <impressions/index>`
""""""""""""""""""""""""""""""""""""""
#. How :ref:`Context Infrastructure <protocol-contextinfrastructure>` exposes information about :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>` and :ref:`Devices <protocol-definitions-device>`:
    * exposed by: :ref:`Context Platform <protocol-definitions-cp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Context Data <protocol-definitions-contextdata>`

#. How :ref:`Context Infrastructure <protocol-contextinfrastructure>` accepts notifications about :ref:`Impression Events <protocol-definitions-impression>`:
    * exposed by: :ref:`Context Platform <protocol-definitions-cp>`
    * consumed by: :ref:`Supply-Side Agent <protocol-definitions-ssa>`
    * returns: :ref:`Context Script <protocol-definitions-contextscript>`

#. How :ref:`Demand-Side Infrastructure <protocol-dsi>` exposes the content of a :ref:`Creative <protocol-definitions-creative>`:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Agent <protocol-definitions-ssa>`
    * returns: :ref:`Creative Content <protocol-definitions-creativecontent>`

#. How :ref:`Demand-Side Infrastructure <protocol-dsi>` accepts notifications about :ref:`Impression Events <protocol-definitions-impression>`:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Agent <protocol-definitions-ssa>`
    * redirects to: :ref:`Context Infrastructure <protocol-contextinfrastructure>`

#. (Optional) How :ref:`Supply-Side Platform <protocol-definitions-ssp>` outsources the process of selecting :ref:`Creatives <protocol-definitions-creative>`:
    * exposed by: :ref:`Ad Select Module <protocol-definitions-asm>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: list of :ref:`Creative Objects <protocol-definitions-creativeobject>`

:doc:`Payments <payments/index>`
""""""""""""""""""""""""""""""""

#. How :ref:`Demand-Side Infrastructure <protocol-dsi>` sends payments to :ref:`Supply-Side Infrastructure <protocol-ssi>`:
    * payer: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * payee: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * medium: :ref:`ADS Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Infrastructure <protocol-dsi>` exposes information about executed payments:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: :ref:`Payment Report <protocol-definitions-paymentreport>`

#. (Optional) How :ref:`Demand-Side Platform <protocol-definitions-dsp>` outsources the process of generating :ref:`Payment Reports <protocol-definitions-paymentreport>`:
    * exposed by: :ref:`Ad Pay Module <protocol-definitions-apm>`
    * consumed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Payment Report <protocol-definitions-paymentreport>`

Contents
^^^^^^^^
.. toctree::
    :maxdepth: 1
    
    definitions/index
    infrastructure/index
    authentication/index
    synchronization/index
    impressions/index
    payments/index
    taxonomy/index