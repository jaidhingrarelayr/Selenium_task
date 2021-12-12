# Flink_Task
# Automation tests for Weather Shopping Url
These tests aim to ensure that current functionalities on the dashboard are properly working.


## How to setup
- Checkout the project
- cd selenium_test
- Install python
- Run ```pip install -U selenium```
- Run ```pip install webdriver-manager```


## How to run test
Steps:
- Go to folder: ```cd selenium_tests```
- Run ```python3 e2e.py '```


## Setup for Firefox
- In e2e.py add
'''from selenium import webdriver'''
'''from webdriver_manager.firefox import GeckoDriverManager'''

'''browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())'''


## Setup for Chrome
- In e2e.py add
'''from selenium import webdriver'''
'''from webdriver_manager.chrome import ChromeDriverManager'''

'''driver = webdriver.Chrome(ChromeDriverManager().install())'''