from flask import Blueprint, request
from modules.serviceOrder import service_controller

service = Blueprint('service', __name__)


@service.route("/nlp/generate-service", methods=['get'])
def create_service():
    return service_controller.create_service_order(request)
