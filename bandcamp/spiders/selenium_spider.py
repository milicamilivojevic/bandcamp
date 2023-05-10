import time
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from selenium import webdriver
import json
from pyvirtualdisplay import Display
from bandcamp.settings import *


class SeleniumSpider(scrapy.Spider):
    name = 'selenium'

    def __init__(self):
        self.fan_id = None
        self.cookies = None
        self.payload = None
        self.count = 99  # to avoid a lot of paginations
        options = webdriver.ChromeOptions()
        options.add_extension('./plugin.zip')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--headless')
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Chrome('chromedriver', options=options)
        self.headers = {
            'Content-Type': 'application/json',
        }

    def set_headers(self):
        """
        Log in to webiste and set needed cookies for API
        """
        self.driver.get('https://bandcamp.com/login?from=home')
        self.driver.execute_script('return navigator.webdriver')
        self.driver.find_element('id', 'username-field').send_keys(USERNAME)
        self.driver.find_element('id', 'password-field').send_keys(PASSWORD)
        time.sleep(5)
        self.driver.find_element('xpath', './/button[@type="submit"]').click()
        # webdriver.support.wait.WebDriverWait(self.driver, 120).until(lambda x: x.find_element_by_id('fan-bio-vm'))
        time.sleep(20)
        self.cookies = {cookie["name"]: cookie["value"] for cookie in self.driver.get_cookies()}
        self.fan_id = \
        json.loads(self.driver.find_element('id', 'pagedata').get_attribute('data-blob'))['identities']['fan']['id']
        timestamp = int(time.time())
        self.payload = {"fan_id": self.fan_id,
                        "older_than_token": f"{timestamp}:{timestamp + 600000}:a::",  # ~7 days +-
                        "count": self.count}
        self.driver.close()

    def start_requests(self):
        self.set_headers()
        for type in GENERAL_MAP.keys():
            yield scrapy.Request(GENERAL_MAP[type]['url'],
                                 callback=self.parse,
                                 method='POST',
                                 body=json.dumps(self.payload),
                                 cookies=self.cookies,
                                 headers=self.headers,
                                 meta={'type': type})

    def parse(self, response):
        json_response = json.loads(response.text)
        more = json_response['more_available']
        type = response.meta['type']
        if more:
            self.payload['older_than_token'] = json_response['last_token']
            yield scrapy.Request(response.url,
                                 callback=self.parse,
                                 method='POST',
                                 body=json.dumps(self.payload),
                                 cookies=self.cookies,
                                 headers=self.headers,
                                 meta={'type': type})
        items = json_response[GENERAL_MAP[type]['field']]
        for item in items:
            yield {'type': type, 'data': item}


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(SeleniumSpider)
    process.start()
