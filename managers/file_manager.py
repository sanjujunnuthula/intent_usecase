import traceback
import requests
import shutil
import os
import uuid
from modules.image import image_constants
from utils import app_utils


def check_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def download_and_save_image_url_from_request(image_url):
    try:
        print("downloading image url: ", image_url)
        response = requests.get(image_url, stream=True)
        if response.ok:
            content_type = response.headers['Content-Type']
            file_extension = content_type.split("/")[1]

            file_name = f"{app_utils.generate_unique_identifier()}.{file_extension}"
            file_location = f"{image_constants.TEMP_IMAGES_FOLDER_PATH}/{file_name}"

            with open(file_location, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        file.write(chunk)
            return None, file_location, file_name
        else:
            return "Image download failure", None, None
    except Exception as ex:
        print("Exception in download file", image_url, ex)
        return "Exception in download file", None, None


def save_image_file_from_request(image_file):
    check_directory(image_constants.TEMP_IMAGES_FOLDER_PATH)

    mimetype_strings = image_file.mimetype.split('/')
    file_extension = mimetype_strings[len(mimetype_strings) - 1]

    # data = uuid
    file_name = f'{str(uuid.uuid4())}.{file_extension}'
    # file_name = data
    file_location = f"{image_constants.TEMP_IMAGES_FOLDER_PATH}{file_name}"

    image_file.save(file_location)

    return file_location, file_name



def save_image_file_from_numpy_array_with_detection(numpy_array_with_detections):
    check_directory(image_constants.RESULT_IMAGES_FOLDER_PATH)

    file_extension = 'jpg'

    # data = uuid

    file_name = f'{str(uuid.uuid4())}.{file_extension}'
    # print("file_name90", file_name)
    # file_name = f'{str(data.uuid4())}.{file_extension}'
    file_location = f"{image_constants.RESULT_IMAGES_FOLDER_PATH}{file_name}"

    pyplot.imsave(file_location, numpy_array_with_detections)

    return file_location, file_name


def delete_local_file(file_path):
    try:
        os.remove(file_path)
        return None
    except Exception:
        print("Exception occurred while deleting file resource.", file_path, flush=True)
        traceback.print_exc()
        return "Exception occurred while deleting file resource."


def delete_local_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        return None
    except Exception:
        print("Exception occurred while deleting folder resource.", folder_path, flush=True)
        traceback.print_exc()
        return "Exception occurred while deleting folder resource."

