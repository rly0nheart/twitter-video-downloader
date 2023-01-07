# Twitter Downloader

[![CodeQL](https://github.com/rly0nheart/twitter-video-downloader/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/twitter-video-downloader/actions/workflows/codeql.yml)

A program for downloading videos from Twitter, given a video url

# Installation
## Install with pip
```
pip install git+https://github.com/rly0nheart/twitter-video-downloader
```

### Note
> You will need to have the FireFox browser installed on your pc (pip package)
>> The program is dependent on selenium, so in order to run it, you will also have to download and properly setup geckodriver (see setup instructions available below)

# Docker
## Build
```
docker build -t twitter-video-downloader .
```
### Note
> The docker image will download and setup geckodriver

# Geckodriver setup
## Linux
**1. Go to the geckodriver [releases page](https://github.com/mozilla/geckodriver/releases/). Find the latest version of the driver for your platform and download it**

**2. Extract the downloaded file**
```
tar -xvzf geckodriver*
```
**3. Add geckodriver to your system path**
```
export PATH="/path/to/downloaded/geckodriver:$PATH"
```

### Note
> If you encounter issues with the above commands, then you should run them as root


## Windows
**1. Go to the geckodriver [releases page](https://github.com/mozilla/geckodriver/releases/). Find the geckodriver.exe binary for your platform and download it**

**2. Move the downloaded executable to** *C:\Users\username\AppData\Local\Programs\Python\Python310*

### Note
> The numbers on the directory 'Python310' will depend on the version of Python you have

## Mac OS
* [Set up Selenium & GeckoDriver (Mac)](https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac-b411dbfe61bc)


# Usage
```
twitter_video_downloader <video-url>
```

# Docker
```
 docker run -it -v $PWD/twitter_downloads:/app/twitter_downloads twitter-video-downloader <twitter_video_url>
```
## Note
> The url format should be as follows;  https://twitter.com/i/status/0101011010010101101


# Optional Arguments
| Flag             |      Description      |       Choices       | Default |
|------------------|:---------------------:|:-------------------:|:-------:|
| ``-q/--quality`` | specify video quality | [576x1024, 480x652] | 320x568 |
| ``-d/--debug``   |   enable debug mode   |                     |         |

# Donations
If you would like my work and would like to support, you could Buy Me A Coffee using the button below

<a href="https://www.buymeacoffee.com/189381184" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated!😊
