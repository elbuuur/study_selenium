# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import time


user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent.random}')

# set proxy
options.add_argument('--proxy-server=91.132.151.232:80')

# url = 'https://www.avito.ru/ufa?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD%D1%8B'
url = 'https://2ip.ru/'
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


