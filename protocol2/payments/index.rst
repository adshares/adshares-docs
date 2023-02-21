.. _protocol-payments:

Payments
========

:ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` needs to pay :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` 
for :ref:`Impression Events <protocol-definitions-impression>` and :ref:`Conversion Events <protocol-definitions-conversion>` that have taken place in a given time interval.

Sending payments
^^^^^^^^^^^^^^^^

Every hour :ref:`Demand-Side Platform <protocol-definitions-dsp>` generates a :ref:`Payment Report <protocol-definitions-paymentreport>`
which allocates the appropriate amount of :ref:`ADS <protocol-definitions-ads>` that :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to pay 
to a specific :ref:`Supply-Side Platform <protocol-definitions-ssp>` for utilizing its :ref:`Sites <protocol-definitions-site>` within the last one-hour timeframe.

To generate a :ref:`Payment Report <protocol-definitions-paymentreport>` for a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`, 
:ref:`Demand-Side Platform <protocol-definitions-dsp>` uses the following data:

* All :ref:`Impression Events <protocol-definitions-impression>` notifications received from all :ref:`Supply-Side Agents <protocol-definitions-ssa>` associated with a given :ref:`Supply-Side Platform <protocol-definitions-ssp>` within the last one-hour timeframe
* The corresponding :ref:`Context Data <protocol-definitions-contextdata>` retrieved from its :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` in order to match those :ref:`Impression Events <protocol-definitions-impression>` with specific :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>` and :ref:`Devices <protocol-definitions-device>`

.. container:: protocol

  Based on the data contained in the :ref:`Payment Report <protocol-definitions-paymentreport>`, :ref:`Demand-Side Platform <protocol-definitions-dsp>` uses 
  :ref:`Adshares Blockchain <protocol-definitions-blockchain>` to send an :ref:`ADS <protocol-definitions-ads>` payment to a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`,  
  by transferring the appropriate amount of :ref:`ADS <protocol-definitions-ads>` to the :ref:`Supply-Side Platform <protocol-definitions-ssp>`'s blockchain address.

.. note::
  :ref:`Demand-Side Platform <protocol-definitions-dsp>` knows the current blockchain address of a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`, 
  as it has already been retrieved during the :doc:`Synchronization <../synchronization/index>` stage.

Receiving payments
^^^^^^^^^^^^^^^^^^

:ref:`Supply-Side Platform <protocol-definitions-ssp>` monitors :ref:`Adshares Blockchain <protocol-definitions-blockchain>` by periodically retrieving the most recent transactions.

.. container:: protocol
  
  If an incoming payment is detected, :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls the appropriate :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  to receive its :ref:`Payment Report <protocol-definitions-paymentreport>`.

The received :ref:`Payment Report <protocol-definitions-paymentreport>` allows :ref:`Supply-Side Platform <protocol-definitions-ssp>` to verify the consistency between the following datasets:

* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` and the resulting payment amounts reported by :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>`
* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` and the resulting payment amounts expected by :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`

.. note::
  The above reconciliation only refers to :ref:`Impression Events <protocol-definitions-impression>`, while :ref:`Conversion Events <protocol-definitions-conversion>` 
  cannot be reconciled in this way, as they are not reported to :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`. 
  Nevertheless, :ref:`Demand-Side Platform <protocol-definitions-dsp>` might want to include :ref:`Conversion Events <protocol-definitions-conversion>` 
  in the :ref:`Payment Report <protocol-definitions-paymentreport>`, as this builds trust and incentivizes :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  to keep choosing the same :ref:`Demand-Side Platform <protocol-definitions-dsp>` in the future.