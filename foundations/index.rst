Foundations
===========

A three-layer ecosystem for web3 transition:

.. digraph:: foo
    :name: adshares.ecosystem
    :align: center

    graph [fontname="Segoe UI,Arial,sans-serif", fontsize="12"];
    node [fontname="Segoe UI,Arial,sans-serif", fontsize="12", target="_top"];
    edge [fontname="Segoe UI,Arial,sans-serif", fontsize="9", style="dashed", arrowhead="empty"];

    adserver [
        label="Ad servers and Apps",
        href="../foundations#ad-servers-and-apps"
        shape="box3d",
        color="",
    ];
    protocol [
        label="Adshares Protocol",
        href="../foundations#adshares-protocol"
        shape="box3d",
        fillcolor="#FF414D",
        fontcolor="#FFFFFF",
        style="filled",
    ];
    blockchain [
        label="Adshares Blockchain",
        href="../foundations#adshares-blockchain"
        shape="box3d",
        fillcolor="#1AA8BF",
        fontcolor="#FFFFFF",
        style="filled",
    ];

    adserver -> protocol;
    protocol -> blockchain;

1. Adshares Blockchain
----------------------

Capable of handling all ads settlements in ADS coin between Publishers and Advertisers in the digital world. Ultra light and fast.

The Adshares dPoS blockchain layer is used to transfer value between advertisers and publishers. It enables direct
one-to-one and one-to-many transfers. With 1,4 million transfers per second, Adshares is capable of holding the entire
advertising industry’s settlements.

There's plenty of benefits that comes from holding ADS coin. Take part in a true web3 advertising economy.

:ref:`Read more. <ads-blockchain>`

2. Adshares Protocol
--------------------

Enables the ad tech industry to adopt blockchain with minimum effort. The backbone of a new web3 advertising world.

The open-source protocol layer is used to transfer information about ad events across all networks: demand, requests,
supply, and bidding.

Adshares protocol delivers advertising in any format, into any placement (Metaverse, DOOH, DPOS, display, native,
social). It revolutionizes campaign planning, as it allows serving multiple formats from one place.

:ref:`Read more. <adshares-protocol>`

3. Ad servers and Apps
----------------------

Built on Adshares. Allow interaction between Publishers and Advertisers. Creating a new web3 advertising economy.

AdServer is the open-source solution built on and working as the interface with the Adshares ecosystem.

Tens of thousands of decentralized ad networks can exchange traffic, share opportunities with mutual benefits.
Any AdTech with  own DSP/SSP solution can integrate and gain the same benefits.

:ref:`Read more. <adserver>`
