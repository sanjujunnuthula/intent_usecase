def get_message(message):
    response = {'message': message}
    return response


def exception(exception):
    return get_message('Something went wrong. Please contact server administrator.'), 500


def response_validation_error(error):
    return get_message(error), 400


def response_server_error(error):
    return get_message(error), 500


def from_flask_response(response):
    if response:
        return response.json(), response.status_code
    return response.content, response.status_code
