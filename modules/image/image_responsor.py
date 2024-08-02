from flask import send_file, jsonify

from modules.image import image_constants


def intent_on_image_success(intent, response):
    if response == image_constants.SEND_PREDICTIONS_JSON:
        return {
            "predictions": intent.predictions

        }

    if response == image_constants.SEND_PREDICTIONS_BOTH:
        return {
            "input_url": intent.input_url,
            "output_url": intent.output_url,
            "predictions": intent.predictions
        }


def send_file_from_directory(file_path):
    return send_file(file_path, as_attachment=False)
