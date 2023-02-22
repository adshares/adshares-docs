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