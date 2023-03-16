import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_are_present(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную statistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pets элементы карточек питомцев
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Получаем количество карточек питомцев
   number_of_pets = len(pets)

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets


def test_all_pets_have_different_names(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   name_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Проверяем, что у всех питомцев разные имена:
   list_name_my_pets = []
   for i in range(len(name_my_pets)):
       list_name_my_pets.append(name_my_pets[i].text)
   set_pet_data = set(list_name_my_pets)  # преобразовываем список в множество
   assert len(list_name_my_pets) == len(set_pet_data)  # сравниваем длину списка и множества: без повторов должны совпасть


def test_no_duplicate_pets(go_to_my_pets):

   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную data_my_pets элементы с данными о питомцах
   data_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Проверяем, что в списке нет повторяющихся питомцев:
   list_data_my_pets = []
   for i in range(len(data_my_pets)):
      list_data = data_my_pets[i].text.split("\n")  # отделяем от данных питомца "х" удаления питомца
      list_data_my_pets.append(list_data[0])  # выбираем элемент с данными питомца и добавляем его в список
   set_data_my_pets = set(list_data_my_pets)  # преобразовываем список в множество
   assert len(list_data_my_pets) == len(
      set_data_my_pets)  # сравниваем длину списка и множества: без повторов должны совпасть


def test_photo_availability(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную statistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Находим половину от количества питомцев
   half = number // 2

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert number_а_photos >= half
   print(f'количество фото: {number_а_photos}')
   print(f'Половина от числа питомцев: {half}')


def test_show_my_pets():

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='button']")))
   # Нажимаем на кнопку меню (кнопка с 3 горизонтальными полосками)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

   # Проверяем что мы оказались на странице "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'


def test_show_pet_friends():

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
   # Тест упал, так как не все карточки питомца имеют фото (отсутствует атрибут 'src')


def test_there_is_a_name_age_and_gender(go_to_my_pets):

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Настраиваем переменную явного ожидания:
   wait = WebDriverWait(pytest.driver, 5)

   # Ожидаем, что данные всех питомцев, найденных локатором css_locator = '.table.table-hover tbody tr', видны на странице:
   for i in range(len(pet_data)):
      assert wait.until(EC.visibility_of(pet_data[i]))

   # Ищем в теле таблицы все имена питомцев и ожидаем увидеть их на странице:
   name_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))

   # Ищем в теле таблицы все породы питомцев и ожидаем увидеть их на странице:
   type_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))

   # Ищем в теле таблицы все данные возраста питомцев и ожидаем увидеть их на странице:
   age_my_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
   for i in range(len(age_my_pets)):
      assert wait.until(EC.visibility_of(age_my_pets[i]))



# python -m pytest -v --driver Chrome --drivpython -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_all.pyer-path /tests/chromedriver.exe tests/test_all.py