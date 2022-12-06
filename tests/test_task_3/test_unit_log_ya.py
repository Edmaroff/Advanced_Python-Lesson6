import unittest
from task_3.script_task_3 import (
    check_exists_by_id, check_exists_by_class, log_in_yandex,
    login_yandex, password_yandex, path_driver, creating_driver
)
from parameterized import parameterized

FIXTURE_1 = [
    (login_yandex, password_yandex, True), # действующий логин и пароль
    ('edge85021', 'неверный_пароль', False), # существующий логин, но неверный пароль
    ('неверный_логин', 'netology', False) # несуществующий логин и пароль
]

FIXTURE_2 = [
    ('passp:sign-in', True), # существующий ID на странице
    ('qqqqq:qqqq-qq', False) # несуществующий class на странице
]

FIXTURE_3 = [
    ('passp-auth-content', True), # существующий class на странице
    ('qqqqqqqqqqq', False) # несуществующий class на странице
]
class TestFunc(unittest.TestCase):
    # Параметризовал ввод разных логинов и паролей
    @parameterized.expand(FIXTURE_1)
    def test_log_in_yandex(self, login, password, etalon, path=path_driver):
        result = log_in_yandex(login, password)
        self.assertEqual(result, etalon)

    # Параметризовал поиск элементов с разными id
    @parameterized.expand(FIXTURE_2)
    def test_check_exists_by_id(self, id, etalon):
        driver = creating_driver(path_driver)
        result = check_exists_by_id(driver, id)
        driver.close()
        driver.quit()
        self.assertEqual(result, etalon)

    # Параметризовал поиск элементов с разными class
    @parameterized.expand(FIXTURE_3)
    def test_check_exists_by_class(self, class_name, etalon):
        driver = creating_driver(path_driver)
        result = check_exists_by_class(driver, class_name)
        driver.close()
        driver.quit()
        self.assertEqual(result, etalon)