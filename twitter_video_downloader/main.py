from twitter_video_downloader.downloader import TwitterVideoDownloader


def start_downloader():
    try:
        TwitterVideoDownloader().download_video()
    except KeyboardInterrupt:
        raise Exception("Process interrupted with Ctrl+C")

    except Exception as e:
        raise Exception(e)
