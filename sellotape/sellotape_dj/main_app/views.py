from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Stream, Profile, UserFollowers


def index(request):
    return render(request, 'sellotape/index.html')


def feed(request, username):
    # Get the profile for the passed username or raise 404 if not found.
    # If found, retrieve the profiles he follows.
    # Extracts the streams of these profiles.
    profile = get_object_or_404(Profile, user__username=username)
    userfollowers = UserFollowers.objects.filter(follow_from=profile)

    future_streams, previous_streams, live_streams = [], [], []
    now = timezone.now()

    for follower in userfollowers:
        for s in Stream.objects.filter(author=follower.follow_to):
            if s.airs_on > now:
                future_streams.append(s)
            else:
                if s.ends_on and s.ends_on > now:
                    live_streams.append(s)
                else:
                    previous_streams.append(s)

    context = {
        'profile': profile,
        'future_streams': future_streams,
        'previous_streams': previous_streams,
        'live_streams': live_streams,
    }
    return render(request, 'feed.html', context)