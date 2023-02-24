Sending payments
================

:ref:`Demand-Side Platform <protocol-definitions-dsp>` is expected to pay for displayed/converted advertisement by 
sending :ref:`ADS <protocol-definitions-ads>` to :ref:`Supply-Side Platform <protocol-definitions-ssp>` 
using :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

Every hour :ref:`Demand-Side Platform <protocol-definitions-dsp>` generates a :ref:`Payment Report <protocol-definitions-paymentreport>`
which allocates the appropriate amount of :ref:`ADS <protocol-definitions-ads>` that :ref:`Demand-Side Platform <protocol-definitions-dsp>` needs to pay 
to a specific :ref:`Supply-Side Platform <protocol-definitions-ssp>` for utilizing its :ref:`Sites <protocol-definitions-site>` within the last one-hour timeframe.

It is important for :ref:`Demand-Side Platform <protocol-definitions-dsp>` to store :ref:`Payment Reports <protocol-definitions-paymentreport>` 
because :ref:`Supply-Side Platform <protocol-definitions-ssp>` is expected to request those reports upon receiving payments.

To generate a :ref:`Payment Report <protocol-definitions-paymentreport>` for a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`, 
:ref:`Demand-Side Platform <protocol-definitions-dsp>` uses the following data:

* All :ref:`Impression Events <protocol-definitions-impression>` notifications received from all :ref:`Supply-Side Agents <protocol-definitions-ssa>` associated with a given :ref:`Supply-Side Platform <protocol-definitions-ssp>` within the last one-hour timeframe
* The corresponding :ref:`Context Data <protocol-definitions-contextdata>` retrieved from its :ref:`Context Infrastructure <protocol-definitions-contextinfrastructure>` in order to match those :ref:`Impression Events <protocol-definitions-impression>` with specific :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>` and :ref:`Devices <protocol-definitions-device>`

The recommended operation for sending :ref:`ADS <protocol-definitions-ads>` payments is :ref:`send_many <send_many>`.

.. container:: protocol

  Based on the data contained in the :ref:`Payment Report <protocol-definitions-paymentreport>`, :ref:`Demand-Side Platform <protocol-definitions-dsp>` uses 
  :ref:`Adshares Blockchain <protocol-definitions-blockchain>` to send an :ref:`ADS <protocol-definitions-ads>` payment to a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`,  
  by transferring the appropriate amount of :ref:`ADS <protocol-definitions-ads>` to the :ref:`Supply-Side Platform <protocol-definitions-ssp>`'s :ref:`ADS Account <protocol-definitions-account>` address.

.. note::
  :ref:`Demand-Side Platform <protocol-definitions-dsp>` knows the :ref:`ADS Account <protocol-definitions-account>` address of a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`, 
  as it has already been retrieved during the :doc:`Synchronization <../synchronization/index>` stage.
  