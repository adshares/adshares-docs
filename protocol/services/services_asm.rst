.. _protocol-services-asm:

Ad Select Service
-----------------

:ref:`Ad Select Module <protocol-definitions-asm>` contains the business logic aimed at selecting :ref:`Creatives <protocol-definitions-creative>` 
according to the :ref:`Publisher <protocol-definitions-publisher>`'s policy, while optimizing the :ref:`Publisher <protocol-definitions-publisher>`'s income.

:ref:`Ad Select Module <protocol-definitions-asm>` exposes an API, so that :ref:`Supply-Side Platform <protocol-definitions-ssp>` can call it 
in order to retrieve a list of :ref:`Creatives <protocol-definitions-creative>` for given :ref:`Context Data <protocol-definitions-contextdata>`.

:ref:`Ad Select Module <protocol-definitions-asm>` needs to be kept updated about payments received by :ref:`Supply-Side Platform <protocol-definitions-ssp>`
from various :ref:`Demand-Side Platforms <protocol-definitions-dsp>`, as this information might affect its future decisions on choosing 
:ref:`Creatives <protocol-definitions-creative>` from a particular :ref:`Demand-Side Platform <protocol-definitions-dsp>`.
