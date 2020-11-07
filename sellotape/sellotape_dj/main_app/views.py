from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stream, Profile, UserFollower
from django.db.models import Count


def landing_logged_on(request):
    # Gather my future&live streams
    logged_in_profile = get_object_or_404(Profile, user__username=request.user.username)
    logged_in_streams = Stream.objects.filter(author=logged_in_profile)
    logged_in_streams = logged_in_streams.filter(ends_on__gte=timezone.now())

    logged_in_live = logged_in_streams.filter(airs_on__lt=timezone.now())
    logged_in_future = logged_in_streams.filter(airs_on__gte=timezone.now())

    # Gather user's who the logged in user follows future&live streams
    following = UserFollower.objects.filter(user=logged_in_profile)
    following = [following_profile.follows for following_profile in following]
    streams = Stream.objects.filter(author__in=following)
    streams = streams.filter(ends_on__gte=timezone.now())

    live_streams = streams.filter(airs_on__lt=timezone.now())
    future_streams = streams.filter(airs_on__gte=timezone.now())

    context = {
        'logged_in_live': logged_in_live,
        'logged_in_future': logged_in_future,
        'live_streams': live_streams,
        'future_streams': future_streams,
    }
    return render(request, 'landing_logged_in.html', context)


def landing(request):
    if request.user.is_authenticated:
        return landing_logged_on(request)
    return render(request, 'landing.html')


def user(request, username):
    # Get the profile for the passed username or raise 404 if not found.
    # If found, retrieve the related profile streams.
    profile = get_object_or_404(Profile, user__username=username)
    streams = Stream.objects.filter(author=profile)

    # Check if there is a live stream at the moment.
    live_stream = None
    now = timezone.now()
    for s in streams:
        ongoing = s.ends_on is None or s.ends_on >= now
        if ongoing and s.airs_on <= now:
            live_stream = s
            break

    # Filter streams data based on the current time of serving the page.
    future_streams = [s for s in streams if s.airs_on > now]
    previous_streams = [s for s in streams if s not in future_streams]

    if live_stream in previous_streams:
        previous_streams.remove(live_stream)

    # Check if we currently follow this user
    following = False
    if request.user.is_authenticated:
        temp = UserFollower.objects.filter(user__user__username=request.user.username)
        temp = temp.filter(follows=profile)
        if len(temp) > 0:
            following = True

    context = {
        'following': following,
        'profile': profile,
        'future_streams': future_streams,
        'previous_streams': previous_streams,
        'live_stream': live_stream,
    }
    return render(request, 'user.html', context)


def unfollow(request, username):
    if not request.user.is_authenticated:
        return redirect('main_app:user', username=username)
    to_unfollow = username
    to_unfollow_profile = get_object_or_404(Profile, user__username=to_unfollow)

    follower = request.user.username
    follower_profile = get_object_or_404(Profile, user__username=follower)

    following = UserFollower.objects.filter(user=follower_profile, follows=to_unfollow_profile)
    if len(following) != 1:
        return redirect('main_app:user', username=username)

    following.delete()
    return redirect('main_app:user', username=username)


def follow(request, username):
    if not request.user.is_authenticated:
        return redirect('main_app:user', username=username)
    to_follow = username
    to_follow_profile = get_object_or_404(Profile, user__username=to_follow)

    follower = request.user.username
    follower_profile = get_object_or_404(Profile, user__username=follower)

    following = UserFollower.objects.filter(user=follower_profile, follows=to_follow_profile)
    if len(following) > 0:
        return redirect('main_app:user', username=username)

    user_follow = UserFollower(user=follower_profile, follows=to_follow_profile)
    user_follow.save()
    return redirect('main_app:user', username=username)


def explore(request):

    education_streams = Stream.objects.filter(genre='1')
    gaming_streams = Stream.objects.filter(genre='2')
    music_streams = Stream.objects.filter(genre='3')
    blog_streams = Stream.objects.filter(genre='4')
    top_rated_users = UserFollower.objects.annotate(num_followers=Count('follows')).order_by('-num_followers')[:5]

    context = {
        'education_streams': education_streams,
        'gaming_streams': gaming_streams,
        'music_streams': music_streams,
        'blog_streams': blog_streams,
        'top_rated_users': top_rated_users,
    }

    return render(request, 'explore.html', context)
