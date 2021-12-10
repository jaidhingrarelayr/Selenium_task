from list_price import list_finder


def weather(browser):

    temparature = browser.find_element_by_id("weather")
    return int(temparature.text[:-2])

def click_buy_sunscreens_button(browser):
    
    browser.find_element_by_xpath("//button[text() = 'Buy sunscreens']").click()

def spf_50(browser):
    
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'SPF-50') or \
        contains(text(),'spf-50')]/following-sibling::p")
    return list_finder(list_elements)

def spf_30(browser):
    
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'SPF-30') or \
        contains(text(),'spf-30')]/following-sibling::p")
    return list_finder(list_elements)

def select_spf50(browser):
    
    price_list = spf_50(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'SPF-50') or \
        contains(text(),'spf-50')]/following-sibling::p[contains(text(),%s)]/following-sibling::\
            button[text() = 'Add']"%minimum_price).click()

def select_spf30(browser):
    
    price_list = spf_30(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/\
        following-sibling::p[contains(text(),%s)]/following-sibling::\
            button[text() = 'Add']"%minimum_price).click()


def click_buy_moisturizers_button(browser):
    
    browser.find_element_by_xpath("//button[text() = 'Buy moisturizers']").click()

def contains_aloe(browser):
    
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'Aloe')]\
        /following-sibling::p")
    return list_finder(list_elements)

def contains_almond(browser):
    
    list_elements = browser.find_elements_by_xpath("//*[contains(text(),'Almond')]\
        /following-sibling::p")
    return list_finder(list_elements)

def select_aloe(browser):
    
    price_list = contains_aloe(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'Aloe')]/\
        following-sibling::p[contains(text(),%s)]/\
            following-sibling::button[text() = 'Add']"%minimum_price).click()

def select_almond(browser):
    
    price_list = contains_almond(browser)
    minimum_price = str(min(price_list))
    browser.find_element_by_xpath("//*[contains(text(),'Almond')]/\
        following-sibling::p[contains(text(),%s)]/\
            following-sibling::button[text() = 'Add']"%minimum_price).click()
