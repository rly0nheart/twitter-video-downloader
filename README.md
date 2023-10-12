# Twitter Downloader
![Screenshot 2023-01-07 043340](https://user-images.githubusercontent.com/74001397/211127644-4caa35c2-7afe-4555-bb7d-21a363448ba2.png)


[![CodeQL](https://github.com/rly0nheart/twitter-video-downloader/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/twitter-video-downloader/actions/workflows/codeql.yml)

A program for downloading videos from Twitter, given a video url

# Installation
## Install with pip
```
pip install git+https://github.com/rly0nheart/twitter-video-downloader
```
> You will need to have the FireFox browser installed and geckodriver properly set up.

## Building from source
**1.** Clone the repository
```
git clone https://github.com/rly0nheart/twitter-video-downloader
```

**2.** Navigate to the cloned repository
```
cd twitter-video-downloader
```

### Building the Docker container
```
docker build --tty my-twitter-video-downloader .
```

### Building the twitter-video-downloader package
#### Linux
Find the `install.sh` script and run it
```
./install.sh
```
> This assumes the script was already made executable with the `chmod +x uninstall.sh` command.



#### Windows
**1.** Navigate to the twitter-video-downloader directory
Find the `install.ps1` script and run it
```
.\install.ps1
```
> The installation scripts will download and setup geckodriver, then install **twitter-video-downloader**.

# Usage
## Package
```
twitter_video_downloader <video-url>
```

## Docker
```
docker run --tty --volume $PWD/twitter_downloader:/app/twitter_downloader my-twitter-video-downloader <twitter_video_url>
```


# Optional Arguments
| Flag             |      Description      |       Choices       | Default |
|------------------|:---------------------:|:-------------------:|:-------:|
| ``-q/--quality`` | specify video quality | [576x1024, 480x652] | 320x568 |
| ``-d/--debug``   |   enable debug mode   |                     |         |

# Donations
If you would like to donate, you could Buy A Coffee for the developer using the button below

<a href="https://www.buymeacoffee.com/_rly0nheart"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=_rly0nheart&button_colour=40DCA5&font_colour=ffffff&font_family=Comic&outline_colour=000000&coffee_colour=FFDD00" /></a>


Your support will be much appreciated!
