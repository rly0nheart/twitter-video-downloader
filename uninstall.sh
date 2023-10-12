#!/bin/bash

# Remove the geckodriver binary from /usr/bin
sudo rm /usr/bin/geckodriver -v

# Uninstall twitter-video-downloder
pip3 uninstall twitter-video-downloader -y -v
echo "Cleanup complete.