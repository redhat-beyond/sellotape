from django.utils import timezone
from ..models import Stream, Profile
# pip install --upgrade google-api-python-client
from apiclient.discovery import build

api_key = "AIzaSyCAL9HUYTpY9vX05h2Wnk5CAmYmPvSxX8E"

# get - username.
# extracts each video in user's youtube playlist
# insert the extracted data into Streams DB
# return - number of videos that were inserted, or 404/403 with error message.


def get_channel_videos():
    profiles = Profile.objects.all()

    youtube = build('youtube', 'v3', developerKey=api_key)

    for profile in profiles:
        if profile.youtube_link:
            # get Uploads playlist id
            res = youtube.channels().list(id=profile.youtube_link, part='contentDetails').execute()
            playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            videos = []
            next_page_token = None

            while True:
                res = youtube.playlistItems().list(playlistId=playlist_id,
                                                   part='snippet',
                                                   maxResults=50,
                                                   pageToken=next_page_token).execute()
                videos += res['items']
                next_page_token = res.get('nextPageToken')

                if next_page_token is None:
                    break

            for video in videos:
                stream = Stream(author=profile,
                                title=video['snippet']['title'],
                                description=video['snippet']['description'],
                                link='https://www.youtube.com/watch?v=' + video['snippet']['resourceId']['videoId'],
                                airs_on=video['snippet']['publishedAt'],
                                added_on=timezone.now())
                stream.save()


