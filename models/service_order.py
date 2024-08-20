from flask import jsonify, request
from typing import List, Dict

class ServiceCharacteristic:
    def __init__(self, name="5GRAN-DU", valueType="object", value=None):
        if value is None:
            value = {
                "@type": "JSONSpecification",
                "@schemaLocation": "https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/tree/scheema",
                "region": "",
                "vendor": "OAI",
                "latency": "5",
                "throughput": "1234",
            }
        self.name = name
        self.valueType = valueType
        self.value = value

class ServiceSpecification:
    def __init__(self, id="5GC_1234", href="https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/tree/scheema", name="5GRAN-DU", version="", _type="5GRAN"):
        self.id = id
        self.href = href
        self.name = name
        self.version = version
        self._type = _type

class Service:
    def __init__(self, serviceState="active", _type="CFS", serviceCharacteristic=None, serviceSpecification=None):
        if serviceCharacteristic is None:
            serviceCharacteristic = [ServiceCharacteristic()]
        if serviceSpecification is None:
            serviceSpecification = ServiceSpecification()
        self.serviceState = serviceState
        self.type = _type
        self.serviceCharacteristic = serviceCharacteristic
        self.serviceSpecification = serviceSpecification

class ServiceOrderItem:
    def __init__(self, id="1", action="add", _type="ServiceOrderItem", service=None):
        if service is None:
            service = Service()
        self.id = id
        self.action = action
        self.type = _type
        self.service = service

class ServiceOrder:
    def __init__(self, externalId="", priority="1", description="Intest orchestration request", category="TMF resource illustration", requestedStartDate="2020-08-27T09:37:40.508Z", requestedCompletionDate="2020-08-27T09:37:40.508Z", _type="ServiceOrder", serviceOrderItem=None):
        if serviceOrderItem is None:
            serviceOrderItem = [ServiceOrderItem()]
        self.externalId = externalId
        self.priority = priority
        self.description = description
        self.category = category
        self.requestedStartDate = requestedStartDate
        self.requestedCompletionDate = requestedCompletionDate
        self.type = _type
        self.serviceOrderItem = serviceOrderItem

    def to_dict(self):
        return {
            "externalId": self.externalId,
            "priority": self.priority,
            "description": self.description,
            "category": self.category,
            "requestedStartDate": self.requestedStartDate,
            "requestedCompletionDate": self.requestedCompletionDate,
            "@type": self.type,
            "serviceOrderItem": [item.__dict__ for item in self.serviceOrderItem]
        }
