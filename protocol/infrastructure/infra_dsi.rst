.. _protocol-dsi:

Demand-Side Infrastructure
--------------------------

:ref:`Demand-Side Platform <protocol-definitions-dsp>` delivers services for :ref:`Advertisers <protocol-definitions-advertiser>`, or acts on their behalf.

:ref:`Demand-Side Platform <protocol-definitions-dsp>` consists of :ref:`Demand-Side Platform <protocol-definitions-dsp>`, its :ref:`Demand-Side Agent <protocol-definitions-dsa>`
(which is embedded in the :ref:`Target <protocol-definitions-target>`), and optionally an :ref:`Ad Pay Module <protocol-definitions-apm>`.

.. image:: infra_dsi.svg
    :align: center

:ref:`Adshares Protocol <adshares-protocol>` defines the following interactions between :ref:`Demand-Side Platform <protocol-definitions-dsp>`
and other entities within the :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* :ref:`Demand-Side Platform <protocol-definitions-dsp>` calls :ref:`Creative Tagging Provider <protocol-definitions-ctp>` to tag the :ref:`Creatives <protocol-definitions-creative>`
  that remain under its control. This is needed for :ref:`Demand-Side Platform <protocol-definitions-dsp>` to be able to properly define its 
  :ref:`Demand-Side Inventory <protocol-synchronization-demandinventory>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` verifies tags assigned to :ref:`Sites <protocol-definitions-site>` by checking 
  :ref:`Site Tagging Provider <protocol-definitions-stp>`'s signature.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` calls :ref:`Context Provider <protocol-definitions-cp>` to retrieve 
  :ref:`Context Data <protocol-definitions-contextdata>` regarding :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>`
  and :ref:`Devices <protocol-definitions-device>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` receives :ref:`Impression Events <protocol-definitions-impression>` shared with it 
  by :ref:`Supply-Side Platform <protocol-definitions-ssp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` shares the received :ref:`Impression Events <protocol-definitions-impression>` 
  with its :ref:`Context Provider <protocol-definitions-cp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` returns :ref:`Payment Reports <protocol-definitions-paymentreport>` requested by :ref:`Supply-Side Platforms <protocol-definitions-ssp>`.

:ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Demand-Side Agent <protocol-definitions-dsa>` are free to communicate in any way they choose, 
as this communication is *not* part of :ref:`Adshares Protocol <adshares-protocol>`. Thus, any interactions between :ref:`Demand-Side Platform <protocol-definitions-dsp>`
and its :ref:`Demand-Side Agent <protocol-definitions-dsa>` (e.g. notifications about :ref:`Conversion Events <protocol-definitions-conversion>`) 
are not covered by :ref:`Adshares Protocol <adshares-protocol>`.

Whereas the communication between :ref:`Demand-Side Platform <protocol-definitions-dsp>` and its :ref:`Ad Pay Module <protocol-definitions-apm>`
might be part of :ref:`Adshares Protocol <adshares-protocol>` in case :ref:`Ad Pay Module <protocol-definitions-apm>` is externalized and delivered 
by a third-party :ref:`Software Provider <protocol-definitions-softwareprovider>`. If this is the case, :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
calls its :ref:`Ad Pay Module <protocol-definitions-apm>` to outsource to it the process of generating :ref:`Payment Reports <protocol-definitions-paymentreport>`.
