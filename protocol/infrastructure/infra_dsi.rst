.. _protocol-dsi:

Demand-Side Infrastructure
--------------------------

:ref:`Demand-Side Infrastructure <protocol-dsi>` delivers services for :ref:`Advertisers <protocol-definitions-advertiser>`, or acts on their behalf.

:ref:`Demand-Side Infrastructure <protocol-dsi>` consists of :ref:`Demand-Side Platform <protocol-definitions-dsp>`, its :ref:`Demand-Side Agent <protocol-definitions-dsa>`
(which is embedded in the :ref:`Target <protocol-definitions-target>`), and optionally an :ref:`Ad Pay Module <protocol-definitions-apm>`.

.. image:: infra_dsi.svg
    :align: center

:ref:`Adshares Protocol <adshares-protocol>` defines the following interactions between :ref:`Demand-Side Infrastructure <protocol-dsi>`
and other entities within the :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* :ref:`Demand-Side Infrastructure <protocol-dsi>` calls :ref:`Creative Tagging Platform <protocol-definitions-ctp>` to tag the :ref:`Creatives <protocol-definitions-creative>`
  that remain under its control.
* :ref:`Demand-Side Infrastructure <protocol-dsi>` calls :ref:`Site Tagging Platform <protocol-definitions-stp>` to verify tags assigned 
  to :ref:`Sites <protocol-definitions-site>` by :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`.
* :ref:`Demand-Side Infrastructure <protocol-dsi>` calls :ref:`Context Platform <protocol-definitions-cp>` to retrieve 
  :ref:`Context Data <protocol-definitions-contextdata>` regarding :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>`
  and :ref:`Devices <protocol-definitions-device>`.
* :ref:`Demand-Side Infrastructure <protocol-dsi>` receives :ref:`Impression Events <protocol-definitions-impression>` shared with it 
  by :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`.
* :ref:`Demand-Side Infrastructure <protocol-dsi>` shares the received :ref:`Impression Events <protocol-definitions-impression>` 
  with its :ref:`Context Platform <protocol-definitions-cp>`.
* :ref:`Demand-Side Infrastructure <protocol-dsi>` returns :ref:`Payment Reports <protocol-definitions-paymentreport>` requested by :ref:`Supply-Side Platforms <protocol-definitions-ssp>`.

:ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Demand-Side Agent <protocol-definitions-dsa>` are free to communicate in any way they choose, 
as this communication is *not* part of :ref:`Adshares Protocol <adshares-protocol>`. Thus, any interactions between :ref:`Demand-Side Platform <protocol-definitions-dsp>`
and its :ref:`Demand-Side Agent <protocol-definitions-dsa>` (e.g. notifications about :ref:`Conversion Events <protocol-definitions-conversion>`) 
are not covered by :ref:`Adshares Protocol <adshares-protocol>`.

Whereas the communication between :ref:`Demand-Side Platform <protocol-definitions-dsp>` and its :ref:`Ad Pay Module <protocol-definitions-apm>`
might be part of :ref:`Adshares Protocol <adshares-protocol>` in case :ref:`Ad Pay Module <protocol-definitions-apm>` is delivered 
by a third-party :ref:`Software Provider <protocol-definitions-softwareprovider>`. If this is the case, :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
calls its :ref:`Ad Pay Module <protocol-definitions-apm>` to outsource to it the process of generating a :ref:`Payment Report <protocol-definitions-paymentreport>`.
