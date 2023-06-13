.. _protocol-definitions-objects:

Objects
-------

.. _protocol-definitions-creative:

Creative
^^^^^^^^
A digital advertisement. Each :ref:`Creative <protocol-definitions-creative>` is expected to be classified by one or more :ref:`Creative Tagging Providers <protocol-definitions-ctp>`.

.. _protocol-definitions-campaign:

Campaign
^^^^^^^^
A series of :ref:`Creatives <protocol-definitions-creative>` aimed to achieve a specific marketing goal.

Each :ref:`Campaign <protocol-definitions-campaign>` has a defined date range during which it is active and the maximum amount it can pay up to.
Each :ref:`Campaign <protocol-definitions-campaign>` consists of one or more :ref:`Creatives <protocol-definitions-creative>` of different type and size.

.. _protocol-definitions-site:

Site
^^^^
A digital medium owned by a :ref:`Publisher <protocol-definitions-publisher>` where a :ref:`Creative <protocol-definitions-creative>` can be placed. 
Each :ref:`Site <protocol-definitions-site>` is expected to be classified by one or more :ref:`Site Tagging Providers <protocol-definitions-stp>`.

Currently, :ref:`Sites <protocol-definitions-site>` featuring the following two media types are supported:

* web page,
* metaverse land parcel.

.. _protocol-definitions-placement:

Placement
^^^^^^^^^
A specific area within a :ref:`Site <protocol-definitions-site>` where a :ref:`Creative <protocol-definitions-creative>` is rendered.

.. _protocol-definitions-device:

Device
^^^^^^
The means the :ref:`User <protocol-definitions-user>` uses to access a :ref:`Site <protocol-definitions-site>`, 
including both software and hardware, e.g. desktop web browser, mobile web browser, mobile app etc.

.. _protocol-definitions-target:

Target
^^^^^^
A website owned by an :ref:`Advertiser <protocol-definitions-advertiser>` which :ref:`User <protocol-definitions-user>` is expected to visit 
as a result of interacting with a :ref:`Creative <protocol-definitions-creative>`. Also, :ref:`Target <protocol-definitions-target>` is the destination where 
the :ref:`User <protocol-definitions-user>` is redirected after clicking on a :ref:`Creative <protocol-definitions-creative>`.