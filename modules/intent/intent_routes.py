from flask import Blueprint, request
from modules.intent import intent_controller

intent = Blueprint('intent', __name__)


@intent.route("/nlp/text-intent", methods=['POST'])
def intent_on_text():
    return intent_controller.intent_extractor(request.args, request.files, request.json)
