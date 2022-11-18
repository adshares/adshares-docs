Campaigns
===========

Campaigns list
--------------------------

.. http:get:: /api/v2/campaigns

    Fetch campaigns.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error

    :>json integer data[].id: ID
    :>json string data[].uuid: UUID
    :>json string data[].createdAt: date of creation
    :>json string data[].updatedAt: date of last update
    :>json string data[].secret: conversion secret
    :>json integer data[].conversionClick: type of click conversion
    :>json string data[].conversionClickLink: click conversion callback URL
    :>json string data[].classifications[].classifier: classifier
    :>json string data[].classifications[].status: status
    :>json object data[].classifications[].keywords: classification result, conforms taxonomy
    :>json integer data[].basicInformation.status: status
    :>json string data[].basicInformation.name: name
    :>json string data[].basicInformation.targetUrl: landing URL
    :>json integer, null data[].basicInformation.maxCpc: maximal CPC
    :>json integer, null data[].basicInformation.maxCpm: maximal CPM
    :>json integer, null data[].basicInformation.budget: budget
    :>json string data[].basicInformation.medium: medium, e.g. "web"
    :>json string, null data[].basicInformation.vendor: vendor
    :>json string data[].basicInformation.dateStart: date of start
    :>json string, null data[].basicInformation.dateEnd: date of end, if `null` campaign will last forever
    :>json object data[].targeting.requires: required features, conforms taxonomy
    :>json object data[].targeting.excludes: forbidden features, conforms taxonomy
    :>json integer data[].ads[].id: banner ID
    :>json string data[].ads[].uuid: UUID
    :>json string data[].ads[].createdAt: date of banner creation
    :>json string data[].ads[].updatedAt: date of last banner update
    :>json string data[].ads[].creativeType: banner type
    :>json string data[].ads[].creativeMime: banner MIME type
    :>json string data[].ads[].creativeSha1: SHA-1 checksum of banner content
    :>json string data[].ads[].creativeSize: space occupied by banner
    :>json string data[].ads[].name: banner name
    :>json integer data[].ads[].status: banner status
    :>json string, null data[].ads[].cdnUrl: banner content URL on CDN, may be `null` if was not uploaded to CDN
    :>json string data[].ads[].url: banner content URL
    :>json string data[].bidStrategy.name: bid strategy name
    :>json string data[].bidStrategy.uuid: bid strategy UUID
    :>json string data[].conversions[].uuid: conversion UUID
    :>json string data[].conversions[].campaignId: campaign ID
    :>json string data[].conversions[].name: conversion name
    :>json string data[].conversions[].limitType: conversion limit type
    :>json string data[].conversions[].eventType: conversion event type
    :>json string data[].conversions[].type: conversion type
    :>json integer data[].conversions[].value: conversion value
    :>json boolean data[].conversions[].isValueMutable: conversion type
    :>json integer data[].conversions[].cost: conversion cost
    :>json integer data[].conversions[].occurrences: number of conversion occurrences
    :>json boolean data[].conversions[].isRepeatable: can conversion be repeated
    :>json boolean data[].conversions[].link: conversion link

.. http:get:: /api/v2/campaigns/{id}

    Fetch campaign by ID.

    :reqheader Content-Type: ``application/json``

    :statuscode 200: no error
    :statuscode 404: campaign does not exist
