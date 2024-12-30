import allure


def basket_normal_name_option_pizza(basket_name_option):
    basket_name_option = basket_name_option.upper()
    basket_name_option = basket_name_option[0:-5]
    with allure.step(f"Название опции пиццы в корзине: '{basket_name_option}'"):
        return basket_name_option


def normal_name_option_pizza(name_option):
    with allure.step(f"Название выбранной опции из: '{name_option}'"):
        name_option = name_option.upper()
        name_option = name_option[0:-11]
        with allure.step(f"Название опции: '{name_option}'"):
            return name_option


def normal_name_pizza(name_pizza):
    with allure.step(f"Название пиццы из: '{name_pizza}'"):
        name_pizza = name_pizza.upper()
        name_pizza = name_pizza[7:-1]
        with allure.step(f"Название пиццы: '{name_pizza}'"):
            return name_pizza


def normal_name_dessert(name_dessert):
    with allure.step(f"Название десерта из: '{name_dessert}'"):
        name_dessert = name_dessert.upper()
        name_dessert = name_dessert[8:-1]
        with allure.step(f"Название десерта: '{name_dessert}'"):
            return name_dessert
