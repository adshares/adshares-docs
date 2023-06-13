
.. _adshares-protocol:

Adshares Protocol
=================
:ref:`Adshares Protocol <adshares-protocol>` describes interactions between the following components:

* :ref:`Supply-Side Platforms <protocol-definitions-ssp>`
* :ref:`Demand-Side Platforms <protocol-definitions-dsp>`
* :ref:`Context Providers <protocol-definitions-cp>`
* :ref:`Tagging Providers <protocol-definitions-tp>`

The following diagram presents the main components participating in :ref:`Adshares Protocol <adshares-protocol>` and the relationships between them:

.. image:: index.svg
    :align: center

The following diagram presents a simplified overview of the main interactions defined by :ref:`Adshares Protocol <adshares-protocol>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply-Side\nAgent"              as SSA
    participant "Supply-Side\nContext Provider"   as SSCP
    participant "Supply-Side\nPlatform"           as SSP
    participant "ADS\nBlockchain"                 as blockchain
    participant "Demand-Side\nPlatform"           as DSP
    participant "Demand-Side\nContext Provider"   as DSCP
    
    ==Synchronization==

    SSP -> blockchain: Send Broadcast
    DSP -> blockchain: Send Broadcast
    SSP -> blockchain: Fetch Broadcast
    DSP -> blockchain: Fetch Broadcast
    SSP -> DSP: Fetch Demand-Side Inventory
    DSP -> SSP: Fetch Supply-Side Inventory

    ==Impressions==

    SSA -> SSCP: Register Event
    SSA -> DSP: Get Creative Content
    SSA -> DSP: View Event
    SSA -> DSCP: Register Event
    SSA -> SSP: Click Event
    SSP -> DSP: Click Event

    ==Payments==

    DSP -> blockchain: Send payment
    SSP -> blockchain: Fetch transactions
    SSP -> DSP: Fetch Payment Report

Scope
^^^^^

:doc:`Authentication <authentication/index>`
""""""""""""""""""""""""""""""""""""""""""""
How various entities participating in :ref:`Adshares Protocol <adshares-protocol>` authenticate each other.

:doc:`Synchronization <synchronization/index>`
""""""""""""""""""""""""""""""""""""""""""""""
#. How :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` announce their current availability:
    * published by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * retrieved by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * medium: :ref:`ADS Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Platforms <protocol-definitions-dsp>` expose their inventory data:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`

#. How :ref:`Supply-Side Platforms <protocol-definitions-ssp>` expose their inventory data:
    * exposed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * consumed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`

:doc:`Impressions <impressions/index>`
""""""""""""""""""""""""""""""""""""""
#. How :ref:`Context Providers <protocol-definitions-cp>` expose information about :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>` and :ref:`Devices <protocol-definitions-device>`:
    * exposed by: :ref:`Context Provider <protocol-definitions-cp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * returns: :ref:`Context Data <protocol-definitions-contextdata>`

#. How :ref:`Context Providers <protocol-definitions-cp>` accept notifications about :ref:`Impression Events <protocol-definitions-impression>`:
    * exposed by: :ref:`Context Provider <protocol-definitions-cp>`
    * consumed by: :ref:`Supply-Side Agent <protocol-definitions-ssa>`
    * returns: :ref:`Context Script <protocol-definitions-contextscript>`

#. How :ref:`Demand-Side Platforms <protocol-definitions-dsp>` expose content of :ref:`Creatives <protocol-definitions-creative>`:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Agent <protocol-definitions-ssa>`
    * returns: :ref:`Creative Content <protocol-definitions-creativecontent>`

#. How :ref:`Demand-Side Platforms <protocol-definitions-dsp>` accept notifications about :ref:`Impression Events <protocol-definitions-impression>`:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Agent <protocol-definitions-ssa>`
    * redirects to: :ref:`Context Provider <protocol-definitions-cp>`

#. (Optional) How :ref:`Supply-Side Platforms <protocol-definitions-ssp>` outsource the process of selecting :ref:`Creatives <protocol-definitions-creative>`:
    * exposed by: :ref:`Ad Select Module <protocol-definitions-asm>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: list of :ref:`Creative Objects <protocol-definitions-creativeobject>`

:doc:`Payments <payments/index>`
""""""""""""""""""""""""""""""""

#. How :ref:`Demand-Side Platforms <protocol-definitions-dsp>` send payments to :ref:`Supply-Side Platforms <protocol-definitions-ssp>`:
    * payer: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * payee: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * medium: :ref:`ADS Blockchain <protocol-definitions-blockchain>`

#. How :ref:`Demand-Side Platforms <protocol-definitions-dsp>` expose information about executed payments:
    * exposed by: :ref:`Demand-Side Platform <protocol-definitions-dsp>`
    * consumed by: :ref:`Supply-Side Platform <protocol-definitions-ssp>`
    * returns: :ref:`Payment Report <protocol-definitions-paymentreport>`

#. (Optional) How :ref:`Demand-Side Platforms <protocol-definitions-dsp>` outsource the process of generating :ref:`Payment Reports <protocol-definitions-paymentreport>`:
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
    services/index
    taxonomy/index