from django.shortcuts import render
from main_app.models import Profile, Stream

from itertools import chain


# Create your views here.

def search(request):
    # Getting the query string for the searching.
    query = request.GET.get('search', None)

    # Searching through the Streams, looking for streams with title or description containing the query.
    stream_results_title = Stream.objects.filter(title__icontains=query)
    stream_results_description = Stream.objects.filter(description__icontains=query)

    # Chaining toghether the stream results to combine both queries
    stream_results = chain(
        stream_results_title,
        stream_results_description,
        )
    # Calculating sum of stream results
    length_streams = len(stream_results_title)+len(stream_results_description)

    # Searching through the Profile, looking for profiles with username, first name and last name containing the query.
    profile_results_username = Profile.objects.filter(user__username__icontains=query)
    profile_results_firstname = Profile.objects.filter(user__first_name__icontains=query)
    profile_results_lastname = Profile.objects.filter(user__last_name__icontains=query)

    # Chaining toghether the profile results to combine both queries.
    profile_results = chain(
        profile_results_username,
        profile_results_firstname,
        profile_results_lastname,
        )
    # Calculating sum of profile results.
    length_profiles = len(profile_results_username) + len(profile_results_firstname) + len(profile_results_lastname)

    # combine both streams and profiles querysets chains.
    queryset_chain = chain(
        stream_results,
        profile_results
        )
    
    # Checking if there were found results, if we did find, sort them.
    if queryset_chain is not None:
        if stream_results is not None or profile_results is not None:
            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)

    # Sums up both results of streams and profiles.
    count = length_streams + length_profiles
    
    # Creating the context relevant for rendering the HTML results file.
    context = {
        'qs': qs,
        'query': query,
        'count': count,
    }
    return render(request, 'sellotape/search.html', context)
