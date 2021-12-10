from time import sleep

def goto_cart(browser):
    
    browser.find_element_by_xpath("//button[contains(text(),'Cart -')]").click()

def click_pay_with_card(browser):
    
    browser.find_element_by_xpath("//button[@type = 'submit']").click()

def fill_cart(browser):
    
    browser.switch_to.frame("stripe_checkout_app")
    browser.find_element_by_xpath("//input[@type = 'email']").send_keys("sample@gmail.com")
    sleep(5)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']").send_keys('5555 5555 5555 4444')
    sleep(10)
    browser.find_element_by_xpath("//input[@placeholder = 'MM / YY']").send_keys('12 / 23')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'CVC']").send_keys('679')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'ZIP Code']").send_keys('201301')
    sleep(2)

def pay(browser):
    
    browser.find_element_by_xpath("//button[@type='submit' and \
        @class='Button-animationWrapper-child--primary Button']").click()
    browser.switch_to_default_content()
    sleep(5)
    return "success" if browser.title == "Confirmation" else "failed"