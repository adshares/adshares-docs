
Scaling
=======

.. uml::
    :align: center

    skinparam monochrome true
    skinparam linetype ortho

    database "MySql" as db {
      frame "AdServer" as adserverdb {
      }
    }

    cloud {
      [ADS Blockchain] as ads
    }

    actor "Swash AdAdmin" as admin
    component AdPanel as adpanel

    node "Primary AdServer" as primary {
        component "AdServer" as adserver
        adserver <--> adserverdb
        adserver <--> ads
    }

    node "Supply AdServer 2" as secondary2 {
        database "Elasticsearch 2" as adselect2db {
        }
        database "MySql 2" as aduser2db {
        }
        component "AdServer 2" as adserver2
        component "AdUser 2" as aduser2
        component "AdSelect 2" as adselect2
        aduser2 <--> aduser2db
        adserver2 <--> aduser2
        adserver2 <--> adselect2
        adserver2 <--> adserverdb
        adselect2 <--> adselect2db
    }

    node "Supply AdServer 1" as secondary1 {
        database "Elasticsearch 1" as adselect1db {
        }
        database "MySql 1" as aduser1db {
        }
        component "AdServer 1" as adserver1
        component "AdUser 1" as aduser1
        component "AdSelect 1" as adselect1
        aduser1 <--> aduser1db
        adserver1 <--> aduser1
        adserver1 <--> adselect1
        adserver1 <--> adserverdb
        adselect1 <--> adselect1db
    }

    admin --> adpanel
    adpanel <--> adserver

    frame "Load balancer" as balancer

    balancer ..> secondary1
    balancer ..> secondary2

    actor "Swash Extension 1" as swash1
    actor "Swash Extension 2" as swash2
    actor "Swash Extension 3" as swash3

    swash3 ..> balancer
    swash2 ..> balancer
    swash1 ..> balancer

.. uml::
    :align: center

    skinparam monochrome true
    skinparam linetype ortho

    database "MySql" as db {
      frame "AdServer" as adserverdb {
      }
      frame "AdUser" as aduserdb {
      }
    }

    cloud {
      [ADS Blockchain] as ads
    }

    actor "Swash AdAdmin" as admin
    component AdPanel as adpanel

    node "Primary AdServer" as primary {
        database "AdPay MySql" as adpaydb
        component "AdServer" as adserver
        component "AdUser" as aduser
        component "AdPay" as adpay
        adserver <--> adpay
        adpay <--> adpaydb
        adserver <-- aduser
        aduser <-- aduserdb
        adserver <--> adserverdb
        adserver <--> ads
    }

    node "Secondary AdServer 2" as secondary2 {
        database "Elasticsearch 1" as adselect2db {
        }
        component "AdServer 2" as adserver2
        component "AdUser 2" as aduser2
        component "AdSelect 2" as adselect2
        aduser2 <--> aduserdb
        adserver2 <--> aduser2
        adserver2 <--> adselect2
        adserver2 <--> adserverdb
        adselect2 <--> adselect2db
    }

    node "Secondary AdServer 1" as secondary1 {
        database "Elasticsearch 1" as adselect1db {
        }
        component "AdServer 1" as adserver1
        component "AdUser 1" as aduser1
        component "AdSelect 1" as adselect1
        aduser1 <--> aduserdb
        adserver1 <--> aduser1
        adserver1 <--> adselect1
        adserver1 <--> adserverdb
        adselect1 <--> adselect1db
    }

    admin --> adpanel
    adpanel <--> adserver

    frame "Load balancer" as balancer

    balancer ..> secondary1
    balancer ..> secondary2

    actor "Swash Extension 1" as swash1
    actor "Swash Extension 2" as swash2
    actor "Swash Extension 3" as swash3

    swash3 ..> balancer
    swash2 ..> balancer
    swash1 ..> balancer

.. uml::
    :align: center

    skinparam monochrome true
    skinparam linetype ortho

    database "MySql" as db {
      frame "AdServer" as adserverdb {
      }
      frame "AdUser" as aduserdb {
      }
    }

    cloud {
      [ADS Blockchain] as ads
    }

    actor "Swash AdAdmin" as admin
    component AdPanel as adpanel

    node "Primary AdServer" as primary {
        database "AdPay MySql" as adpaydb
        component "AdServer" as adserver
        component "AdUser" as aduser
        component "AdPay" as adpay
        component "AdSelect" as adselect
        adserver <--> adpay
        adserver --> adselect
        adpay <--> adpaydb
        adserver <-- aduser
        aduser <-- aduserdb
        adserver <--> adserverdb
        adselect --> adselectdb
        adserver <--> ads
    }

    node "Secondary AdServer 2" as secondary2 {
        component "AdServer 2" as adserver2
        component "AdUser 2" as aduser2
        component "AdSelect 2" as adselect2
        aduser2 <--> aduserdb
        adserver2 <--> aduser2
        adserver2 <-- adselect2
        adserver2 <--> adserverdb
        adselect2 <-- adselectdb
    }

    node "Secondary AdServer 1" as secondary1 {
        component "AdServer 1" as adserver1
        component "AdUser 1" as aduser1
        component "AdSelect 1" as adselect1
        aduser1 <--> aduserdb
        adserver1 <--> aduser1
        adserver1 <-- adselect1
        adserver1 <--> adserverdb
        adselect1 <-- adselectdb
    }

    admin --> adpanel
    adpanel <--> adserver

    frame "Load balancer" as balancer

    balancer ..> secondary1
    balancer ..> secondary2

    actor "Swash Extension 1" as swash1
    actor "Swash Extension 2" as swash2
    actor "Swash Extension 3" as swash3

    swash3 ..> balancer
    swash2 ..> balancer
    swash1 ..> balancer