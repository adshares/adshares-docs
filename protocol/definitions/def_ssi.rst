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
A module integrated with an instance of :ref:`Supply-Side Platform <protocol-definitions-ssp>`, or operating as an external service for 
:ref:`Supply-Side Platform <protocol-definitions-ssp>`, containing business logic whose role is to select :ref:`Creatives <protocol-definitions-creative>` 
according to the :ref:`Publisher <protocol-definitions-publisher>`'s policy, while optimizing the :ref:`Publisher <protocol-definitions-publisher>`'s income.
