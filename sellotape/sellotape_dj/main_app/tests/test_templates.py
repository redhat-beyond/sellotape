from django.test import TestCase
from django.utils import timezone

from django.template.loader import render_to_string


class UserTemplateTests(TestCase):
    def test_shows_profile_name(self):
        """It should display the first and last name of the user."""
        profile = {
            'user': {
                'username': 'darth-vader',
                'first_name': 'Darth',
                'last_name': 'Vader'
            }
        }

        html = render_to_string('user.html', {'profile': profile})
        self.assertTrue("Darth Vader" in html)

    def test_shows_no_streams_message(self):
        """It should display an appropriate message when no streams are available."""
        user = {'username': 'darth-vader'}
        profile = {'user': user}
        html = render_to_string('user.html', {'profile': profile})
        self.assertTrue('No Live Stream' in html)
        self.assertTrue('No past streams!' in html)
        self.assertTrue('No future streams scheduled yet!' in html)

    def test_shows_live_stream(self):
        """It should display the live link to a stream happening at the moment."""
        user = {
            'username': 'darth-vader',
            'first_name': 'Darth',
            'last_name': 'Vader'
        }

        live_stream = {
            'author': user,
            'title': 'Live Stream',
            'link': 'linktomystream.com',
            'pk': 1,
        }

        context = {
            'profile': {
                'user': user,
            },
            'live_stream': live_stream
        }

        html = render_to_string('user.html', context)
        self.assertTrue('<h5 class="mb-1">Live Stream</h5>' in html)
        self.assertTrue('<a href="linktomystream.com"' in html)

    def test_shows_future_streams(self):
        """It should display future and previous streams."""
        date = timezone.datetime(2025, 1, 1)

        future_streams = [
            {'title': 'Stream 1', 'pk': 1, 'airs_on': date},
            {'title': 'Stream 2', 'pk': 2, 'airs_on': date}
        ]

        context = {'future_streams': future_streams}
        html = render_to_string('user.html', context)

        self.assertTrue('<h1 style="display-4">Future streams</h1>' in html)
        self.assertTrue('<h5 class="mb-1">Stream 1</h5>' in html)
        self.assertTrue('<h5 class="mb-1">Stream 2</h5>' in html)
        self.assertTrue('<small>Airs on Jan. 1, 2025</small>' in html)

    def test_shows_previous_streams(self):
        """It should display future and previous streams."""
        date = timezone.datetime(2018, 1, 1)

        previous_streams = [
            {'title': 'Stream 1', 'pk': 1, airs_on': date},
            {'title': 'Stream 2', 'pk': 2, 'airs_on': date}
        ]

        context = {'previous_streams': previous_streams}
        html = render_to_string('user.html', context)

        self.assertTrue('<h1 style="display-4">Past streams</h1>' in html)
        self.assertTrue('<h5 class="mb-1">Stream 1</h5>' in html)
        self.assertTrue('<h5 class="mb-1">Stream 2</h5>' in html)
        self.assertTrue('<small>Aired on Jan. 1, 2018</small>' in html)
