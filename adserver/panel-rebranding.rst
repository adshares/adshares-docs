
Panel rebranding
================

This article describes how to change brand - dependent assets in `adpanel <https://github.com/adshares/adpanel>`_ project.

Requirements
^^^^^^^^^^^^

This article assumes that the `adcontroller <https://github.com/adshares/adcontroller>`_ project is installed.

Customize metadata and styling login page
^^^^^^^^^^^^^^^^^^

* Page metadata can be changed. In the adcontroller, on page ``/panel`` enter the data to be added. After refreshing the adpanel page, personalized data will appear in the appropriate tags

* You can also customize the login page by adding your own HTML and CSS code in the appropriate fields,

.. image:: /_static/images/change_metadata.png
   :target: /_static/images/change_metadata.png
   :alt: change panel metadata


Customize assets
^^^^^^^^^^^^^^^^

Content of image files can be changed. It is important to preserve file names and images sizes in pixels.

* **Required assets**: in the adcontroller, on page ``/panel`` in ``Required assets`` tab, you can select a new desired file. After saving changes will be added and will be available in the adpanel after page refresh.

.. image:: /_static/images/change_required_assets_tab.png
   :target: /_static/images/change_required_assets_tab.png
   :alt: change required assets tab

* **Additional assets**: in the adcontroller, on page ``/panel`` in ``Additional assets`` tab, you can select a new files and change existing ones. After uploading files will be added. For each file will be generate path with which this file can be used. If you change existing file, path will not change. If you upload a file named as an existing file, the existing file will be overwritten.

.. image:: /_static/images/change_additional_assets_tab.png
   :target: /_static/images/change_additional_assets_tab.png
   :alt: change additional assets tab

