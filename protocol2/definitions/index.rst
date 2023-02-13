.. _protocol-definitions:

Definitions
===========

.. _protocol-definitions-objects:

Objects
-------

.. _protocol-definitions-creative:

Creative
^^^^^^^^
A digital advertisement.

.. _protocol-definitions-campaign:

Campaign
^^^^^^^^
A series of :ref:`Creatives <protocol-definitions-creative>` aimed to achieve a specific marketing goal.

.. _protocol-definitions-site:

Site
^^^^
A digital medium owned by a :ref:`Publisher <protocol-definitions-publisher>` where a :ref:`Creative <protocol-definitions-creative>` can be placed. 
Currently the following two media types are supported:

* web page,
* metaverse land parcel.

.. _protocol-definitions-placement:

Placement
^^^^^^^^^
A specific area within a :ref:`Site <protocol-definitions-site>` where a :ref:`Creative <protocol-definitions-creative>` is rendered.

.. _protocol-definitions-device:

Device
^^^^^^
The hardware the :ref:`User <protocol-definitions-user>` uses to access a :ref:`Site <protocol-definitions-site>`.

.. _protocol-definitions-target:

Target
^^^^^^
A website owned by an :ref:`Advertiser <protocol-definitions-advertiser>` which the :ref:`User <protocol-definitions-user>` is expected to visit 
as a result of interacting with a :ref:`Creative <protocol-definitions-creative>`. Also, :ref:`Target <protocol-definitions-target>` is the destination where 
the :ref:`User <protocol-definitions-user>` is redirected after clicking on a :ref:`Creative <protocol-definitions-creative>`.


.. _protocol-definitions-actors:

Actors
------

.. _protocol-definitions-publisher:

Publisher
^^^^^^^^^

A business entity that owns a :ref:`Site <protocol-definitions-site>`. :ref:`Publishers <protocol-definitions-publisher>` constitute the supply side of the market, 
as they generate supply of places where :ref:`Advertisers <protocol-definitions-advertiser>` can display their :ref:`Creatives <protocol-definitions-creative>`.

.. _protocol-definitions-advertiser:

Advertiser
^^^^^^^^^^

A business entity that runs a :ref:`Campaign <protocol-definitions-campaign>`. :ref:`Advertisers <protocol-definitions-advertiser>` constitute the demand side of the market, 
as they generate demand for places where they can display their :ref:`Creatives <protocol-definitions-creative>`.

.. _protocol-definitions-user:

User
^^^^

A person expected to view or interact with a :ref:`Creative <protocol-definitions-creative>` when browsing through a :ref:`Site <protocol-definitions-site>`.

.. _protocol-definitions-ssi:

Supply-Side Infrastructure
--------------------------

.. _protocol-definitions-ssp:

Supply-Side Platform
^^^^^^^^^^^^^^^^^^^^
An IT platform used by :ref:`Publishers <protocol-definitions-publisher>` to manage their :ref:`Sites <protocol-definitions-site>`. 
The supply-side module of an :ref:`AdServer <protocol-definitions-adserver>` is an example implementation of :ref:`Supply-Side Platform <protocol-definitions-ssp>`.

.. _protocol-definitions-ssa:

Supply-Side Agent
^^^^^^^^^^^^^^^^^
Executable code embedded by a :ref:`Publisher <protocol-definitions-publisher>` in a :ref:`Site <protocol-definitions-site>`. 
Each implementation of :ref:`Supply-Side Platform <protocol-definitions-ssp>` has its own implementation of :ref:`Supply-Side Agent <protocol-definitions-ssa>`.

.. _protocol-definitions-asm:

Ad Select Module
^^^^^^^^^^^^^^^^
A module integrated with an instance of :ref:`Supply-Side Platform <protocol-definitions-ssp>`, or operating as an external service for :ref:`Supply-Side Platform <protocol-definitions-ssp>`, 
containing business logic whose role is to select :ref:`Creatives <protocol-definitions-creative>` according to the :ref:`Publisher <protocol-definitions-publisher>`'s policy, while maximizing the :ref:`Publisher <protocol-definitions-publisher>`'s income.

.. note::
    :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Supply-Side Agent <protocol-definitions-ssa>` are free to communicate in any way they choose, 
    as this communication is *not* part of :ref:`Adshares Protocol<adshares-protocol2>`. 
    Whereas the communication between :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Ad Select Module <protocol-definitions-asm>` is included in :ref:`Adshares Protocol<adshares-protocol2>`.


.. _protocol-definitions-dsi:

Demand-Side Infrastructure
--------------------------

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
between :ref:`Campaigns<protocol-definitions-campaign>` and their :ref:`DSAs <protocol-definitions-dsa>`.

.. _protocol-definitions-apm:

Ad Pay Module
^^^^^^^^^^^^^
A module integrated with an instance of :ref:`Demand-Side Platform <protocol-definitions-dsp>`, or operating as an external service for :ref:`Demand-Side Platform <protocol-definitions-dsp>`, 
containing business logic whose role is to manage the :ref:`Advertiser <protocol-definitions-advertiser>`'s finances, while minimizing the :ref:`Advertiser <protocol-definitions-advertiser>`'s cost.

.. note::
    :ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Demand-Side Agent <protocol-definitions-dsa>` are free to communicate in any way they choose, 
    as this communication is *not* part of :ref:`Adshares Protocol<adshares-protocol2>`. Whereas the communication 
    between :ref:`Demand-Side Platform <protocol-definitions-dsp>` and :ref:`Ad Pay Module <protocol-definitions-apm>` is included in :ref:`Adshares Protocol<adshares-protocol2>`.


.. _protocol-definitions-contextinfrastructure:

Context Infrastructure
----------------------

.. _protocol-definitions-cp:

Context Platform
^^^^^^^^^^^^^^^^
An IT platform whose role is to collect & manage data about :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>` 
and :ref:`Devices <protocol-definitions-device>`, and respond with packages of :ref:`Context Data <protocol-definitions-contextdata>` to queries about the properties of 
a specific :ref:`User <protocol-definitions-user>`, :ref:`Site <protocol-definitions-site>` or :ref:`Device <protocol-definitions-device>`.

Internally, :ref:`Context Platform <protocol-definitions-cp>` might consist of sub-modules, such as:

.. _protocol-definitions-ucp:

User Context Platform
"""""""""""""""""""""
An IT platform whose role is to collect & manage data about :ref:`Users <protocol-definitions-user>` 
and respond with packages of :ref:`Context Data <protocol-definitions-contextdata>` to queries about properties of a specific :ref:`User <protocol-definitions-user>`.

.. _protocol-definitions-scp:

Site Context Platform
"""""""""""""""""""""
An IT platform whose role is to collect & manage data about :ref:`Sites <protocol-definitions-site>` 
and respond with packages of :ref:`Context Data <protocol-definitions-contextdata>` to queries about properties of a specific :ref:`Site <protocol-definitions-site>`.

.. _protocol-definitions-dcp:

Device Context Platform
"""""""""""""""""""""""
An IT platform whose role is to collect & manage data about :ref:`Devices <protocol-definitions-device>` 
and respond with packages of :ref:`Context Data <protocol-definitions-contextdata>` to queries about properties of a specific :ref:`Device <protocol-definitions-device>`.

.. note::
    :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>` need to decide 
    which instances of :ref:`Context Platform <protocol-definitions-cp>` they trust and independently query them. 
    Even if :ref:`Supply-Side Platform <protocol-definitions-ssp>` and :ref:`Demand-Side Platform <protocol-definitions-dsp>` end up trusting 
    the same instance of :ref:`Context Platform <protocol-definitions-cp>`, they need to query it separately.


.. _protocol-definitions-tagginginfrastructure:

Tagging Infrastructure
----------------------

.. _protocol-definitions-stp:

Site Tagging Platform
^^^^^^^^^^^^^^^^^^^^^
An IT platform whose role is to classify :ref:`Sites <protocol-definitions-site>` 
by assigning tags to them and respond to queries about tags for a specific :ref:`Site <protocol-definitions-site>`.

.. _protocol-definitions-ctp:

Creative Tagging Platform
^^^^^^^^^^^^^^^^^^^^^^^^^
An IT platform whose role is to classify :ref:`Creatives <protocol-definitions-creative>` 
by assigning tags to them and respond to queries about tags for a specific :ref:`Creative <protocol-definitions-creative>`.

.. note::
    It's up to :ref:`Supply-Side Platform <protocol-definitions-ssp>` to choose the appropriate :ref:`Site Tagging Platform <protocol-definitions-stp>` service, 
    but this choice should be acceptable for :ref:`Demand-Side Platform <protocol-definitions-dsp>`. 
    Similarly, it's up to :ref:`Demand-Side Platform <protocol-definitions-dsp>` to choose the appropriate :ref:`Creative Tagging Platform<protocol-definitions-ctp>` service, 
    but this choice should be acceptable for :ref:`Supply-Side Platform <protocol-definitions-ssp>`.

.. note::
    When queried, both :ref:`Site Tagging Platform <protocol-definitions-stp>` and :ref:`Creative Tagging Platform<protocol-definitions-ctp>` should sign their responses with private keys, 
    so that the tags assigned to :ref:`Sites <protocol-definitions-site>` or :ref:`Creatives <protocol-definitions-creative>` remain cryptographically verifiable. 
    This way there is no need to invoke the same query multiple times, as long as an :ref:`Supply-Side Platform <protocol-definitions-ssp>` trusts a :ref:`Creative Tagging Platform<protocol-definitions-ctp>` service 
    chosen by a :ref:`Demand-Side Platform <protocol-definitions-dsp>`, or a :ref:`Demand-Side Platform <protocol-definitions-dsp>` trusts an :ref:`Site Tagging Platform <protocol-definitions-stp>` service chosen by an :ref:`Supply-Side Platform <protocol-definitions-ssp>`.


.. _protocol-definitions-datastructures:

Data Structures
---------------

.. _protocol-definitions-supplyinventory:

Supply-Side Inventory
^^^^^^^^^^^^^^^^^^^^^
A manifest describing the parameters of a :ref:`Site <protocol-definitions-site>` currently offered by a :ref:`Publisher <protocol-definitions-publisher>`, e.g. topic, prevailing audience etc.

.. _protocol-definitions-demandinventory:

Demand-Side Inventory
^^^^^^^^^^^^^^^^^^^^^
A manifest describing the parameters of a :ref:`Campaign <protocol-definitions-campaign>` currently run 
by an :ref:`Advertiser <protocol-definitions-advertiser>`, e.g. time duration, target audience, pricing policy etc.

.. _protocol-definitions-creativecontent:

Creative Content
^^^^^^^^^^^^^^^^
Digital assets (e.g. images, videos etc) needed to render a :ref:`Creative <protocol-definitions-creative>` 
inside its designated :ref:`Placement <protocol-definitions-placement>`.

.. _protocol-definitions-contextdata:

Context Data
^^^^^^^^^^^^
A package of data describing a :ref:`User <protocol-definitions-user>`, a :ref:`Site <protocol-definitions-site>` or a :ref:`Device <protocol-definitions-device>`.

.. _protocol-definitions-contextscript:

Context Script
^^^^^^^^^^^^^^
Executable code generated by :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>`, 
and executed inside a sandbox created by :ref:`Supply-Side Agent <protocol-definitions-ssa>` within the context of a :ref:`Site <protocol-definitions-site>`.

.. _protocol-definitions-paymentreport:

Payment Report
^^^^^^^^^^^^^^
A standardized report generated by :ref:`Demand-Side Platform <protocol-definitions-dsp>` that presents the business context for the payments sent (within a given time interval) 
from :ref:`Demand-Side Platform <protocol-definitions-dsp>` to :ref:`Supply-Side Platform <protocol-definitions-ssp>`.

.. note::
    In most ecosystems the term *inventory* refers only to the supply side of the market, i.e. what :ref:`Publishers<protocol-definitions-publisher>` 
    offer for sale and the minimum price they are willing to accept from :ref:`Advertisers <protocol-definitions-advertiser>`. 
    However, in :ref:`Adshares Protocol <adshares-protocol2>` this term has a more generic meaning, as it refers to assets that belong to either side of the market, 
    i.e. :ref:`Publishers<protocol-definitions-publisher>` or :ref:`Advertisers <protocol-definitions-advertiser>`.


.. _protocol-definitions-events:

Events
------

.. _protocol-definitions-impression:

Impression Event
^^^^^^^^^^^^^^^^
An event emitted by :ref:`Supply-Side Agent <protocol-definitions-ssa>` when a :ref:`User <protocol-definitions-user>` interacts with a :ref:`Site <protocol-definitions-site>`. 
There are three types of :ref:`Impression Events <protocol-definitions-impression>`:

.. _protocol-definitions-registerevent:

Register Event
""""""""""""""
Emitted when a :ref:`User <protocol-definitions-user>` navigates to a :ref:`Site <protocol-definitions-site>`.

.. _protocol-definitions-viewevent:

View Event
""""""""""
Emitted when a :ref:`Creative <protocol-definitions-creative>` is rendered on a :ref:`User <protocol-definitions-user>`'s screen.

.. _protocol-definitions-clickevent:

Click Event
"""""""""""
Emitted when a :ref:`User <protocol-definitions-user>` interacts with a :ref:`Creative <protocol-definitions-creative>` by clicking on it.

.. _protocol-definitions-conversion:

Conversion Event
^^^^^^^^^^^^^^^^
An event emitted by :ref:`Demand-Side Agent <protocol-definitions-dsa>` when a :ref:`User <protocol-definitions-user>` performs an action while browsing a :ref:`Target <protocol-definitions-target>`.


.. _protocol-definitions-ecosystem:

Adshares Ecosystem
------------------

.. _protocol-definitions-adserver:

AdServer
^^^^^^^^
A publicly accessible server combining the following functionality:

* :ref:`Supply-Side Platform <protocol-definitions-ssp>`, including :ref:`Ad Select Module <protocol-definitions-asm>`
* :ref:`Demand-Side Platform <protocol-definitions-dsp>`, including :ref:`Ad Pay Module <protocol-definitions-apm>`
* :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>`


.. _protocol-definitions-blockchain:

Adshares Blockchain
^^^^^^^^^^^^^^^^^^^
The underlying blockchain of :ref:`Adshares Protocol <adshares-protocol2>`.

.. _protocol-definitions-ads:

ADS
^^^
The native currency of :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.