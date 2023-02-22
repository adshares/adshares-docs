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
