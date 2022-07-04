from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import time


user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent.random}')

# url = 'https://www.avito.ru/ufa?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD%D1%8B'
url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
path = Service(r'C:\Users\elbuu\PycharmProjects\selenium\chromedriver\chromedriver.exe')

driver = webdriver.Chrome(
    service=path,
    options=options
)

try:
    driver.get(url=url)
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


