import time
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    code = input("Enter your room code:")
    name = input("Enter your preferred name:")
    # finds the relative path to the chromedriver
    aPath = os.path.abspath(__file__)
    fileD = os.path.dirname(aPath)
    PATH = os.path.join(fileD, 'chromedriver.exe')
    # sets up webdriver to start on the url with the code given
    driver = webdriver.Chrome(PATH)
    driver.get(url="https://jklm.fun/" + code)
    time.sleep(3)

    # finds name input and ready buttons on the page fills the name in and clicks the button
    name_input = driver.find_element_by_xpath("//input[@class='styled nickname']")
    user_button = driver.find_element_by_xpath("//button[@class='styled']")
    name_input.send_keys(name)
    time.sleep(0.5)
    ActionChains(driver).click(user_button).perform()
    time.sleep(3)

    # gets the iframe the game is running on and finds the join button and input_box.
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.frame(iframe)
    dictionary = driver.find_element_by_xpath("//span[@class='dictionary']")
    join_button = driver.find_element_by_xpath("//button[@class='styled joinRound']")
    input_box = driver.find_element_by_xpath("//input[@type='text']")
    ActionChains(driver).click(join_button).perform()

    with open('usa.txt') as f:
        # gets the word file ready to be used
        word_list = " ".join(f.read().split())

    while True:
        time.sleep(1)
        if input_box.is_displayed() or dictionary.is_displayed():
            # makes sure the browser is ready to play
            if input_box.is_displayed():
                # initialization values for finding syllables in the text file
                first = driver.find_elements_by_class_name('syllable')
                syl = first[0].text.lower()
                index = word_list.find(syl)
                end = index + 0
                start = index - 0
                check_used = True
                # finds where the word starts and ends to remove it from the list
                while True:
                    if word_list[end] == " ":
                        break
                    else:
                        end = end + 1
                while True:
                    if word_list[start] == " ":
                        break
                    else:
                        start = start - 1
                # removes the word from word_list
                word = word_list[start + 1:end]
                word_list = word_list[0: start:] + word_list[end::]
                # sends the word
                input_box.send_keys(word)
                input_box.send_keys(Keys.RETURN)
        else:
            quit()
