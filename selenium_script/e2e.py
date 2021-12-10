from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from page_objects import weather
from page_objects import click_buy_sunscreens_button, select_spf50, select_spf30, click_buy_moisturizers_button, select_aloe, select_almond
from checkout_payment import goto_cart, click_pay_with_card, fill_cart, pay

def add_sunscreens():

    click_buy_sunscreens_button(browser)
    print("Successfully moved to the sunscreen page")
    select_spf50(browser)
    print("Least Priced SPF-50 product added to the cart..")
    select_spf30(browser)
    print("Least Priced SPF-30 product added to the cart..")

def add_moisturizers():

    click_buy_moisturizers_button(browser)
    print("successfully moved to Moisturizers page")
    select_aloe(browser)
    print("Least priced ALOE product added to the cart..")
    select_almond(browser)
    print("Least Priced ALMOND product is added to the cart..")

def checkout():

    goto_cart(browser)
    print("Successfully Moved to the cart")
    sleep(3)
    click_pay_with_card(browser)
    print("Pay with card clicked")
    fill_cart(browser)
    print("Payment details filled...")
    sleep(2)
    message = pay(browser)
    print("payment", message)

if __name__ == "__main__":
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://weathershopper.pythonanywhere.com/")
    if browser.title == "Current Temperature":
        print("Owsome: Landed over right page")
    else:
        print("Error: Landed over wrong page")
    temperature = weather(browser)
    print("Temperature found: ", temperature)
    if temperature > 34:
        add_sunscreens()
        checkout()
    elif temperature < 19:
        add_moisturizers()
        checkout()
    else:
        print("Hurrah!! It's All Good, No need for shopping")
    sleep(10)
    browser.close()
