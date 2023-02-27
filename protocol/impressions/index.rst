.. _protocol-impressions:

Impressions
===========

.. uml::
    :align: center

    skinparam monochrome true

    participant "Supply Ctxt"      as SCP
    participant "Supply Agent"     as SSA
    participant "Supply Platf"     as SSP
    participant "Demand Platf"     as DSP
    participant "Demand Agent"     as DSA
    participant "Demand Ctxt"      as DCP    

    ==Initialization==

    SSA -> SSP : Register Evt
    SSP -> SCP : Register Evt //redirected//
    SCP --> SSA: Ctxt Scripts
    SSA -> SCP: Ctxt result //opt//

    ==Displaying ads==

    SSA -> SSP : Find Creatives
    SSP -> SCP : Get Ctxt
    SCP --> SSP : User/Site/Device Ctxt
    SSP --> SSA : Creatives

    loop for each Creative
        SSA -> DSP : Get Creative Cnt
        DSP --> SSA : Creative Cnt
        SSA -> SSP : View Evt
        SSP -> DSP: View Evt //redirected//
        DSP --> SSA: Register URL
        SSA -> DCP : Register Evt
        DCP --> SSA: Ctxt Scripts
        SSA -> DCP: Ctxt result //opt//
    end
    
    ==Clicking==

    SSA -> SSP : Click Evt
    SSP -> DSP : Click Evt //redirected//
    DSP -> DSA : Click Evt //redirected//
    DSA --> DSP: Cnv Evt //opt//


Contents
--------
.. toctree::
    :maxdepth: 1

    user_navigates
    user_browses
    user_clicks
