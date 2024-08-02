from common import common_constants
from modules.intent import image_constants


def parse_image_from_request(files, form):
    (error_file, image_file) = parse_image_file_from_request(files)
    (error_url, image_url) = parse_image_url_from_request(form)

    if error_file and error_url:
        return "Missing intent file or url", None, None
    else:
        if image_file:
            return None, image_file, None
        else:
            return None, None, image_url


def parse_image_file_from_request(files):
    if image_constants.IMAGE_FILE_KEY in files and files[image_constants.IMAGE_FILE_KEY]:
        return None, files[image_constants.IMAGE_FILE_KEY]
    else:
        return "Missing intent file", None


def parse_image_url_from_request(form):
    if image_constants.IMAGE_URL_KEY in form and form[image_constants.IMAGE_URL_KEY]:
        return None, form[image_constants.IMAGE_URL_KEY]
    else:
        return "Missing intent url", None


def parse_arguments_from_request(arguments):

    return arguments.get(image_constants.RESPONSE_KEY)

