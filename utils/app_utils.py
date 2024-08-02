import glob
import os
import uuid
from PIL import Image


def is_path_exist(path):
    return glob.glob(path)


def generate_unique_identifier():
    return str(uuid.uuid4())


def get_image_dimensions(image_path):
    if is_path_exist(image_path):
        with Image.open(image_path) as img:
            return img.size
    else:
        return None, None


is_development_environment = 'FLASK_ENV' in os.environ \
                             and os.environ['FLASK_ENV'] == 'development'
