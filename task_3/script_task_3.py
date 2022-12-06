from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

load_dotenv()
login_yandex = os.getenv('login_yandex')
password_yandex = os.getenv('password_yandex')
path_driver = r'D:\Python\Homewrok\Advanced_Python\Lesson 6\task_3\chromedriver.exe'

# Создание подключения
def creating_driver(path=path_driver):
    # Передаем путь к драйверу Chrome через Servie, т.к. ч/з executable_path выдает ошибку
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    url = 'https://passport.yandex.ru/auth/'
    driver.get(url=url)
    return driver

# Поиск элемента на странице по ID
def check_exists_by_id(driver, id):
    try:
        driver.find_element(By.ID, id)
    except NoSuchElementException:
        return False
    return True

# Поиск элемента на странице по class
def check_exists_by_class(driver, class_name):
    try:
        driver.find_element(By.CLASS_NAME, class_name)
    except NoSuchElementException:
        return False
    return True

# Авторизация в Яндекс ID
def log_in_yandex(login=login_yandex, password=password_yandex):
    try:
        # Создаем подключение
        driver = creating_driver()

        # Нажимаем на кнопку "Почта", чтобы авторизоваться по email
        email_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]' \
                             '/form/div[1]/div[1]/button'
        driver.find_element(By.XPATH, email_button_xpath).click()
        time.sleep(2)

        # Находим поле и вводим email, жмем кнопку "Войти"
        email_input = driver.find_element(By.ID, 'passp-field-login')
        email_input.clear()
        email_input.send_keys(login)
        time.sleep(2)
        driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(2)

        # Проверяем правильно ли ввели email
        if check_exists_by_id(driver, 'field:input-login:hint'):
            return False

        # Находим поле и вводим password, жмем кнопку "Войти"
        password_input = driver.find_element(By.ID, 'passp-field-passwd')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(2)
        driver.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(2)

        # Проверяем правильно ли ввели пароль
        if check_exists_by_id(driver, 'field:input-passwd:hint'):
            return False

        # Проверяем удалось ли дойти до этапа подтверждения номера телефона или авторизовались
        # (подтверждения номера телефона не требовалось). Если да - считаем, что авторизовались.
        if check_exists_by_class(driver, 'auth-challenge-wrapper') or \
                check_exists_by_class(driver, 'Section_link__pZJDa'):
            return True
        else:
            return False
    except Exception as ex:
        print(ex)
        return False
    finally:
        driver.close()
        driver.quit()

# Заметки
# # Создаем фейковый user-agent (1 вариант)
# import random
# user_agents_list = [
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36',
# ]
# options = webdriver.ChromeOptions()
# options.add_argument(f'user-agent={random.choice(user_agents_list)}')

# # Создаем фейковый user-agent (2 вариант)
# # from fake_useragent import UserAgent
# useragent = UserAgent()
# options = webdriver.ChromeOptions()
# options.add_argument(f'user-agent={useragent.random}')
