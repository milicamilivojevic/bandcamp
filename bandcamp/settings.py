# Scrapy settings for bandcamp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import urllib.request
import zipfile
from pathlib import Path
import os


BOT_NAME = 'bandcamp'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36)'
COOKIES_DEBUG=True
COOKIES_ENABLED=True


SPIDER_MODULES = ['bandcamp.spiders']
NEWSPIDER_MODULE = 'bandcamp.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ANTI_CAPTCHA_API_KEY = "097662c5a79b23482aa20b791bad3d91"
USERNAME = 'dcollect'
PASSWORD = 'yP!!k258aGh2'


GENERAL_MAP = {
    'wishlist': {'field': 'items', 'url': 'https://bandcamp.com/api/fancollection/1/wishlist_items'},
    'collection': {'field': 'items', 'url': 'https://bandcamp.com/api/fancollection/1/collection_items'},
    'astists': {'field': 'followeers', 'url': 'https://bandcamp.com/api/fancollection/1/following_bands'},
    'genres': {'field': 'followeers', 'url': 'https://bandcamp.com/api/fancollection/1/following_genres'},
}

ITEM_PIPELINES = {
    'bandcamp.pipelines.BandcampPipeline' : 100,
 }



def prepare_env():
    url = 'https://antcpt.com/anticaptcha-plugin.zip'
    # download the plugin
    filehandle, _ = urllib.request.urlretrieve(url)
    # unzip it
    with zipfile.ZipFile(filehandle, "r") as f:
        f.extractall("plugin")

    # set API key in configuration file
    file = Path('./plugin/js/config_ac_api_key.js')
    file.write_text(file.read_text().replace("antiCapthaPredefinedApiKey = ''",
                                             "antiCapthaPredefinedApiKey = '{}'".format(ANTI_CAPTCHA_API_KEY)))

    # zip plugin directory back to plugin.zip
    zip_file = zipfile.ZipFile('./plugin.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk("./plugin"):
        for file in files:
            path = os.path.join(root, file)
            zip_file.write(path, arcname=path.replace("./plugin/", ""))
    zip_file.close()
    print('Plugin installed!')

prepare_env()