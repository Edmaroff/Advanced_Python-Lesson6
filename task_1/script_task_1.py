# Задача №1 из ЛК «Коллекции данных. Словари. Множества»
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Марсель', 'Франция']},
    {'visit11': ['Иркутск', 'Россия']},
    {'visit12': ['Пуна', 'Индия']},
    {'visit13': ['Ангарск', 'Россия']},
    {'visit14': ['Мумбаи', 'Индия']}
]

def search_country(geo_list: list, country: str) -> list:
    result = []
    for geo in geo_list:
        if country in list(geo.values())[0]:
            result.append(geo)
    return result


# Задача №2 из ЛК «Коллекции данных. Словари. Множества»
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def get_unique_id(id_dict):
    result = []
    for id_list in id_dict.values():
        result += id_list
    return sorted(list(set(result)))


# Задача №3 из ЛК «Коллекции данных. Словари. Множества»
queries_1 = [
    'a a a a a a',
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'афиша кино',
    'афиша кино',
    'афиша кино',
    'афиша кино',
    ]

def get_percent_word(queries):
    dict_queries = {}
    for query in queries:
        query = query.split()
        request_length = len(query)
        dict_queries.setdefault(request_length, 0)
        dict_queries[request_length] += 1
    result = {}
    for word, request in dict_queries.items():
        percent_request = round((request / sum(dict_queries.values()) * 100), 2)
        if word % 10 == 1:
            result[f'Поисковых запросов из {word} слова'] = percent_request
        else:
            result[f'Поисковых запросов из {word} слов'] = percent_request
    sorted_tuples = sorted(result.items(), key=lambda item: item[1])
    result = {k: f'{v}%' for k, v in sorted_tuples}
    return result


# Задача №4 из ЛК «Коллекции данных. Словари. Множества»
stats_1 = {'facebook': 550, 'yandex': 1200, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def get_max_key(stats):
    max_element = max(stats.values())
    result = []
    for k, v in stats.items():
        if v == max_element:
            result.append(f'{k} = {v}')
    return result
