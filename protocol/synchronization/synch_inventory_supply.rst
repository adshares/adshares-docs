.. _protocol-synchronization-supplyinventory:

Supply-Side Inventory
=====================

Each :ref:`Supply-Side Platform <protocol-definitions-ssp>` is expected to expose its :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`
under the URL contained in the ``inventoryUrl`` field, as defined in the :ref:`Metadata Format <protocol-synchronization-metadata>`.

The URL published under the ``inventoryUrl`` field should support the ``limit`` and ``offset`` query parameters for pagination.

The data returned by the above URL should implement the :ref:`Supply-Side Inventory Format <protocol-synchronization-supplyinventory-format>`.

.. toctree::
    :hidden:

    synch_inventory_supply_format