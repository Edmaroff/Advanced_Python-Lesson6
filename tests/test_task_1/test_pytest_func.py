import pytest
from task_1.script_task_1 import get_percent_word, get_max_key

FIXTURE_1 = [
    (['1слово', '2 слова', '3 _ слова'], {'Поисковых запросов из 1 слова': '33.33%',
                                          'Поисковых запросов из 2 слов': '33.33%',
                                          'Поисковых запросов из 3 слов': '33.33%'}),
    (['1слово', '2 слова', '3 _ слова', '1слово', '1слово'], {'Поисковых запросов из 2 слов': '20.0%',
                                                              'Поисковых запросов из 3 слов': '20.0%',
                                                              'Поисковых запросов из 1 слова': '60.0%'}),
    (['1слово'], {'Поисковых запросов из 1 слова': '100.0%'})
]


# Параметризовал распределение количества слов в разных запросах (списках)
@pytest.mark.parametrize('queries, etalon', FIXTURE_1)
def test_get_percent_word(queries, etalon):
    result = get_percent_word(queries)
    assert result == etalon


FIXTURE_2 = [
    ({'facebook': 550, 'yandex': 1200, 'vk': 15, 'google': 99, 'email': 42, 'ok': 98},
     ['yandex = 1200']),
    ({'facebook': 10, 'yandex': 1, 'vk': 11, 'ok': 98, 'google': 98},
     ['ok = 98', 'google = 98']),
    ({'facebook': -550, 'yandex': -1200, 'vk': -15, 'google': -99, 'email': -42, 'ok': -98},
     ['vk = -15'])
]


# Параметризовал поиск значений по максимальному ключу в разных словарях
@pytest.mark.parametrize('stats, etalon', FIXTURE_2)
def test_get_max_key(stats, etalon):
    result = get_max_key(stats)
    assert result == etalon
