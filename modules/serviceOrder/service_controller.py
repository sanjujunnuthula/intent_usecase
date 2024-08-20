from flask import jsonify, request
from typing import List, Dict
from models.service_order import ServiceCharacteristic, ServiceSpecification, Service, ServiceOrderItem, ServiceOrder
import json
from utils import app_utils 
from common import common_constants
import requests



def generate_tmf_json(data):
    try:
        if isinstance(data, list) and len(data) > 0:
            item = data[0]  # Get the first dictionary from the list

            # Extract the values, using an empty string if a key is missing
            region = item.get('region','')
            vendor = item.get('vendor', '')
            version = item.get('version', '')
            workload = item.get('workload', '')

            # Return the extracted values as a JSON response
            data = ({
                'vendor': vendor,
                'version': version,
                'workload': workload,
                'region': region
            })

            return create_service_order(data)
        else:
            data= ({
                'vendor': '',
                'version': '',
                'workload': '',
                'region':''
            })

            return create_service_order(data)

    except Exception as err:
        print("in generare_tmf",str(err))


def create_servie_request(data):
   try:
       raw_request = {
           "variables": {
               "tmaf641payload": {
                   "value": json.dumps(data, indent=4),
                   "type": "string"
               }
           },
           "businessKey": "loanApproval"
       }

       print("while request to camunda", raw_request)
       response = requests.post(url=common_constants.CAMUNDA_SERVICE_BASE_URL,
                                json=raw_request)
       print("response from camunda",response)
       return response
   except Exception as err:
       print("while creating request",str(err))



def create_service_order(request):
 try:
     service_order = {
         "externalId": "tx167",
         "priority": "1",
         "description": "Intest orchestration request",
         "category": "TMF resource illustration",
         "requestedStartDate": app_utils.generate_current_datetime(),
         "requestedCompletionDate": app_utils.generate_current_datetime(),
         "@type": "ServiceOrder",
         "serviceOrderItem": [
             {
                 "id": "1",
                 "action": "add",
                 "@type": "ServiceOrderItem",
                 "service": {
                     "serviceState": "active",
                     "type": "CFS",
                     "serviceCharacteristic": [
                         {
                             "name": request['workload'],
                             "valueType": "object",
                             "value": {
                                 "@type": "JSONSpecification",
                                 "@schemaLocation": "https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/tree/scheema",
                                 "region": request['region'],
                                 "vendor": request['vendor'],
                                 "latency": "5",
                                 "throughput": "1234"
                             }
                         }
                     ],
                     "serviceSpecification": {
                         "id": "5GC_"+(app_utils.generate_unique_id()),
                         "href": "https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/tree/scheema",
                         "name": request['workload'],
                         "version": request['version'],
                         "@type": request['workload']
                     }
                 }
             }
         ]
     }

     # Convert the dictionary to a JSON string
     # service_order_json = json.dumps(service_order, indent=4)
     # print(service_order_json)

     print('service request',create_servie_request(service_order))
     return service_order

 except Exception as err:
  print("in exception",str(err))


