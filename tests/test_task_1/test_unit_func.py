import unittest
from task_1.script_task_1 import search_country, geo_logs, get_unique_id
from parameterized import parameterized

FIXTURE_1 = [
    ('Индия', [{'visit2': ['Дели', 'Индия']}, {'visit12': ['Пуна', 'Индия']}, {'visit14': ['Мумбаи', 'Индия']}]),
    ('Франция', [{'visit5': ['Париж', 'Франция']}, {'visit10': ['Марсель', 'Франция']}]),
    ('Португалия', [{'visit4': ['Лиссабон', 'Португалия']}, {'visit6': ['Лиссабон', 'Португалия']}])
]

FIXTURE_2 = [
    ({'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]},
     [15, 35, 54, 98, 119, 213]),
    ({'user4': [1, 2, 3, 4], 'user5': [1, 100, 423, 432], 'user6': [1, 2, 3, 4, 423, 100]},
     [1, 2, 3, 4, 100, 423, 432]),
    ({'user7': [213, 4, 213, 23, 41], 'user8': [0, 0, 119, 119, 119], 'user9': [89, 54, 1, 56]},
     [0, 1, 4, 23, 41, 54, 56, 89, 119, 213])
]

class TestFunc(unittest.TestCase):
    # Параметризовал поиск разных стран в одном списке
    @parameterized.expand(FIXTURE_1)
    def test_search_country(self, country, etalon):
        result = search_country(geo_logs, country)
        self.assertListEqual(result, etalon)

    # Параметризовал поиск уникальных id в разных словарях
    @parameterized.expand(FIXTURE_2)
    def test_get_unique_id(self, id_dict, etalon):
        result = get_unique_id(id_dict)
        self.assertListEqual(result, etalon)


