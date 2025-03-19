import random
import string


def get_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def get_account_data():
    return {'firstName': get_random_string(),
            'login': get_random_string(),
            'password': get_random_string()}


def is_expected_response(response, code, message):
    body = message
    if isinstance(message, str):
        body = {'code': code, 'message': message}
    return response.status_code == code and response.json() == body


def is_expected_code_and_type(response, code, key, _type):
    return response.status_code == code and isinstance(response.json().get(key), _type)
