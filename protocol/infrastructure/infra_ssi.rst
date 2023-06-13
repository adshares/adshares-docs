.. _protocol-ssi:

Supply-Side Infrastructure
--------------------------

:ref:`Supply-Side Platform <protocol-definitions-ssp>` delivers services for :ref:`Publishers <protocol-definitions-publisher>`, or acts on their behalf.

:ref:`Supply-Side Platform <protocol-definitions-ssp>` consists of :ref:`Supply-Side Platform <protocol-definitions-ssp>`, its :ref:`Supply-Side Agent <protocol-definitions-ssa>`
(which is embedded in the :ref:`Site <protocol-definitions-site>`), and optionally an :ref:`Ad Select Module <protocol-definitions-asm>`.

.. image:: infra_ssi.svg
    :align: center

:ref:`Adshares Protocol <adshares-protocol>` defines the following interactions between :ref:`Supply-Side Platform <protocol-definitions-ssp>`  
and other entities within the :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls :ref:`Site Tagging Provider <protocol-definitions-stp>` to tag the :ref:`Sites <protocol-definitions-site>` 
  that remain under its control. This is needed for :ref:`Supply-Side Platform <protocol-definitions-ssp>` to be able to properly define its 
  :ref:`Supply-Side Inventory <protocol-synchronization-supplyinventory>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` verifies tags assigned to :ref:`Creatives <protocol-definitions-creative>` by checking 
  :ref:`Creative Tagging Provider <protocol-definitions-ctp>`'s signature.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls :ref:`Context Provider <protocol-definitions-cp>` to retrieve 
  :ref:`Context Data <protocol-definitions-contextdata>` regarding :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>`
  and :ref:`Devices <protocol-definitions-device>`.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` shares the received :ref:`Click Events <protocol-definitions-clickevent>`
  with :ref:`Demand-Side Platform <protocol-definitions-dsp>` which a given :ref:`Creative <protocol-definitions-creative>` belongs to.
* :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls :ref:`Demand-Side Platform <protocol-definitions-dsp>`
  to receive a :ref:`Payment Report <protocol-definitions-paymentreport>`.

:ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Supply-Side Agent <protocol-definitions-ssa>` are free to communicate in any way they choose, 
as this communication is *not* part of :ref:`Adshares Protocol <adshares-protocol>`. Thus, any interactions between :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
and its :ref:`Supply-Side Agent <protocol-definitions-ssa>` (e.g. notifications about :ref:`Impression Events <protocol-definitions-impression>`) 
are not covered by :ref:`Adshares Protocol <adshares-protocol>`.

Whereas the communication between :ref:`Supply-Side Platform <protocol-definitions-ssp>` and its :ref:`Ad Select Module <protocol-definitions-asm>` 
might be part of :ref:`Adshares Protocol <adshares-protocol>` in case :ref:`Ad Select Module <protocol-definitions-asm>` is externalized and delivered 
by a third-party :ref:`Software Provider <protocol-definitions-softwareprovider>`. If this is the case, :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
calls its :ref:`Ad Select Module <protocol-definitions-asm>` to outsource to it the process of generating a list of :ref:`Creatives <protocol-definitions-creative>`.

The details of the communication between :ref:`Supply-Side Platform <protocol-definitions-ssp>` and its :ref:`Ad Select Module <protocol-definitions-asm>`
are described in the :ref:`Ad Select Service <protocol-services-asm>` section.
