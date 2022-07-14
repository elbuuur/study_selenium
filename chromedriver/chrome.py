from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options.add_extension(pluginfile)
    if user_agent:
        user_agent = UserAgent()
        options.add_argument(f'user-agent={user_agent.random}')
    driver = webdriver.Chrome(
        service=path,
        chrome_options=options)
    return driver


def main():
    try:
        driver = get_chromedriver(use_proxy=True)
        driver.get('https://www.avito.ru/ufa/kvartiry/prodam/3-komnatnye/')
        time.sleep(25)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
