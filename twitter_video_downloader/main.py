from twitter_video_downloader.downloader import TwitterVideoDownloader


def downloader():
    try:
        TwitterVideoDownloader().download_video()
    except KeyboardInterrupt:
        print("[CTRLC] Process interrupted with Ctrl+C")

    except Exception as e:
        print("[ERROR] An error occurred:", e)
