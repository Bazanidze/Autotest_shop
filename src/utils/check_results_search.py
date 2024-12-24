import allure

def check_results_search(num, word_search, word_search_2, element_page):
    if word_search in element_page:
        word_search = element_page
        assert word_search == element_page
    elif word_search_2 in element_page:
        word_search_2 = element_page
        assert word_search_2 == element_page
    else:
        print(num, ':Не верно')