from django.shortcuts import render
import datetime
from.models import Stream, User
# pip install --upgrade google-api-python-client
from apiclient.discovery import build

api_key = "AIzaSyCAL9HUYTpY9vX05h2Wnk5CAmYmPvSxX8E"
youtube = build('youtube', 'v3', developerKey=api_key)

def index(request):
    return render(request, 'sellotape/index.html')
	
def get_channel_videos(request):
    #shuold be added to User
    channel_id = request.user.get_youtube_link()
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None

    while true:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    added_on = datetime.date.today()
    author = request.user()

    for video in videos:
        stream = Stream(author=author,
                        title=video['snippet']['title'],
                        description=video['snippet']['description'],
                        link='https://www.youtube.com/watch?v='+video['snippet']['resourceId']['videoId'],
                        airs_on=datetime.datetime.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%S%z").date(),
                        added_on=added_on)
        stream.save()

    return render(request, 'sellotape/index.html')
