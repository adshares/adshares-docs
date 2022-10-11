
.. _ads_client_installation:

Installation
==========================

The software is developed for Linux platform.
There is no intent to support other platforms.
The software was tested on Debian and Ubuntu.

Although compilation from source is available, we suggest to use binaries from Adshares PPA.

::

    sudo add-apt-repository ppa:adshares/releases -y
    sudo apt update
    sudo apt install ads ads-tools -y

Compilation
--------------------------

To compile the software you need boost and ssl libraries. Check the Makefile if anything else is missing.

::

    sudo apt update
    sudo apt install openssl libboost-all-dev libssl-dev cmake -y

Start with cloning the git directory.

::

    git clone https://github.com/adshares/ads.git

Before compiling ADS you could check if the ed25519 cryptography software is working correctly and what compile option gives you better speed for your CPU.

::

    cd ads/external/ed25519
    make -f Makefile.sse2
    ./mytest
    make clean
    make
    ./mytest

In our case compiling for sse2 reduces the speed of batch signature verifications by over 30% (it is not the case on AWS).
The results of the 2 runs are shown below.
The line stating with "BATC" reports number of signature verifications per second.
Compiling against the regular Makefile (``make``) generates a code that can perform over 30k signature verifications per second.

::

    START
    HASH: 1295553.388/s [79.074MiB/s]
    PKEY: 29027.926/s
    SIGN: 28596.429/s [1.745MiB/s]
    OPEN: 8721.537/s [0.532MiB/s]
    BATC: 18608.159/s [1.136MiB/s]

    START
    HASH: 836288.155/s [51.043MiB/s]
    PKEY: 48491.258/s
    SIGN: 47754.419/s [2.915MiB/s]
    OPEN: 14017.216/s [0.856MiB/s]
    BATC: 30312.243/s [1.850MiB/s]

Keep the compiled object files in the directory and compile ADS.

::

    cd ../..
    mkdir build
    cd build
    cmake -DCMAKE_PROJECT_CONFIG=ads ../src/
    make -j `nproc` ads adsd install

The default build is for production.
If you want to compile DEBUG version, add ``-DCMAKE_BUILD_TYPE=DEBUG`` option to ``cmake`` command.

::

    cmake -DCMAKE_BUILD_TYPE=DEBUG -DCMAKE_PROJECT_CONFIG=ads ../src/

When compiling, the compiler will detect if you have a recent kernel that supports the "FALLOC_FL_COLLAPSE_RANGE" option for fallocate().
This option is used to remove old (first) pages from log files and works only on ext4 file systems.
If You don't have a recent kernel or run the software on a different file system, then user log files will not be purged (will grow forever).
We will consider adding support for this case in the future.

Check if ``ads`` and ``adsd`` are installed properly.

::

    ads -v
    adsd -v

Both commands should return version.
