from flask import Blueprint, request

from messenger.service import verify

messenger_controller = Blueprint('messenger', __name__)

@messenger_controller.get('/')
def verify_controller():
    query = request.args
    return verify.verify_service(query)
