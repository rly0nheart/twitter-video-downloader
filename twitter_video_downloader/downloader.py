import os
import logging
import argparse

import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from . import __author__, __about__, __version__

update_check_endpoint = "https://api.github.com/repos/rly0nheart/twitter-video-downloader/releases/latest"
downloads_directory = os.path.join(os.path.expanduser("~"), "twitter-video-downloader")

# create the downloads directory if it doesn't already exist
def path_finder():
    os.makedirs(downloads_directory, exist_ok=True)


# print license note
def notice():
    return f"""
    twitter-video-downloader {__version__} Copyright (C) 2022-2023  Richard Mwewa

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    """


# check for updates via the GitHub api
def check_updates():
    path_finder()
    print(notice())
    response = requests.get(update_check_endpoint).json()
    remote_version = response.get("tag_name")
    if remote_version != __version__:
        print(f"[UPDATE] A new release is available ({remote_version}). Run 'pip install --force-reinstall --no-deps git+git://github.com/rly0nheart/twitter-video-downloader' to get the updates.")


class TwitterVideoDownloader:
    def __init__(self):
        # create argument parser
        parser = argparse.ArgumentParser(description=f"twitter-video-downloader — by {__author__} ({__about__})")
        parser.add_argument("url", help="twitter video url (eg. https://twitter.com/i/status/0101011010010101101")
        parser.add_argument("-q", "--quality", help="choose video quality (default: %(default)s)", choices=["576x1024", "480x652"], default="320x568")
        parser.add_argument("-d", "--debug", help="enable debug mode", action='store_true')
        self.args = parser.parse_args()
        if self.args.debug:
            logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%H:%M:%S%p', level=logging.DEBUG)
        # set selenium to --headless (hides the firefox browser)
        option = webdriver.FirefoxOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Firefox(options=option)
        self.download_endpoint = "https://twittervideodownloader.com"

    # select video quality
    # returns xpath_element
    def video_quality(self):
        if self.args.quality == "480x652":
            xpath_element = "/html/body/div[2]/div/center/div[7]/div[1]/a"
        elif self.args.quality == "576x1024":
            xpath_element = "/html/body/div[2]/div/center/div[6]/div[1]/a"
        else:
            xpath_element = "/html/body/div[2]/div/center/div[5]/div[1]/a"

        return xpath_element

    # download video
    def download_video(self):
        path_finder()
        print(f"Started downloader with {self.args.url}")
        self.driver.get(self.download_endpoint)
        url_entry_field = self.driver.find_element(By.NAME, "tweet")
        url_entry_field.send_keys(self.args.url)
        url_entry_field.send_keys(Keys.ENTER)
        print("Loading web resource, please wait..")
        download_btn = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, self.video_quality())))
        video_url = download_btn.get_attribute('href')

        with requests.get(video_url, stream=True) as response:
            response.raise_for_status()
            with open(os.path.join(downloads_directory, f"{self.args.url[29:]}.mp4"), 'wb') as file:
                for chunk in tqdm(response.iter_content(chunk_size=8192), desc=f"Downloading {file.name}"):
                    file.write(chunk)
                print(f"{self.args.quality} Downloaded:", file.name)
        self.driver.close()
