import os
import argparse
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

version_tag = "2023.1.0.0"
update_check_endpoint = "https://api.github.com/repos/rly0nheart/twitter-video-downloader/releases/latest"


# create the downloads directory if it doesn't already exist
def path_finder():
    os.makedirs("../downloads", exist_ok=True)


# print license note
def notice():
    path_finder()
    notice_msg = f"""
    twitter-video-downloader {version_tag} Copyright (C) 2023  Richard Mwewa

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    """
    print(notice_msg)


# check for updates via the GitHub api
def check_updates():
    notice()
    response = requests.get(update_check_endpoint).json()
    if response['tag_name'] == version_tag:
        # ignore if the program is up-to-date
        pass
    else:
        print(f"[UPDATE] A new release is available ({response['tag_name']}). Run 'pip install --upgrade twitter-video-downloader' to get the updates.")


class TwitterVideoDownloader:
    def __init__(self):
        # create argument parser
        parser = argparse.ArgumentParser(description="twitter-video-downloader — by Richard Mwewa  | https://about.me/rly0nheart")
        parser.add_argument("url", help="twitter video url (eg. https://twitter.com/i/status/0101011010010101101")
        parser.add_argument("-q", "--quality", help="choose video quality (default: %(default)s)", choices=["576x1024", "480x652"], default="320x568")
        parser.add_argument("-d", "--debug", help="enable debug mode (returns network logs)", action="store_true")
        self.args = parser.parse_args()

        # set selenium to --headless (hides the firefox browser)
        option = webdriver.FirefoxOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Firefox(options=option)
        self.download_endpoint = "https://twittervideodownloader.com"

    # select video quality
    def video_quality(self):
        if self.args.quality == "480x652":
            xpath_element = "/html/body/div[2]/div/center/div[7]/div[1]/a"
        elif self.args.quality == "576x1024":
            xpath_element = "/html/body/div[2]/div/center/div[6]/div[1]/a"
        else:
            xpath_element = "/html/body/div[2]/div/center/div[5]/div[1]/a"

        return xpath_element

    def download_video(self):
        path_finder()
        self.driver.get(self.download_endpoint)
        url_entry_field = self.driver.find_element(By.NAME, "tweet")
        url_entry_field.send_keys(self.args.url)
        url_entry_field.send_keys(Keys.ENTER)
        print("[LOAD] Please wait...")
        download_btn = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, self.video_quality())))
        video_url = download_btn.get_attribute('href')

        with requests.get(video_url, stream=True) as response:
            response.raise_for_status()
            with open(os.path.join("../downloads", f"{self.args.url[29:]}.mp4"), "wb") as file:
                for chunk in tqdm(response.iter_content(chunk_size=8192), desc=f"[{self.args.quality}] Downloading: {file.name}"):
                    file.write(chunk)
                print(f"[{self.args.quality}] Downloaded:", file.name)
        self.driver.close()
