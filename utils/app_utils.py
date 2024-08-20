import glob
import os
import uuid
from datetime import datetime, timezone
import random
import string

def generate_current_datetime():
    # Get the current datetime with timezone set to UTC
    current_datetime = datetime.now(timezone.utc)

    # Format the datetime to the required string format
    formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return formatted_datetime





def generate_unique_id(length=5):
    # Define the possible characters: uppercase letters and digits
    characters = string.ascii_uppercase + string.digits

    # Generate a random string of the specified length
    unique_id = ''.join(random.choices(characters, k=length))

    return unique_id



def is_path_exist(path):
    return glob.glob(path)


def generate_unique_identifier():
    return str(uuid.uuid4())



is_development_environment = 'FLASK_ENV' in os.environ \
                             and os.environ['FLASK_ENV'] == 'development'
