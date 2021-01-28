from selenium import webdriver
from selenium.common.exceptions import *
import time

hex_dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"

}


def split(word):
    return [char for char in word]


def translate_hex(h):
    h = split(h)
    h[0] = hex_dict[h[0]]
    try:
        h[1] = hex_dict[h[1]]
    except IndexError:
        h = ["0000", h[0]]

    return "".join(h)


if __name__ == "__main__":
    driver = webdriver.Chrome("/Users/nathanbaines/PycharmProjects/web_scraping_test/chromedriver")
    url = "https://flippybitandtheattackofthehexadecimalsfrombase16.com/"
    driver.get(url)

    enemy_num = 1

    print("Please start the game.")
    time.sleep(10)

    columns = [driver.find_element_by_xpath("//*[@id='game']/div[25]"),
               driver.find_element_by_xpath("//*[@id='game']/div[23]"),
               driver.find_element_by_xpath("//*[@id='game']/div[21]"),
               driver.find_element_by_xpath("//*[@id='game']/div[19]"),
               driver.find_element_by_xpath("//*[@id='game']/div[17]"),
               driver.find_element_by_xpath("//*[@id='game']/div[15]"),
               driver.find_element_by_xpath("//*[@id='game']/div[13]"),
               driver.find_element_by_xpath("//*[@id='game']/div[11]")]

    # Main loop
    try:
        while True:
            missiles = [driver.find_element_by_xpath("//*[@id='game']/div[26]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[24]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[22]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[20]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[18]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[16]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[14]"),
                    driver.find_element_by_xpath("//*[@id='game']/div[12]")]

            for x in range(0, 8):
                if missiles[x].__class__ == "missile in-dock selected hover":
                    columns[x].click()

            try:
                enemy = driver.find_element_by_id("enemy-{}".format(enemy_num))
            except NoSuchElementException:
                continue

            enemy_num += 1
            enemy_hex = enemy.text

            enemy_binary = translate_hex(enemy_hex)

            enemy_binary = split(enemy_binary)

            for x in range(0, 8):
                if enemy_binary[x] == "1":
                    columns[x].click()

            time.sleep(2)

    except KeyboardInterrupt:
        print("Quitting...")
        driver.quit()
