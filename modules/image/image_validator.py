import re
from werkzeug.datastructures import FileStorage

from common import common_constants
from modules.image import image_constants


def validate_image_file_from_request(image_file):
    if not image_file or not isinstance(image_file, FileStorage):
        return "Invalid image file."

    if image_file.mimetype not in image_constants.IMAGE_MIMETYPES:
        return "Invalid image mimetype. Only JPEG/JPG/PNG type is supported."

    return False


def validate_image_url_from_request(image_url):
    if image_url and not re.search(image_constants.IMAGE_URL_REGEX, image_url):
        return "Invalid image URL."

    return False


def validate_arguments_from_request(send_predictions):
    if send_predictions is None:
        send_predictions = image_constants.SEND_PREDICTIONS_BOTH

    if not (send_predictions == image_constants.SEND_PREDICTIONS_JSON or
            send_predictions == image_constants.SEND_PREDICTIONS_IMAGE or
            send_predictions == image_constants.SEND_PREDICTIONS_BOTH):
        return F"Invalid value for '{image_constants.RESPONSE_KEY}'", None, None, None, None


    return None, send_predictions
