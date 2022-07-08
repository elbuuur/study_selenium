from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import time


user_agent = UserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent.random}')

# path to driver
path = Service(r'C:\Users\iRu\PycharmProjects\selenium\chromedriver\chromedriver.exe')
# path = Service(r'C:\Users\elbuu\PycharmProjects\selenium\chromedriver\chromedriver.exe')

# set proxy
login = ''
password = ''
proxy = ''

proxy_options = {
    'proxy': {
        'https': f"https://:{login}:{password}@{proxy}"
    }
}

url = 'https://2ip.ru/'

driver = webdriver.Chrome(
    service=path,
    seleniumwire_options=proxy_options,
    options=options
)

try:
    driver.get(url=url)
    time.sleep(25)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


