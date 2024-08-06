import os
import json
import re
from extr import RegEx, RegExLabel
from extr.entities import create_entity_extractor
from init import app
from models import evaluation_model
from managers.text_pattern_manager import Entity_pattern
import os
from retry import retry
from common import common_constants
import json

class TextExtractor:
    def __init__(self, input_file=None,input_text=''):
        self.input_file = input_file
        self.input_text = input_text

    def read_file(self):
        filename, file_extension = os.path.splitext(self.input_file)
        if file_extension == ".json":
            with open(self.input_file) as f:
                text = json.load(f)
                return text,file_extension
        elif file_extension == ".txt" :
            with open(self.input_file, 'r') as f:
                text = f.read()
                return text, file_extension
        else:
           text = input_file
           return text, null

    def extract_entities(self):
        final_dict = []
        try:
            final_entities = []
            entity_patterns = Entity_pattern().pattern()
            if self.input_text == '' :
              text, file_extension =self.read_file()
            else:
              file_extension = None
              text = self.input_text

            entity_extractor = create_entity_extractor(entity_patterns)
            if file_extension == ".json":
                for i in text:
                    # entities = entity_extractor.get_entities(text[i].lower())
                    print("text[i].......",text[i])
                    entities = entity_extractor.get_entities(text[i])
                    final_entities.append(entities)
            else:
                return modify_raw_text(text)
                for line in text.split("\n"):
                    if line.strip():
                        # entities = entity_extractor.get_entities(line.lower())
                        entities = entity_extractor.get_entities(line[i])
                        final_entities.append(entities)

            for entities in final_entities:
                entity_dict = {entity.label: entity.text.strip().strip('"') for entity in entities}
                final_dict.append(entity_dict)
            # print("final_dict1",final_dict)

            if len(final_dict[0])==0:
                final_dict = {'version': '', 'vendor': '', 'region': '', 'workload': ''}

            if len(final_dict)==1:
                # here we are return in dict format incase single line of text.
                return final_dict[0]
        except Exception as e:
            print(f"Error extracting entities: {e}")
            final_dict = {'version': '', 'vendor': '', 'region': '', 'workload': ''}
        return final_dict

# Example usage
# input_file_path = r"C:\Users\anuthati\OneDrive - Capgemini\Desktop\Nlp_Doc.txt"
# input_file_path = r"C:\Users\anuthati\OneDrive - Capgemini\Desktop\text_json.json"
#TextExtractor(input_file_path).extract_entities()


def modify_raw_text(raw_text):
    final_entities = []
    for i in raw_text.split("\n"):
        entity_extractor = create_entity_extractor( Entity_pattern().pattern())
        # final_entities.append(entity_extractor.get_entities(i.lower()))
        print("i---------.......", i)
        final_entities.append(entity_extractor.get_entities(i))
    final_entities
    print("final_entities222222222222222222",final_entities)
    final_dict = []  # creates an empty list
    for i in range(len(final_entities)):
        entities = final_entities[i]
        entity_dict = {entity.label: entity.text.strip().strip('"') for entity in entities}
        final_dict.append(entity_dict)

    return final_dict