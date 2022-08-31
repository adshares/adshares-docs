
Log rotation
=========================
ADS logs can grow in size fairly fast, so we recommend you set up logrotate.

Installation
-----------------------
You can check if logrotate is installed by asking:

::

    logrotate --version

If not, you can install it from a system package.
On Debian/Ubuntu:

::

    sudo apt-get install logrotate

Configuration
----------------------------
You need to create a configuration file.

::

    nano /etc/logrotate.d/ads

File contents:

::

    "/home/ads/.adsd/*.log" {
        daily
        weekly
        size 25M
        rotate 7
        missingok
        compress
        delaycompress
        copytruncate
    }

That's it.
After the filesize will be bigger than 25M you will see compressed log rotations.
