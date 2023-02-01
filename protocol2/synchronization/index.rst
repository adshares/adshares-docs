Synchronization
===============

.. _protocol-synchronization:

To be able to interact with each other, :ref:`AdServers <protocol-definitions-adserver>` need to inform other :ref:`AdServers <protocol-definitions-adserver>` that they are accessible and what they offer. 
This information sharing is done by broadcasting via :ref:`Adshares Blockchain <protocol-definitions-blockchain>` a URL pointing to JSON-based metadata.

The URL is published on :ref:`Adshares Blockchain <protocol-definitions-blockchain>` in the form of an uppercase hexadecimal string.

.. note::
    Most programming languages have a utility to convert an ASCII string to its hex representation. Online converters can be used as well.

.. container:: protocol

    Every :ref:`AdServer <protocol-definitions-adserver>` broadcasts its metadata every 24 hours. 
    This means that if an :ref:`AdServer <protocol-definitions-adserver>` wants to collect information about other :ref:`AdServers <protocol-definitions-adserver>`, 
    it needs to check every block created within the last 24 hours for the presence of a URL. 
    Then, each URL needs to be verified if it actually points to an :ref:`AdServer <protocol-definitions-adserver>`'s metadata.

Within the metadata, the most important field is `inventoryUrl`, as it points to the current offering of an :ref:`AdServer <protocol-definitions-adserver>`: 
depending on the role of an AdServer, it is either :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>`, 
or :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>`, or both. 
Also, as this data is likely to change over time, it needs to be queried on a regular basis.

.. container:: protocol

    Using the endpoints contained in the `inventoryUrl` field:

    * :ref:`SSP <protocol-definitions-ssp>` retrieves :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` from all available :ref:`DSPs <protocol-definitions-dsp>`
    * :ref:`DSP <protocol-definitions-dsp>` retrieves :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` from all available :ref:`SSPs <protocol-definitions-ssp>`

.. note::
    In most ecosystems, :ref:`Advertisers <protocol-definitions-advertiser>` receive information about :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` 
    declared by :ref:`Publishers <protocol-definitions-publisher>`, and based on this information they offer their bids to buy advertising space. 
    However, in :ref:`Adshares Protocol<adshares-protocol2>` the opposite workflow is applied, i.e. :ref:`Publishers <protocol-definitions-publisher>` 
    collect information about :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` declared by :ref:`Advertisers <protocol-definitions-advertiser>`, 
    and based on this information they make a decision to whom they want to sell space on their :ref:`Sites <protocol-definitions-site>`.

In summary, here is why :ref:`SSPs <protocol-definitions-ssp>` and :ref:`DSPs <protocol-definitions-dsp>` might want to query each other:

* :ref:`Publishers <protocol-definitions-publisher>` query :ref:`Demand-Side Inventory <protocol-definitions-demandinventory>` when they want to sell their :ref:`Sites <protocol-definitions-site>` to :ref:`Advertisers <protocol-definitions-advertiser>`.
* :ref:`Advertisers <protocol-definitions-advertiser>` query :ref:`Supply-Side Inventory <protocol-definitions-supplyinventory>` when they want to define what :ref:`Sites <protocol-definitions-site>` they want to include or exclude from their :ref:`Campaign<protocol-definitions-campaign>` declarations.
