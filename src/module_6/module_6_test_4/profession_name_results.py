import allure
import logging


def profession_name(lenght, blocks_name_professions):
    logging.info('Test 4: checking the names of professions by filters ')
    with allure.step('Проверка названий профессий по введённым фильтрам'):
        prof_1 = 'Python-разработчик'
        prof_2 = 'Data scientist'
        prof_3 = 'Data Scientist с нуля до Junior'
        prof_4 = 'Разработчик'
        prof_5 = 'Data-аналитик'
        prof_6 = 'Machine Learning Engineer'
        prof_7 = 'Инженер по автоматизации тестирования'
        for position in range(lenght):
            text_name_block = blocks_name_professions[position].text
            assert (prof_1 in text_name_block or prof_2 in text_name_block or prof_3 in text_name_block
                    or prof_4 in text_name_block or prof_5 in text_name_block
                    or prof_6 in text_name_block or prof_7 in text_name_block) is True
