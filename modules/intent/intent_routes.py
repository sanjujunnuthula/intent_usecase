from flask import Blueprint, request
from managers import file_manager,text_pattern_manager,nlp_manager

intent = Blueprint('intent', __name__)


@intent.route("/nlp/intent", methods=['POST'])
def intent_on_text():
    return nlp_manager.intent_on_image(request.args, request.files, request.form)
