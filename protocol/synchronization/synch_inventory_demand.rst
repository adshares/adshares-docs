.. _protocol-synchronization-demandinventory:

Demand-Side Inventory
=====================

Each :ref:`Demand-Side Platform <protocol-definitions-dsp>` is expected to expose its :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`
under the URL contained in the ``inventoryUrl`` field, as defined in the :ref:`Metadata Format <protocol-synchronization-metadata>`.

The URL published under the ``inventoryUrl`` field should support the ``limit`` and ``offset`` query parameters for pagination.

The data returned by the above URL should implement the :ref:`Demand-Side Inventory Format <protocol-synchronization-demandinventory-format>`.

.. toctree::
    :hidden:

    synch_inventory_demand_format

::

    **TODO** https://adshares.atlassian.net/browse/ACP-7
