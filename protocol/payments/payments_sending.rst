.. _protocol-payments-sending:

Sending Payments
================

The following diagram presents an overview of how :ref:`Demand-Side Platform <protocol-definitions-dsp>` sends
payments to corresponding :ref:`Supply-Side Platforms <protocol-definitions-ssp>`:

.. uml::
    :align: center

    skinparam monochrome true

    participant "ADS Blockchain"                    as blockchain
    participant "Demand-Side\nPlatform"             as DSP
    participant "Demand-Side\nContext Provider"     as DSCP
    participant "Ad Pay\nModule"                    as APM
    actor       "Advertiser"                        as advertiser

    advertiser -> DSP: Deposit funds
    loop every 1 hour
        DSP -> DSCP: Get\nUser/Site/Device\nContext
        DSCP --> DSP: User/Site/Device\nContext
        DSP -> APM: Post User/Site/Device\nContext
        DSP -> APM: Post Impression Events
        DSP -> APM: Generate Payment Report
        APM --> DSP: Payment Report
        DSP -> DSP: Calculate payments
        DSP -> blockchain: Send multi transaction
    end

:ref:`Demand-Side Platform <protocol-definitions-dsp>` is expected to pay for displayed/converted :ref:`Creatives <protocol-definitions-creative>`
by sending :ref:`ADS <protocol-definitions-ads>` payments to all :ref:`Supply-Side Platforms <protocol-definitions-ssp>` that have been involved
in displaying those :ref:`Creatives <protocol-definitions-creative>` to the :ref:`User <protocol-definitions-user>`.

To fulfill those payments, every hour :ref:`Demand-Side Platform <protocol-definitions-dsp>` generates a :ref:`Payment Report <protocol-definitions-paymentreport>`
which allocates the appropriate amount of :ref:`ADS <protocol-definitions-ads>` that it needs to pay to :ref:`Supply-Side Platforms <protocol-definitions-ssp>`
for utilizing their :ref:`Sites <protocol-definitions-site>` within the last one-hour timeframe.

It's important for :ref:`Demand-Side Platform <protocol-definitions-dsp>` to store the generated :ref:`Payment Reports <protocol-definitions-paymentreport>` 
because :ref:`Supply-Side Platforms <protocol-definitions-ssp>` are expected to request those reports upon receiving their payments.

The actual task of generating the :ref:`Payment Report <protocol-definitions-paymentreport>` can be done by :ref:`Demand-Side Platform <protocol-definitions-dsp>`
itself, or it might be outsourced by :ref:`Demand-Side Platform <protocol-definitions-dsp>` to an external :ref:`Ad Pay Module <protocol-definitions-apm>`.

In case an external :ref:`Ad Pay Module <protocol-definitions-apm>` is utilized, :ref:`Ad Pay Module <protocol-definitions-apm>` needs to receive 
from :ref:`Demand-Side Platform <protocol-definitions-dsp>` the following information:

* All :ref:`Impression Events <protocol-definitions-impression>` received by :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  from all :ref:`Supply-Side Agents <protocol-definitions-ssa>` within the last one-hour timeframe.
* The corresponding :ref:`Context Data <protocol-definitions-contextdata>` retrieved by :ref:`Demand-Side Platform <protocol-definitions-dsp>` 
  from its :ref:`Context Provider <protocol-definitions-cp>` in order to match those :ref:`Impression Events <protocol-definitions-impression>`
  with specific :ref:`Users <protocol-definitions-user>`, :ref:`Sites <protocol-definitions-site>` and :ref:`Devices <protocol-definitions-device>`.

The details of the communication between :ref:`Demand-Side Platform <protocol-definitions-dsp>` and its :ref:`Ad Pay Module <protocol-definitions-apm>`
are described in the :ref:`Ad Pay Service <protocol-services-apm>` section.

:ref:`Ad Pay Module <protocol-definitions-apm>` verifies the received :ref:`Impression Events <protocol-definitions-impression>`, and the outcome
of this verification is contained in the :ref:`Payment Report <protocol-definitions-paymentreport>`, i.e. :ref:`Ad Pay Module <protocol-definitions-apm>`
includes a payment for an :ref:`Impression Events <protocol-definitions-impression>` in the :ref:`Payment Report <protocol-definitions-paymentreport>` 
only if it's able to verify that the event has actually occured and was valid (not fake).

The generated :ref:`Payment Report <protocol-definitions-paymentreport>` becomes the basis for 
:ref:`Demand-Side Platform <protocol-definitions-dsp>` to proceed with executing payments. Payments are executed by 
:ref:`Demand-Side Platform <protocol-definitions-dsp>` sending an :ref:`ADS <protocol-definitions-ads>` amount to a given 
:ref:`Supply-Side Platform <protocol-definitions-ssp>`, i.e. transferring the appropriate amount of :ref:`ADS <protocol-definitions-ads>` 
to the :ref:`Supply-Side Platform <protocol-definitions-ssp>`'s :ref:`ADS Account <protocol-definitions-account>` address.

.. note::
  :ref:`Demand-Side Platform <protocol-definitions-dsp>` knows the :ref:`ADS Account <protocol-definitions-account>` 
  address of a given :ref:`Supply-Side Platform <protocol-definitions-ssp>`, as it has already been retrieved 
  during the :doc:`Synchronization <../synchronization/index>` stage.
  
The recommended operation for sending :ref:`ADS <protocol-definitions-ads>` payments is :ref:`send_many <send_many>`.
