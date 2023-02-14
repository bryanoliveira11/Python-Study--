from pytube import YouTube,Playlist
from pytube.cli import on_progress
import re

video_url_re = r'^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$'
playlist_url_re = r'^https?:\/\/(www.youtube.com|youtube.com)\/playlist(.*)$'

# downloading video or playlist function

def download_video_playlist():

    YT_Url = str(input('\nInput the Youtube Video or Playlist Here\n : ')).strip().replace(' ','')
    print()

    try:

        if re.match(playlist_url_re,YT_Url):
            yt_p = Playlist(YT_Url)
            print(f'\n[INFO] : Downloading Playlist ' + f"{str(yt_p.title)}",'\n')

            for video in yt_p.videos:
                video.register_on_progress_callback(on_progress)
                video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Py_Video_Downloader/my_playlist_downloads')

            print('')
            print('\n Videos Located in Py_Video_Downloader/my_playlist_downloads !\n')

        elif re.match(video_url_re,YT_Url):
            yt = YouTube(YT_Url,on_progress_callback=on_progress)
            print(f'[INFO] : Downloading ' + f"{str(yt.title)}",'\n')
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Py_Video_Downloader/my_video_downloads')
            print('')
            print('\n Videos Located in Py_Video_Downloader/my_video_downloads !\n')

        else:
            raise ValueError('\n[ERROR] : Input a Valid Video or Playlist URL ! \n')

        return download_video_playlist()

    except Exception:
        print(f'\n[ERROR] : Input a Valid Video or Playlist URL ! \n')
        return download_video_playlist()

if __name__ == '__main__':
    download_video_playlist()
