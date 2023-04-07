.. _adserver-ads-txt:

ads.txt
=======

The ads.txt file is a text file that contains a list of Authorized Digital Sellers.
Adding an ads.txt record is essential for publishers looking to protect their ad inventory from fraud and to ensure that
they maintain control over their ad revenue.

Typical line consist of 4 fields separated by commas:

- ``domain`` - domain name of the advertising system
- ``publisher_id`` - unique identifier of the Authorized Digital Seller
- ``type`` - type of account/relationship between the publisher and advertising system
- ``certification_authority_id`` - optional unique identifier of the certificate authority

Full specification is available at (https://iabtechlab.com/ads-txt/).

Setting up ads.txt
------------------

#. Obtain your ads.txt information: log in to your AdPanel account and go to the site details page. Copy the entry from ads.txt frame.
#. Create an ads.txt file: Open a plain text editor such as Notepad (Windows) or TextEdit (Mac). Start a new file and paste in the ads.txt information copied from the panel. Each entry should be on a separate line and follow this format:

   .. code-block:: text

      <domain>, <publisher_id>, <type>

   For example:

   .. code-block:: text

      adserver.com, 1cd64871-8533-4fb9-b918-1d99e9b37e28, DIRECT

#. Save the ads.txt file: Save the file as ``ads.txt``. Make sure the file extension is ``.txt`` and not ``.txt.rtf`` or ``.txt.doc``.
#. Upload the ads.txt file to your web server: Use an FTP client, file manager, or your hosting control panel to access your website's root directory (also known as the public_html or www folder). Upload the ads.txt file to this directory. Ensure that the file is directly under your root domain (e.g., https://example.com/ads.txt).
#. Verify the ads.txt file is accessible: Open your browser and navigate to your website's ads.txt file by typing your domain followed by ``/ads.txt`` (e.g., https://example.com/ads.txt). You should see the contents of your ads.txt file displayed. If not, double-check the file location and ensure that you have uploaded it correctly.
#. AdServer will automatically verify the ads.txt file. Only after verification, the website will be activated and ads will be served.
#. Regularly update your ads.txt file: Whenever you add or remove ad partners or change your publisher ID, update your ``ads.txt`` file accordingly. This ensures that your ad revenue remains protected and that your ad partners have the most up-to-date information.

.. note::

    All your sites shares the same ads.txt entry. You can use it for all your sites.
