
How to add html banner
========================

With our AdServer you have the opportunity to upload banners in form of HTML files
with CSS files, animations, images (only local assets can be used and not links to outside sources) and basic JavaScript.

Adding an HTML Banner to an Existing Campaign
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can choose one of your existing campaigns by clicking its name on the ``My campaigns`` list.
A tab with the campaign info opens, click link ``Add new advertisement`` which leads to the ``Upload ads tab``.
Choose ``Add new advertisement``, a block with upload options will appear.

Adding an HTML Banner as a New Campaign
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can add a brand new campaign by pushing a ``Create new campaign`` button on the right-hand side of the top toolbar or by clicking ``Create new campaign`` link at the bottom of your campaigns list. After filling all the necessary targeting information a block with upload options will appear.

Ads Upload
----------

In the ``Upload ads`` block from ``Ad type`` dropdown menu choose ``Html`` option. If file name includes size of your banner the Adserver will detect it and set automatically, otherwise pick the right size from the ``Size`` drop-down menu.

Upload your HTML banner as a zip archive with a standard folder structure. You can do it by dragging the zip folder and dropping it inside the ``Drag & Drop`` spot or by clicking ``Browse`` and choosing a zip archive in file explorer.

Push ``Save & continue`` button to save the advertisement. You can also ``Save as draft`` and finish ad editing later or choose ``Delete ad unit`` to discard changes.

Folder Structure
^^^^^^^^^^^^^^^^

Place your images inside img folder, your css styling files inside css folder and files with fonts inside fonts.

.. image:: /_static/images/html_banner_dir_structure.jpg
   :target: /_static/images/html_banner_dir_structure.jpg
   :alt: css, img and fonts folder plus 'index.html' file


Index File
^^^^^^^^^^

Your index file should have a `valid HTML structure <https://validator.w3.org/>`_, with links to your styling sheets (e.g. 'main.css').

.. code-block:: html

       <!DOCTYPE html>
       <html lang="en">
       <head>
       <title>Page Title</title>

       <!-- stylesheet link -->
       <link rel="stylesheet" href="css/main.css">

       </head>
       <body>

       <h1>My Heading</h1>
       <p>My paragraph.</p>

       <!-- path to an image inside img folder -->
       <img src="img/my-product.jpg" alt="my product">

       </body>
       </html>
