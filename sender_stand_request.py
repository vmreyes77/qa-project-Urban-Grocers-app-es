import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_user_token():
    new_user = post_new_user(data.user_body)
    return new_user.json()["authToken"]


def post_new_kit(name):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=name,
                        headers=data.headers)


def post_new_client_kit(kit_body, auth_token=None):
    if auth_token is None:
        raise ValueError("Se requiere un token de autenticación para crear un nuevo kit")

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
