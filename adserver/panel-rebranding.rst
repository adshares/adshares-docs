
Panel rebranding
================

This article describes how to change brand - dependent assets in `adpanel <https://github.com/adshares/adpanel>`_ project.

Requirements
^^^^^^^^^^^^

This article assumes that the environmental variables are defined:

* ``ADPANEL_PARENT_DIR`` - directory in which adpanel project is cloned
* ``BRAND_ASSETS_DIR`` - directory in which custom assets will be stored. It should be placed outside project directory to ensure that files will not be deleted
* ``COPY_BRAND_ASSETS`` - switch enabling assets change, should be ``Y`` for enable,

Collect assets
^^^^^^^^^^^^^^

Brand - dependent assets are icons and logos in different sizes for different screens.
They are stored inside adpanel ``src`` directory.

Copy project assets to own directory.

.. code-block::

   cp ${ADPANEL_PARENT_DIR}/adpanel/src/favicon* ${BRAND_ASSETS_DIR}
   cp ${ADPANEL_PARENT_DIR}/adpanel/src/assets/images/logo* ${BRAND_ASSETS_DIR}

Customize assets
^^^^^^^^^^^^^^^^

Content of image files can be changed. It is important to preserve file names and images' sizes in pixels.

Build adpanel
^^^^^^^^^^^^^

The adpanel project must be rebuild to properly replace Adshares assets with custom.

If you use interactive installer, you will be asked if you want to copy brand assets inside project directory.
In case of automatic installer two environment variables should be set. They were mentioned in `Requirements <#requirements>`_


* ``COPY_BRAND_ASSETS`` should be ``Y``
* ``BRAND_ASSETS_DIR`` should be full path to assets directory

Files from custom assets directory will overwrite the standard files.
