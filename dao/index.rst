
.. _dao:

Adshares DAO
============

Adshares DAO is a decentralized autonomous organization (DAO) run by holders of the Adshares coin. Its governance framework has been created by the Adshares founding team. This document provides an overview of the first iteration of the main decision-making mechanisms of the DAO, its roadmap, and plans for the future.


Introduction
------------

In the early stage of the web1 world, the data from installed software was stored on the user's local hard drives and it belonged to them. We paid for the software and the data stayed (usually) with us if our PC was not targeted by hackers. We did not have much to say on the Internet, but we were not being monetized, and we knew what we were paying for.

| Web2 world created new opportunities for people to express their opinions. They were finally able to have something to say in the digital world.
| However, it came at a price. In the web2 world, people still do not have any ownership over their data, nor do they have the influence to decide how it is being used and monetized. The biggest tech companies acquired ownership of user behavior data, personal information, and content created by the community. Web2 world exists and is widely used, but people who are using it are not able to shape it according to their needs. This world is governed by the boards and stakeholders of various companies, not the people who are using the product.

The emergence of the web3 world signals the possibility of a paradigm shift. Privacy, transparency, immutability, decentralization, and data ownership have become real possibilities. Every organization or company understands the value of community engagement and the magnitude of its influence.

With more and more industries adopting blockchain technology, AdTech is a perfect place for web3 innovation. We can have more flawless, personal internet experiences if we own and control our data and can have a say in terms of the development of products that we use.


AdTech can be enhanced by web3 tools
````````````````````````````````````

| The Internet Advertising Market is expected to reach $1.08 Trillion by the end of 2027 [#]_.
| Despite the size of this market, the AdTech sector – whose sole purpose is to exist for publishers, advertisers, and brands – has been lacking any significant innovation over the past decade.
| The digital advertising industry is currently in a hand of a few big players. Publishers lose up to 70% of their revenue due to ecosystem inefficiencies and middlemen. Frauds are making companies lose billions of dollars every year.
| And the only way to "fix" those issues – is to add more services, plugins, and middlemen.
| The actual consumers have nothing to say about how their user data is being used and sold, and like in other industries, they are just a product which is being monetized by the giants. In the current advertising world, consumers' data only increases the revenue of a given platform, not its users.

The most precious resource on the web3 world is the people and communities. In web3 reality, people can finally express their opinion about their digital world. It gets even better - they can shape it together. This new paradigm is being created as we speak, and people are slowly refusing to be just a product.


Think globally, act locally
```````````````````````````

Since Adshares' goal is to become an infrastructure for the whole AdTech sector it should also set trends within the industry. Especially, if it aims to become a Metaverse advertising standard. Moving the digital advertising ecosystem into web3 will not be an easy thing to do and it will require a collaborative mindset. With more and more companies joining the ecosystem there will be a need for a decentralized organization that should govern the blockchain and the protocol.

| This is the reason why Adshares has decided to take a further step in shaping the future of AdTech by setting up **Adshares DAO**.
| Our goal is to create the proper kind of community - one that promotes intercultural understanding, creates trust between members who are strangers, guarantees full transparency, and ensures that every member adheres to the standards of the community.

Adshares initial core team remains as it was. It stands as part of the community by supporting the Adshares protocol and the whole ecosystem. It's doing so by putting resources into organizations and projects that will contribute to Adshares' long-term development. The creation of DAO will help to achieve this goal.


Overview
--------

Decentralized autonomous organizations, or DAOs, are automatic and democratic online communities that function through participation and voting by individuals coming from a given community. DAOs adopt a fundamentally transparent and democratic approach to decision-making. Since every DAO decision is collaborative, publicly debated, voted on, and recorded, trust in DAO-run government is increasing over time.

| Adshares DAO is an initiative that grants voting rights to ADS holders. Its purpose is to govern the product and the direction of its development with the use of ADS Coin or its wrapped token version in the later stage.
| Through the public governance module, the DAO coin/token holders will govern the core products, a special DAO treasury, and key decisions around the ecosystem.
| Members of Adshares DAO will be able to work and connect in novel ways that are not feasible with centralized organizations. A more connected, engaged, and invested community brings extra value to the project.
| The Adshares core development team will create the public governance module in-house. In the first iteration, AdsharesDAO will be partially centralized when it comes to decision execution, as it will assure the effectiveness of resources and activities. As the Adshares ecosystem expands and gains more users and DAO grows, it will become increasingly decentralized.


Adshares Improvement Proposal (AIP)
-----------------------------------

The proposal procedure is described in general in this governance guide. It is a dynamic document that will change and evolve with the help of the DAO community.

Fundamentally, Adshares DAO is governed by its members. Anyone who holds enough ADS can create a proposal. As a result, significant changes to Adshares DAO should be approved by the entire community through a process called **"Adshares Improvement Proposal"** (AIP).

**AIP steps:**

#. **Ideas and Discussion.** AIP ideas typically start on the Adshares Discord, Telegram, live meetings, or somewhere else in the community.
#. **Proposal form.** If a DAO member wants to submit an AIP, he needs to use an AIP template and submit it to the Adshares DAO forum in the right one section. AIP Idea is submitted as a new proposal post.
#. **Forum Feedback.** `Forum <https://forum.adshares.net/>`_ is a place for initial discussion on the dedicated AIP proposal page on the forum in the `[ideas] <https://adshar.es/ideas>`_ category. The original post cannot be changed by the author; any modifications or improvements to the original idea must be made in the comments. The Discussion topic is closed by a moderator when the author and community agree that it's ok to create AIP. This will filter out bad ideas and encourage thoughtful proposals.
#. **AIP creation.** After initial community feedback author fills out the template again. He should include any forum suggestions that will help the proposal better serve the DAO community. If further information is required to fully express the purposes, details, and ramifications of the AIP Draft, it can be added by the author to the template.
#. **Voting** occurs on the Adshares DAO platform, and it takes 7 days. Only moderators can submit the AIP to ensure that each proposal is following the proposal form template. One ADS Coin is equal to one vote. To ensure the fairness of the voting, the system calculates your voting power based on the latest snapshot of your ADS wallet balance which happened prior to the API creation. Snapshots are taken at the time of latest distribution of staking rewards (every 2048 blocks which usually  takes about 12 days).
#. **Implementation.** Proposals that receive a majority "In favor" vote are moved into implementation. In quorum will not be reached proposal is rejected and the author can resubmit the proposal about the given subject after 14 day cooldown period which can be used for discussions and enhancement of the original proposal.

.. uml::
    :align: center

    skinparam monochrome true

    <style>
        activityDiagram {
            BackgroundColor #000
            FontColor #FFF
            diamond {
                BackgroundColor #FFF
                FontColor #000
            }
            arrow {
                FontColor #000
            }
            swimline {
                BackgroundColor #FFF
                FontColor #000
            }
        }
        document {
           BackgroundColor transparent
        }
    </style>

    |Discourse (forum)|
    :Create AIP proposal
    on forum;
    repeat
        repeat :AIP discussion;
            backward :Adjust proposal;
        repeat while (30 positive votes
                    on forum?) is (no)
        ->yes;
    |Voting platform|
        :Create AIP on
        voting platform;
        :Voting takes
        place for 7 days;
        backward :Create new version
        of AIP proposal;
    repeat while (Majority and
                quorum reached?) is (no)
    ->yes;
    :AIP has passed;


AIP Template
------------

Typically, a proposal will include:

- **Title**
- **Intro**: High-level overview. A summary of the proposal in two or three sentences.
- **Motivation**: an explanation for the proposal's implementation, and why is it worth implementing given the AIP.
- **Specification**: Low-level overview. A thorough overview of the tools and needs that will be used in AIP implementation.
- **Steps/Milestones**: The actions needed to put the idea into practice, together with any necessary expenses, manpower, as well as other resources.
- **Timeline**: Essential timeline information, such as the start date, milestone dates, and finish date.
- **Cost**: The entire cost to carry out the proposal.
- **Risks**: What are the risks regarding proposal implementation.

Any template may have extra fields added, if necessary, by the author to adequately express the purposes, details, and concerns of the AIP Draft. Please keep in mind that numerous people can collaborate on an AIP concept, but it should only be submitted once.

Proposals that were not approved the first time around and are being resubmitted should additionally include:

- Original proposal URL
- The reason it was denied
- Changes made and reasons why it should now be approved


Voting Requirements
-------------------

There are two possible votes: **"In Favor"** and **"Against"**. Voting "In favor" indicates support for enacting the AIP in its current form. Voting "Against" signifies opposing the AIP's implementation in its current form; you may vote "Against" to urge the author to revise the AIP before resubmitting it.

- A proposal creator can only have one active proposal at a time but can vote on other proposals.
- To create a proposal, you will need to hold at least 100 ADS.
- There is no fee for proposal creation, you just need to hold the appropriate ADS balance.
- The minimum quorum is 10% of the total ADS supply.
- Exchanges wallets and LP contracts will be excluded from quorum. List of those wallets will be publicly available.
- Proposal requires a simple majority (50% + 1) to pass.


DAO Activation
``````````````

The DAO will be officially launched with its first voting about DAO creation. In order to proposal to pass it is required for quorum to reach 50% + 1 to pass


Future of Adshares DAO
----------------------

Adshares DAO 2.0 and Adshares DAO AI
````````````````````````````````````

Imagine all AdTech layers, the whole advertising world governed by code and controlled by AI. All those things are built by the community consensus, where the community also benefits from this system. Like the Adshares ecosystem, Adshares DAO will constantly evolve. After the successful implementation of the first DAO iteration, the community and all the teams who participate in Adshares ecosystem development will also focus on the future of Adshares DAO to make it more robust and decentralized over time. The ideal Adshares Ecosystem should be developed by a hundred of independent developers, AdTech companies and Metaverse creators which are working together on building the whole AdTech world with the use of web3 tools. Like Ethereum is the biggest Ecosystem for DeFi, we want Adshares to be the biggest ecosystem for AdTech. The more ad servers and ad networks are built on Adshares protocol the more irresistible and decentralized will be the future of advertising system.

Adshares DAO Council
````````````````````

With more companies joining the Adshares ecosystem our goal is to build a totally decentralized AdTech infrastructure governed by DAO. To achieve this, on the next stage of DAO development we plan to establish a council of finite number of members. Those members will come from the core team, community, and the most involved companies from the ecosystem.

| Original Council members will be proposed and chosen via the AIP. DAO itself will decide about exact role of Council Members however their major tasks will be to manage funding submissions for DAO Grant initiative and govern the entire process of AIP.
| The Council's debates and votes will take place on the Adshares Discord channel.

Adshares DAO will gradually integrate the proposal and vote procedures into a comprehensive, on-chain platform in the form selected by the community.

.. [#] Allied Market Research

.. toctree::
    :hidden:

    Discourse (forum) <https://forum.adshares.net/>