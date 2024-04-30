import sender_stand_request
import data


def get_kit_body(name):
    current_kit = data.user_body.copy()
    current_kit["name"] = name
    return current_kit


def get_new_user_token():
    new_user = sender_stand_request.post_new_user(data.user_body)
    return new_user.json()["authToken"]


def positive_assert(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


# Prueba 1 "El número permitido de caracteres en name es 1.
def test_create_kit_1_characters_in_name_get_success_response():
    get_kit_body("a")
    positive_assert({"name": "a"})

# Prueba 2 "El número permitido de caracteres en name es 511.
def test_create_kit_511_characters_get_success_response():
    positive_assert({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})

# Prueba 3 "El número de caracteres es menor que la cantidad permitida en name (0).
def test_create_kit_0_characters_get_negative_response():
    negative_assert_code_400({"name": "0"})

# Prueba 4 "El número de caracteres es mayor que la cantidad permitida en name (512).
def test_create_kit_512_characters_get_negative_response():
    negative_assert_code_400({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})

# Prueba 5 "El campo name permite caracteres especiales (№%@).
def test_create_kit_especial_characters_get_positive_response():
    positive_assert({"name": "№%@"})

# Prueba 6 "El campo name permite espacios (A Aaa).
def test_create_kit_space_in_name_get_positive_response():
    positive_assert({"name": "A Aaa"})

#Prueba 7 "El campo name permite números enteros (123).
def test_create_kit_numbers_in_name_get_positive_response():
    positive_assert({"name": "123"})

# Prueba 8 "El campo name está vacío ( ).
def test_create_kit_no_parameters_in_name_negative_response():
    negative_assert_code_400({"name": ""})

# Prueba 9 "El campo name contiene parámetros deferentes (números (123)).
def test_create_kit_no_string_in_name_negative_response():
    negative_assert_code_400({"name": 123})