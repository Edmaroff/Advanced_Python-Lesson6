import unittest
from task_2.script_task_2 import YandexDisk, TOKEN


class TestFunc(unittest.TestCase):
    def test_create_folder(self):
        ya = YandexDisk(token=TOKEN)
        result = ya.create_folder('Папка тест')
        status_code = [200, 201, 409]
        self.assertIn(result, status_code)

    def test_check_folder(self):
        ya = YandexDisk(token=TOKEN)
        result = ya.check_folder('Папка тест')
        status_code = [200, 201]
        self.assertIn(result, status_code)
