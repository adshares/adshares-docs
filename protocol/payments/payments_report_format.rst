.. _protocol-payments-report-format:

Payment Report Format
=====================

Here is an example of a :ref:`Payment Report <protocol-definitions-paymentreport>`:

::

    [
        {
            "case_id": "8c4d43f6-d4ee-4ca8-9cb4-907ac0a2e520",
            "event_id": "e6593827-30d0-4934-ba24-361e0c5dce49",
            "event_type": "view",
            "banner_id": "b22e19a3874847f4a6287d26deacd208",
            "zone_id": "a22e19a3874847f4a6287d26deacd208",
            "publisher_id": "fa9611d2d2f74e3f89c0e18b7c401891",
            "event_value": 10
        },
        {
            "case_id": "4fb6bf3f-0849-4eb4-9777-43a96f5c21d6",
            "event_id": "636c6355-df2c-4219-94b4-10eb4266e2b9",
            "event_type": "click",
            "banner_id": "9c6edfaef7454af4a96cb434c85323ee",
            "zone_id": "2c6edfaef7454af4a96cb434c85323ee",
            "publisher_id": "d5f5deefd010449ab0ee0e5e6b884090",
            "event_value": 100
        }
    ]
