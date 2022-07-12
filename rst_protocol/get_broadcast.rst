
See others – fetch broadcasts
======================================
Before connecting to other adservers it is crucial to find them in the network.
Every adserver broadcasts it's metadata using ADS blockchain every 12 hours.
This means that each block from last 12 hours must be checked for the presence of an URL.
Then, each URL must be checked to see if it points to the adserver metadata.
To check expected format of adserver's metadata read :ref:`Adserver's metadata <adserver_metadata>`.
Save ``inventoryUrl`` and ``adsAddress`` from each metadata.
