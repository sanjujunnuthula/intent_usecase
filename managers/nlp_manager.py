import os
import json
import re
from extr import RegEx, RegExLabel
from extr.entities import create_entity_extractor
from init import app
from modules.image import image_constants
from utils import app_utils, storage_manager
from models import evaluation_model
from managers.text_pattern_manager import Entity_pattern
import os
from retry import retry
from common import common_constants
import json

class TextExtractor:
    def __init__(self, input_file=None):
        self.input_file = input_file

    def read_file(self):
        filename, file_extension = os.path.splitext(self.input_file)
        if file_extension == ".json":
            with open(self.input_file) as f:
                text = json.load(f)
                return text,file_extension
        else:
            with open(self.input_file, 'r') as f:
                text = f.read()
                return text, file_extension

    def extract_entities(self):
        final_dict = []
        try:
            final_entities = []
            entity_patterns = Entity_pattern().pattern()
            text, file_extension =self.read_file()

            entity_extractor = create_entity_extractor(entity_patterns)
            if file_extension == ".json":
                for i in text:
                    entities = entity_extractor.get_entities(text[i].lower())
                    final_entities.append(entities)
            else:
                for line in text.split("\n"):
                    if line.strip():
                        entities = entity_extractor.get_entities(line.lower())
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
result = TextExtractor(input_file_path).extract_entities()
print(result)