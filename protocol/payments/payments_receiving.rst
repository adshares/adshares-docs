.. _protocol-payments-receiving:

Receiving payments
==================

:ref:`Supply-Side Platform <protocol-definitions-ssp>` is expected to scan :ref:`Adshares Blockchain <protocol-definitions-blockchain>` 
for incoming :ref:`ADS <protocol-definitions-ads>` transfers.

.. container:: protocol
  
  If an incoming payment is detected, :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls the appropriate :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  to receive the corresponding :ref:`Payment Report <protocol-definitions-paymentreport>`.

The received :ref:`Payment Report <protocol-definitions-paymentreport>` allows :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
to verify the consistency between the following datasets:

* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` and the resulting payment amounts reported by :ref:`Demand-Side Platform <protocol-definitions-dsp>`
* :ref:`Impression Events <protocol-definitions-impression>`, the corresponding :ref:`Context Data <protocol-definitions-contextdata>` and the resulting payment amounts expected by :ref:`Supply-Side Platform <protocol-definitions-ssp>`

.. note::
  The above reconciliation only refers to :ref:`Impression Events <protocol-definitions-impression>`, while :ref:`Conversion Events <protocol-definitions-conversion>` 
  cannot be reconciled in this way, as they are only reported within :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>`, thus without :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` being inolved. 
  Nevertheless, the :ref:`Ad Pay Module <protocol-definitions-apm>` operating within :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` is incetivised to include :ref:`Conversion Events <protocol-definitions-conversion>` 
  in its :ref:`Payment Report <protocol-definitions-paymentreport>`, as this builds trust and incentivizes the :ref:`Ad Select Module <protocol-definitions-asm>` of a given :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
  to continue choosing the same :ref:`Demand-Side Platform <protocol-definitions-dsp>` in the future.

Refer to the following guides for furhter details:

* :ref:`Scan the blockchain for payments <protocol-payments-receiving-scan>`
* :ref:`Validate a transaction <protocol-payments-receiving-validate>`

.. toctree::
    :hidden:

    payments_receiving_execution
