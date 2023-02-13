from pytube import YouTube,Playlist
from pytube.cli import on_progress
import re

SINGLE_VIDEO = 1
FULL_PLAYLIST = 2
EXIT = 3

video_url_regex = r'^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$'
playlist_url_regex = r'((http(s)?:\/\/)?)(www\.)?((youtube\.com\/)|(youtu.be\/))[\S]+'


# function that starts the app

def start_app():

    try:
        download_choice = int(input('1 - Single Video \n2 - Playlist\n3 - Exit\n : '))

        if download_choice not in [SINGLE_VIDEO,FULL_PLAYLIST,EXIT]:
            raise ValueError('Input must be 1 or 0 ! ')

    except Exception as e:
        print(f'\n[INFO] : {e} \n')
        return start_app()

    if download_choice == SINGLE_VIDEO:
        return download_single_video()
    elif download_choice == FULL_PLAYLIST:
        return download_full_playlist()
    else:
        exit()

    
# downloading a single video function

def download_single_video():

    video_link = str(input('\nInput the Youtube Link Here\n : '))
    print()

    try:

        if not re.match(video_url_regex,video_link):
            raise ValueError('Input a Valid Video URL ! \n')
        else:
            yt = YouTube(video_link,on_progress_callback=on_progress)
            print(f'[INFO] : Downloading ' + f"{str(yt.title)}",'\n')
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('YT_Video_Downloader/my_video_downloads')
            print('')
            print('\n Videos Located in YT_Video_Downloader/my_video_downloads !\n')
            return start_app()

    except Exception:
        print(f'\n[INFO] : Use a Single Video URL, Not Playlist ! \n')
        return download_single_video()


# downloading a full playlist function

def download_full_playlist():

    playlist_link = str(input('\nInput the Youtube Playlist Link Here\n : '))
    print()

    try:

        if not re.match(playlist_url_regex,playlist_link):
            raise ValueError('Input a Valid Playlist URL ! \n')
        else:
            yt_p = Playlist(playlist_link)
            print(f'\n[INFO] : Downloading Playlist ' + f"{str(yt_p.title)}",'\n')

            for video in yt_p.videos:
                video.register_on_progress_callback(on_progress)
                video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('YT_Video_Downloader/my_playlist_downloads')

            print('')
            print('\n Videos Located in YT_Video_Downloader/my_playlist_downloads !\n')
            return start_app()

    except Exception:
        print(f'\n[INFO] : Use a Playlist URL, Not Video ! \n')
        return download_full_playlist()

if __name__ == '__main__':
    start_app()