
.. _how-to-start-adserver:

How to start AdServer
======================

.. note::

    We strongly recommend using DNS with traffic proxy and DDoS protection (e.g. `Cloudflare <https://www.cloudflare.com/>`_).

Setup requirements:
^^^^^^^^^^^^^^^^^^^

* Domain with 3 subdomains:

  *
    Frontend domain (default: ``panel.example.com``)

    *It is used to manage campaigns, sites and adserver itself.*

  *
    Backend domain (default: ``app.example.com``)

    *It is used for API and for serving banner files to publishers.*

  *
    2nd Backend domain (default: ``au.example.com``)

    *It is used for gathering request context.*

* Server to run application (specifications `below <#server-minimum-requirements>`_)
* SMTP server/account for sending e-mails (e.g. Amazon SES)
* ADS Account (e.g. from `ADS Wallet <https://adshares.net/wallet>`_)

Server minimum requirements:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Operating system: **Ubuntu 20.04**
* RAM: **8 GB**
* Storage: **SSD**, **500 GB**, *heavily depends on traffic*
* CPU: **x64**, **4 cores**

Installation
------------

#. Install `Ansible <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>`_ (locally)
#. Install `Adshares adservice role <https://galaxy.ansible.com/adshares/adservice>`_ (locally)

    ``ansible-galaxy install adshares.adservice``

#. Use example playbook to install AdServer modules (locally).
   All available variables you can find here: https://github.com/adshares/ansible-role-adservice#role-variables

   .. code-block:: yaml

       - hosts: my-server
          roles:
            - role: adshares.adservice
              vars:
                service_name: "{{ item }}"
                server_domain: example.com
                setup: true
                deploy: true
              loop:
                - adserver
                - adpanel
                - adselect
                - aduser
                - adpay
                - adcontroller

#. Go to the AdPanel (``https://panel.example.com``), create an administrator account and complete the setup.

Technical info
^^^^^^^^^^^^^^

All modules are in ``/opt/adshares/`` handled by system user ``adshares``
(you can change it during installation; `see more <https://github.com/adshares/ansible-role-adservice#role-variables>`_).

There are six modules:

* `AdPanel <https://github.com/adshares/adpanel>`_ - frontend UI
* `AdController <https://github.com/adshares/adcontroller>`_ - control panel to manage and monitor all modules
* `AdSelect <https://github.com/adshares/adselect>`_ - module that handles ad selection for publishers (db: elasticsearch)
* `AdPay <https://github.com/adshares/adpay>`_ - module that calculate payments for each ad impression (db: mysql)
* `AdUser <https://github.com/adshares/aduser>`_ - module that provides context info about request (db: mysql)
* `AdServer <https://github.com/adshares/adserver>`_ - module that manages all processes and communicates with other modules, ADS blockchain and other adservers (db:mysql)

Updates
-------

To update AdServer modules use Ansible with the same adservice role, just set ``deploy: true``. You can also limit list of modules to perform partial update.

.. code-block:: yaml

   - hosts: my-server
     roles:
       - role: adshares.adservice
         vars:
           service_name: "{{ item }}"
           deploy: true
         loop:
           - adserver
           - adpanel
           - adselect
           - aduser
           - adpay
           - adcontroller
