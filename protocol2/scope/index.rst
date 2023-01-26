Scope
=====

.. _protocol-scope:

Lorem Ipsum
-----------

Those are the four main areas handled by *Adshares Protocol*:

Authentication
^^^^^^^^^^^^^^
How various entities participating in *Adshares Protocol* authenticate each other.

Synchronization
^^^^^^^^^^^^^^^
#. How :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` and :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` uses :ref:`Adshares Blockchain <protocol-definitions-blockchain>` to broadcast an URL indicating their current availability.
    .. * exposed by: :ref:`bla bla <protocol-definitions-creative>`
    .. * consumed by: :ref:`foo abr <protocol-definitions-campaign>`

#. How Demand-Side Infrastructure exposes inventory data:
    * exposed by: *DSP*
    * consumed by: *SSP*
    * returns: *Demand-Side Inventory*

#. How Supply-Side Infrastructure exposes inventory data:
    - exposed by: *SSP*
    - consumed by: *DSP*
    - returns: *Supply-Side Inventory*

Impressions
^^^^^^^^^^^
1. How *Context Infrastructure* exposes context data:
    - exposed by: *UCP*, *SCP*, *DCP*
    - consumed by: *SSP* and *DSP*
    - returns: *Context Data*

2. How *Demand-Side Infrastructure* exposes content data:
    - exposed by: *DSP*
    - consumed by: *SSA*
    - returns: *Creative Content*

3. How *Context Infrastructure* accepts notifications about *Register*-type impression events:
    - exposed by: *UCP*, *SCP*, *DCP*
    - consumed by: *SSA*
    - returns: *Context Script*

4. How *Demand-Side Infrastructure* accepts notifications about *View*-type or *Click*-type impression events:
    - exposed by: *DSP*
    - consumed by: *SSA*
    - returns: endpoints for *UCP*, *SCP*, *DCP*

Payments
^^^^^^^^
1. How *Demand-Side Infrastructure* uses *Adshares Blockchain* to send payments to *Supply-Side Infrastructure*:
    - payer: *DSP*
    - payee: *SSP*

2. How *Demand-Side Infrastructure* exposes payment reports:
    - exposed by: *DSP*
    - consumed by: *SSP*
    - returns: *Payment Report*