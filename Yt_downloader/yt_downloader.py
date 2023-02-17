from pytube import YouTube,Playlist
from pytube.cli import on_progress
from datetime import datetime
from unidecode import unidecode
import os
import json
import re

# downloading video or playlist function

def download_video_playlist():

    VIDEO_RE = r'^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$'
    PLAYLIST_RE = r'^https?:\/\/(www.youtube.com|youtube.com)\/playlist(.*)$'
    JSON_SAVE = r'Py_Video_Downloader/videoData.json'
    DATETIME = datetime.now().strftime('%d/%m/%Y %H:%M') 
    video_title = URL_Type = ''
    video_qnt = 1

    YT_Url = str(input('\nInput the Youtube Video or Playlist Here\n : ')).strip().replace(' ','') # get the user input and removes the blank spaces or ''
    print()

    try:

        if re.match(PLAYLIST_RE,YT_Url): # verifies if the url matches a youtube playlist

            yt_playlist = Playlist(YT_Url)
            playlist_title = str(yt_playlist.title) # getting the playlist title
            URL_Type = 'Playlist'
            video_qnt = len(yt_playlist)

            for video in yt_playlist.videos: # get all videos in playlist title and shows the download bar for every single one
                
                video_playlist_title = video.title
                video_title = playlist_title
                os.system('cls')
                print(f"\n[INFO] : Downloading Playlist '{playlist_title}' - '{video_playlist_title}'\n")
                video.register_on_progress_callback(on_progress)
                video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Py_Video_Downloader/my_downloads')

        elif re.match(VIDEO_RE,YT_Url): # verifies if the url matches a youtube video

            yt_video = YouTube(YT_Url,on_progress_callback=on_progress)
            video_title = str(yt_video.title) # get the video title 
            URL_Type = 'Video'

            os.system('cls')
            print(f'[INFO] : Downloading ' + f"{video_title}",'\n') # will download the video
            yt_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Py_Video_Downloader/my_downloads')

        else:
            os.system('cls')
            raise ValueError(f"URL '{YT_Url}' is not Valid. Try Again ! \n")
        
        print()
        print('\n[INFO] : Download was Suceeded ! Files at Py_YT_Downloader/my_downloads. \n')

        bd_data = {'TITLE':f'{unidecode(video_title)}','TYPE': f'{URL_Type}','LINK':f'{YT_Url}','VIDEO QUANTITY':f'{video_qnt}','DOWNLOADED':f'{DATETIME}'} # this is a dict for saving download data at a json archive

        with open(JSON_SAVE,'a') as data_archive: # code to save the data and create the actual archive. 'a' is for append and not overwrite data
            json.dump(bd_data,data_archive,ensure_ascii=False,indent=2)

        return download_video_playlist()

    except Exception as e: # exception for possible errors
        print(f'\n[ERROR] : {e}')
        return download_video_playlist()

if __name__ == '__main__':
    download_video_playlist()
