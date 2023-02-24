import os

from PetStore.app.api import PetFriends
from PetStore.setting.config import v_email, v_password, incorrect_email, incorrect_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=v_email, password=v_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_incorrect_email(email=incorrect_email, password=v_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_api_key_for_incorrect_password(email=v_email, password=incorrect_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_all_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_post_new_pets_with_photo_positiv(name='Vasya', animal_type="cat", age='3', pet_photo='image/Vasiliy.jpg'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_new_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_post_new_pets_with_photo_incorrect_age(name='Vasya', animal_type="cat", age='- 3', pet_photo='image/Vasiliy.jpg'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_new_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    print('Возвращает некорректный статус 200 вместо 400, т.к. нельзя вводить отрицательный возраст')

def test_post_new_pets_with_photo_incorrect_age2(name='Vasya', animal_type="cat", age='54131874', pet_photo='image/Vasiliy.jpg'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_new_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    print('Возвращает некорректный статус 200 вместо 400, т.к. нельзя вводить слишком большой возраст')

def test_post_new_pets_with_photo_incorrect_name(name='', animal_type="cat", age='3', pet_photo='image/Vasiliy.jpg'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_new_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    print('Возвращает некорректный статус 200 вместо 400, т.к. нельзя вводить пустое поле name')

def test_post_new_pets_with_photo_incorrect_name2(name='ПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетрПетр', animal_type="cat", age='3', pet_photo='image/Vasiliy.jpg'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_new_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    print('Возвращает некорректный статус 200 вместо 400, т.к. нельзя вводить в поле name строку длинной более напр. 30 символов')

def test_delete_pets_valid_id():
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")

    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pets(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

def test_delete_pets_random_id():
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, pets = pf.get_list_of_pets(auth_key, filter="")

    pet_id = pets['pets'][0]['id']

    status, _ = pf.delete_pets(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()
    print('Возвращает некорректный статус 200 вместо 400. Нельзя удалять чужих животных')

def test_post_new_pets_without_photo_incorrect_age(name='Kotayson', animal_type="kot", age='-2'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print('Некорректный статус код в ответе 200 вместо 400, ожидание правок на беке')

def test_post_new_pets_without_photo_incorrect_age2(name='Kotayson', animal_type="kot", age='25485'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print('Некорректный статус код в ответе 200 вместо 400, ожидание правок на беке')

def test_post_new_pets_without_photo_incorrect_name(name='', animal_type="kot", age='2'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print('Некорректный статус код в ответе 200 вместо 400, поле name не может быть пустым')

def test_post_new_pets_without_photo_incorrect_name2(name='ТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсонТайсон', animal_type="kot", age='2'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print('Некорректный статус код в ответе 200 вместо 400, данные в поле name не может быть длинной более напр. 30 символов')

def test_post_new_pets_without_photo_pass(name='Vasya', animal_type='cat', age='3'):
    _, auth_key = pf.get_api_key(v_email, v_password)

    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_post_new_pets_without_photo_incorrect_age(name='Vasya', animal_type='cat', age='- 3'):
    _, auth_key = pf.get_api_key(v_email, v_password)

    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    print('Неокрректный статус 200 вместо 400. Ожидаем правки')

def test_post_new_pets_without_photo_incorrect_age2(name='Vasya', animal_type='cat', age='5468441'):
    _, auth_key = pf.get_api_key(v_email, v_password)

    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    print('Неокрректный статус 200 вместо 400. Ожидаем правки')

def test_post_new_pets_without_photo_incorrect_name(name='', animal_type='cat', age='3'):
    _, auth_key = pf.get_api_key(v_email, v_password)

    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    print('Неокрректный статус 200 вместо 400. Ожидаем правки')

def test_post_new_pets_without_photo_incorrect_name2(name='VasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasyaVasya', animal_type='cat', age='3'):
    _, auth_key = pf.get_api_key(v_email, v_password)

    status, result = pf.post_new_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    print('Неокрректный статус 200 вместо 400. Ожидаем правки')


def test_update_info_for_pet(name='Мурзилло', animal_type='Котик', age='16'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    pet_id = my_pets['pets'][0]['id']

    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_pet(auth_key,pet_id, name, animal_type, age)
        assert status == 200
        assert result['name'] == name

def test_update_info_for_pet_incorrect_age(name='Мурзилло', animal_type='Котик', age='8545241'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    pet_id = my_pets['pets'][0]['id']

    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_pet(auth_key,pet_id, name, animal_type, age)
        assert status == 200
        assert result['name'] == name
        print('Возвращает некорректный статус 200 вместо ожидаемого 400, т.к. возраст некорректный')

def test_post_set_photo_for_pets_positiv(pet_photo = 'image/Vasiliy.jpg'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, my_pets = pf.get_list_of_pets(auth_key, filter="my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, result = pf.post_set_photo_for_pets(auth_key, pet_id, pet_photo)
    assert status == 200
