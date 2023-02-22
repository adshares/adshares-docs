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
    This way there is no need to invoke the same query multiple times, as long as :ref:`Supply-Side Platform <protocol-definitions-ssp>` trusts :ref:`Creative Tagging Platform<protocol-definitions-ctp>` service 
    chosen by :ref:`Demand-Side Platform <protocol-definitions-dsp>`, or :ref:`Demand-Side Platform <protocol-definitions-dsp>` trusts :ref:`Site Tagging Platform <protocol-definitions-stp>` service chosen by :ref:`Supply-Side Platform <protocol-definitions-ssp>`.