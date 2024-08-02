from flask import Blueprint, request
# from modules.image import image_controller
from managers import file_manager,text_pattern_manager,nlp_manager

image = Blueprint('image', __name__)


@image.route("/nlp/intent", methods=['POST'])
def intent_on_image():
    return nlp_manager.intent_on_image(request.args, request.files, request.form)
