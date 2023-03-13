.. _protocol-definitions-dsi:

Demand-Side Infrastructure
--------------------------

:ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` delivers services for :ref:`Advertisers <protocol-definitions-advertiser>`, or acts on their behalf.
The central part of :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` consists of :ref:`Demand-Side Platform <protocol-definitions-dsp>`.

.. image:: def_dsi.svg

:ref:`Adshares Protocol <adshares-protocol>` defines the following interactions between :ref:`Demand-Side Platform <protocol-definitions-dsp>`  
and other entities within the :ref:`Adshares Ecosystem <protocol-definitions-ecosystem>`:

* :ref:`Demand-Side Platform <protocol-definitions-dsp>` calls :ref:`Creative Tagging Platform <protocol-definitions-ctp>` to tag the :ref:`Creatives <protocol-definitions-creative>`
  that remain under its control.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` calls :ref:`Site Tagging Platform <protocol-definitions-stp>` to verify tags assigned 
  to :ref:`Sites <protocol-definitions-site>` by :ref:`Supply-Side Platform <protocol-definitions-ssp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` calls :ref:`Context Platform <protocol-definitions-cp>` to retrieve 
  :ref:`Context Data <protocol-definitions-contextdata>` regarding :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>`
  and :ref:`Devices <protocol-definitions-device>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` receives :ref:`Impression Events <protocol-definitions-impression>` redirected to it by :ref:`Supply-Side Platform <protocol-definitions-ssp>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` responds to requests from :ref:`Supply-Side Platforms <protocol-definitions-ssp>` regarding :ref:`Payment Reports <protocol-definitions-paymentreport>`.

The following interactions remain outside of :ref:`Adshares Protocol <adshares-protocol>`:

* :ref:`Demand-Side Platform <protocol-definitions-dsp>` interacts with its :ref:`Ad Pay Module <protocol-definitions-apm>` to generate its
  :ref:`Payment Reports <protocol-definitions-paymentreport>`.
* :ref:`Demand-Side Platform <protocol-definitions-dsp>` interacts with its :ref:`Demand-Side Agent <protocol-definitions-dsa>` to receive notifications
  about :ref:`Conversion Events <protocol-definitions-conversion>`.

.. _protocol-definitions-dsp:

Demand-Side Platform
^^^^^^^^^^^^^^^^^^^^
An IT platform used by :ref:`Advertisers <protocol-definitions-advertiser>` to manage their :ref:`Campaigns <protocol-definitions-campaign>`. 
The demand-side module of an :ref:`AdServer <protocol-definitions-adserver>` is an example implementation of :ref:`Demand-Side Platform <protocol-definitions-dsp>`.

.. _protocol-definitions-dsa:

Demand-Side Agent
^^^^^^^^^^^^^^^^^
Executable code embedded by an :ref:`Advertiser <protocol-definitions-advertiser>` in a :ref:`Target <protocol-definitions-target>`. 
Each implementation of :ref:`Demand-Side Platform <protocol-definitions-dsp>` has its own implementation of :ref:`Demand-Side Agent <protocol-definitions-dsa>`. 
To be able to correctly redirect :ref:`User <protocol-definitions-user>`’s clicks, :ref:`Demand-Side Platform <protocol-definitions-dsp>` maintains a mapping 
between :ref:`Campaigns <protocol-definitions-campaign>` and their :ref:`Demand-Side Agents <protocol-definitions-dsa>`.

.. _protocol-definitions-apm:

Ad Pay Module
^^^^^^^^^^^^^
A module integrated with an instance of :ref:`Demand-Side Platform <protocol-definitions-dsp>`, or operating as an external service for
:ref:`Demand-Side Platform <protocol-definitions-dsp>`, containing business logic whose role is to manage the :ref:`Advertiser <protocol-definitions-advertiser>`'s 
finances, while optimizing the :ref:`Advertiser <protocol-definitions-advertiser>`'s cost.

.. note::
    :ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Demand-Side Agent <protocol-definitions-dsa>` are free to communicate in any way they choose, 
    as this communication is *not* part of :ref:`Adshares Protocol<adshares-protocol>`. Whereas the communication between 
    :ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Ad Pay Module <protocol-definitions-apm>` is included in :ref:`Adshares Protocol<adshares-protocol>`.