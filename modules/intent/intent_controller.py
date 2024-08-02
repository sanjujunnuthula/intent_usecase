from managers import text_pattern_manager,nlp_manager

def intent_extractor(args,files,json):
    try:
        raw_text = json['text-intent']
        result = nlp_manager.TextExtractor(files,raw_text).extract_entities()
        return result
    except Exception as err:
        print("in exception",str(err))
        return str(err)
