Payments
========

.. _protocol-payments:

:ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` needs to pay 
:ref:`Supply-Side Infrastructure <protocol-definitions-ssi>` for displayed or converted :ref:`Creatives <protocol-definitions-creative>`.

Sending payments
^^^^^^^^^^^^^^^^

Every hour :ref:`Demand-Side Platform <protocol-definitions-dsp>` generates a :ref:`Payment Report <protocol-definitions-paymentreport>`, 
and, based on the results of this report, it calculates the payment amounts to be sent to the appropriate :ref:`SSPs <protocol-definitions-ssp>` for 
utilizing their :ref:`Sites <protocol-definitions-site>` within the most recent one-hour timeframe. 

.. container:: protocol

  If :ref:`Demand-Side Platform <protocol-definitions-dsp>` finds out that it owes money to an instance of :ref:`Supply-Side Platform <protocol-definitions-ssp>`, it transfers to the :ref:`Supply-Side Platform <protocol-definitions-ssp>`'s 
  blockchain address the appropriate amount of :ref:`ADS <protocol-definitions-ads>` using :ref:`Adshares Blockchain <protocol-definitions-blockchain>`.

Receiving payments
^^^^^^^^^^^^^^^^^^

:ref:`Supply-Side Platform <protocol-definitions-ssp>` monitors :ref:`Adshares Blockchain <protocol-definitions-blockchain>` by periodically retrieving the most recent transactions.

.. container:: protocol
  
  If an incoming payment is detected, :ref:`Supply-Side Platform <protocol-definitions-ssp>` calls the appropriate :ref:`Demand-Side Platform <protocol-definitions-dsp>` to retrieve a :ref:`Payment Report <protocol-definitions-paymentreport>`.

Te received :ref:`Payment Report <protocol-definitions-paymentreport>` allows :ref:`Supply-Side Platform <protocol-definitions-ssp>` to verify if the events (and corresponding payment amounts) 
reported by :ref:`Demand-Side Infrastructure <protocol-definitions-dsi>` match the events (and corresponding payment amounts) observed by :ref:`Supply-Side Infrastructure <protocol-definitions-ssi>`.
