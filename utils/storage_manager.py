import requests
from common import common_constants

FILE = 'file'
FILE_NAME = 'file_name'


def upload_file(file_name, file_path, content_type):
    url = f"{common_constants.STORAGE_SERVICE_BASE_URL}upload"

    file = None
    with open(file_path, 'rb') as f:
        file = f.read()

    files = {FILE: (
        file_name, file, content_type)}

    response = requests.post(url, files=files)
    if response.ok:
        return response.json()[FILE_NAME]
    else:
        return None
