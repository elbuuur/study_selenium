from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import sys
import zipfile
sys.path.append(".")
from config import Config


# set proxy
PROXY_USER = Config.LOGIN
PROXY_PASS = Config.PASSWORD
PROXY_HOST = Config.PROXY
PROXY_PORT = Config.PORT

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    path = Service(r'C:\Users\elbuu\PycharmProjects\selenium\chromedriver\chromedriver.exe')

    options = webdriver.ChromeOptions()

    # disable webdriver mode

    # for older ChromeDriver under version 79
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_experimental_option('useAutomationExtension', False)

    # for ChromeDriver version 79 and over
    options.add_argument('--disable-blink-features=AutomationControlled')

    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options.add_extension(pluginfile)
    if user_agent:
        user_agent = UserAgent()
        options.add_argument(f'user-agent={user_agent.random}')

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        service=path,
        options=options)
    return driver


def main():
    try:
        driver = get_chromedriver(use_proxy=True)
        driver.get('https://www.avito.ru/ufa/kvartiry/prodam/3-komnatnye/')

        driver.implicitly_wait(5)

        items = driver.find_elements(By.XPATH, "//div[@data-marker='item']")

        driver.implicitly_wait(5)

        info = {}

        for x, item in enumerate(items):
            print(item.find_element(By.XPATH, "//a[@data-marker='item-title']").get_property('href'))
        # print(info)

        time.sleep(25)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
