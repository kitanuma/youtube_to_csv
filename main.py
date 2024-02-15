from scraper import *

videos = get_playlist("https://youtube.com/playlist?list=PLhkfLVDQ8gKqBI-ctlcUxmfa7q9KAOS9P&feature=shared")
for video in videos:
    print(video)