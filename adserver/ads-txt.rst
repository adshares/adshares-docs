
.. _adserver-ads-txt:

ads.txt
=======

The ads.txt file is a text file that contains a list of Authorized Digital Sellers.
It is used to prevent unauthorized entities from selling ad inventory in the name of a publisher.

Typical line consist of 4 fields separated by commas:

- ``domain`` - domain name of the advertising system
- ``publisher_id`` - unique identifier of the Authorized Digital Seller
- ``type`` - type of account/relationship between the publisher and advertising system
- ``certification_authority_id`` - optional unique identifier of the certificate authority

Full specification is available at (https://iabtechlab.com/ads-txt/).

AdServer ads.txt entry
----------------------

AdServer ads.txt entry can be found in AdPanel. Refer to :ref:`Setting up ads.txt<adserver-ads-txt-setting-up>`.

Below is a brief overview of the fields: 

- Field ``domain`` is the domain of AdServer.
- Field ``publisher_id`` is the user UUID.
- Field ``type`` is always ``DIRECT``.
- AdServer ads.txt entry omits the optional ``certification_authority_id`` field.

Example:

.. code-block:: text

    adserver.com, 12345678-1234-1234-1234-123456789012, DIRECT

.. _adserver-ads-txt-setting-up:

Setting up ads.txt
------------------

- Create a file named ``ads.txt`` in the root of your domain if it does not exist. This file must be publicly accessible.
- Log in to your AdPanel account and go to the site details page.
- Copy the entry from ads.txt frame and paste it into the ``ads.txt`` file.

.. note::

    All your sites shares the same ads.txt entry. You can use it for all your sites.
