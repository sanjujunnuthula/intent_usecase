from managers import text_pattern_manager,nlp_manager
from flask import Flask, request, jsonify
from modules.serviceOrder.service_controller import generate_tmf_json

def intent_extractor(args,files,json):
    try:
        raw_text = json['text-intent']
        result = nlp_manager.TextExtractor(files,raw_text).extract_entities()
        tmf_pre_data = generate_tmf_json(result)
        print("resp from tmf", tmf_pre_data)
        return result
    except Exception as err:
        print("in exception",str(err))
        return str(err)




