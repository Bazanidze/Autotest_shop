from selenium import webdriver


def duration_training(selenium, test_range_left_button, test_range_right_button):
    action_chains = webdriver.ActionChains(selenium)
    action_chains.click_and_hold(test_range_left_button).move_by_offset(xoffset=40, yoffset=10).perform()
    action_chains.release().perform()
    action_chains.click_and_hold(test_range_right_button).move_by_offset(xoffset=-40, yoffset=10).perform()
    action_chains.release().perform()
