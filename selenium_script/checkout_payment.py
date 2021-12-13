from time import sleep

def goto_cart(browser):
    
    browser.find_element_by_xpath("//button[contains(text(),'Cart -')]").click()

def click_pay_with_card(browser):
    
    browser.find_element_by_xpath("//button[@type = 'submit']").click()

def fill_cart(browser):
    
    browser.switch_to.frame("stripe_checkout_app")
    browser.find_element_by_xpath("//input[@type = 'email']").send_keys("flink@gmail.com")
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']").send_keys("4242")
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']").send_keys("4242")
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']").send_keys("4242")
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']").send_keys("4242")
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'MM / YY']").send_keys('12 / ')
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'MM / YY']").send_keys('23')
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'CVC']").send_keys('679')
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'ZIP Code']").send_keys('201301')
    sleep(2)

def pay(browser):
    
    browser.find_element_by_xpath("//button[@type = 'submit']").click()
    browser.switch_to_default_content()
    sleep(5)
    return "success" if browser.title == "Confirmation" else "failed"