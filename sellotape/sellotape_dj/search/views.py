from django.shortcuts import render
from main_app.models import Profile, Stream

from itertools import chain


# Create your views here.
def uniq_chain(*args, **kwargs):
    seen = set()
    for x in chain(*args, **kwargs):
        if x in seen:
            continue
        seen.add(x)
        yield x


def search(request):
    # Getting the query string for the searching.
    query = request.GET.get('search', None)

    # Searching through the Streams, looking for streams with title or description containing the query.
    stream_results_title = Stream.objects.filter(title__icontains=query)
    stream_results_description = Stream.objects.filter(description__icontains=query)

    # Chaining toghether the stream results to combine both queries
    stream_results = uniq_chain(
        stream_results_title,
        stream_results_description,
        )

    if stream_results is not None:
        stream_results = sorted(stream_results, key=lambda instance: instance.pk, reverse=True)

    # Searching through the Profile, looking for profiles with username, first name and last name containing the query.
    profile_results_username = Profile.objects.filter(user__username__icontains=query)
    profile_results_firstname = Profile.objects.filter(user__first_name__icontains=query)
    profile_results_lastname = Profile.objects.filter(user__last_name__icontains=query)

    # Chaining toghether the profile results to combine both queries.
    profile_results = uniq_chain(
        profile_results_username,
        profile_results_firstname,
        profile_results_lastname,
        )

    if profile_results is not None:
        profile_results = sorted(profile_results, key=lambda instance: instance.pk, reverse=True)

    # Creating the context relevant for rendering the HTML results file.
    context = {
        'query': query,
        'stream_results': stream_results,
        'profile_results': profile_results,
    }
    return render(request, 'sellotape/search.html', context)
