from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime


def get_menu_prices():
    menu_prices = {}
    for x in store:
        if x.text != "":
            price = int(x.text.strip().split("-")[1].replace(",", ""))
            menu_prices[x.text.split("-")[0].strip()] = price

    return menu_prices


def get_most_expensive_item(available_money):
    higher_price = 0
    affordable_item_name = ""
    for n in store:
        if n.text != "":
            item_price = int(n.text.strip().split("-")[1].replace(",", ""))
            if available_money > item_price > higher_price:
                higher_price = item_price
                affordable_item_name = n.text.split("-")[0].strip()

    return affordable_item_name


url = "https://orteil.dashnet.org/experiments/cookie/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url)

cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

store_prices = get_menu_prices()

end_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
while datetime.datetime.now() < end_time:
    checking_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
    while datetime.datetime.now() < checking_time:
        cookie.click()

    money = driver.find_element(By.ID, value="money").text
    if "," in money:
        money = money.replace(",", "")

    # Update store list
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    buy_item = get_most_expensive_item(int(money))

    if buy_item != "":
        print(f"Bought {buy_item} with the Total: {money}")
        driver.find_element(By.ID, value=f"buy{buy_item}").click()

print(driver.find_element(By.ID, value="cps").text)

driver.quit()
