from flask import Blueprint, request

from messenger.verify.service import verify_service

messenger_controller = Blueprint('messenger', __name__)

@messenger_controller.get('/')
def verify_controller():
    query = request.args
    return verify_service(query)
