.. _protocol-synchronization-sendbroadcast:

Sending broadcasts
==================

To become a part of the network :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
need to inform other :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` that they are accessible.

This is done on :ref:`ADS Blockchain <protocol-definitions-blockchain>` by broadcasting 
a URL pointing to :ref:`Platform Metadata <protocol-definitions-metadata>`.

Every 24 hours, all :ref:`Supply-Side Platforms <protocol-definitions-ssp>` and :ref:`Demand-Side Platforms <protocol-definitions-dsp>` 
are required to broadcast a URL pointing to their :ref:`Platform Metadata <protocol-definitions-metadata>`. 

.. note::

    Broadcast must be sent from the account declared in the ``adsAddress`` field, as defined in the :ref:`Metadata Fromat <protocol-synchronization-metadata>`.

The URL itself, as well as :

URL Format
^^^^^^^^^^

The URL is published on :ref:`ADS Blockchain <protocol-definitions-blockchain>` in the form of an uppercase hexadecimal string.

.. note::
    Most programming languages have a utility to convert an ASCII string to its hex representation. Online converters can be used as well.

The encoded URL is the message to be broadcast.

Example URL::

  https://app.example.com/info.json

Example URL after encoding::

  68747470733A2F2F6170702E6578616D706C652E636F6D2F696E666F2E6A736F6E

Metadata Format
^^^^^^^^^^^^^^^

:ref:`Platform Metadata <protocol-definitions-metadata>` needs to be published in :ref:`Metadata Format <protocol-synchronization-metadata>`.


How to broadcast
^^^^^^^^^^^^^^^^
Broadcasting is done via :ref:`ADS CLI Client <ads-api>` by running the :ref:`broadcast <broadcast>` command. 

You can also run the above command by using the following alternative methods:

* Use :ref:`ADS PHP Client <ads-php-client>`
* Use :ref:`ADS JSON RPC <ads-json-rpc>`
