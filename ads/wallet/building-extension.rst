
Building extension
==================

Download project

::

    git clone https://github.com/adshares/ads-browser-wallet.git
    cd ads-browser-wallet

Install Node.js and npm

::

    curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
    sudo apt-get install -y nodejs

Install dependencies

::

    npm install

Build distribution files

::

    npm run build

Files will be saved in ``ads-browser-wallet/build`` directory.

Plugin was built successfully using:

* Node.js v8.11.3
* npm v6.2.0

Packing extension using chrome
------------------------------

Open ``chrome://extensions/`` and click **Pack Extension** button.

Alternatively, use command line

::

    google-chrome --pack-extension=./build/

As a result **dist.crx** file should be generated.

If you have pem key, you should use it while packing next version of extension.
Command line call takes key as ``--pack-extension-key`` parameter.
