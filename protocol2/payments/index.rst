Payments
========

.. _protocol-payments:

:ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` needs to pay 
:ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` for displayed/converted :ref:`Creatives <protocol-definitions-creative>`.

Every hour :ref:`DSP <protocol-definitions-dsp>` generates a :ref:`Payment Report <protocol-definitions-paymentreport>`, 
and, based on the results of this report, it calculates the payment amounts to be sent to the appropriate :ref:`SSPs <protocol-definitions-ssp>` for 
utilizing their :ref:`Sites <protocol-definitions-site>` within the most recent one-hour timeframe. 

.. container:: protocol

  Then, :ref:`DSP <protocol-definitions-dsp>` transfers to each :ref:`SSP <protocol-definitions-ssp>` the appropriate 
  amount of :ref:`ADS <protocol-definitions-ads>` using :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

Periodically, :ref:`SSP <protocol-definitions-ssp>` retrieves transactions from :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

.. container:: protocol
  
  Then, if an inbound payment is found, :ref:`SSP <protocol-definitions-ssp>` calls the appropriate :ref:`DSP <protocol-definitions-dsp>` to retrieve a :ref:`Payment Report <protocol-definitions-paymentreport>`.

In summary, :ref:`Payment Report <protocol-definitions-paymentreport>` allows :ref:`SSP <protocol-definitions-ssp>` to verify if the events (and corresponding payment amounts) 
reported by :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` match the events (and corresponding payment amounts) observed by :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`.
