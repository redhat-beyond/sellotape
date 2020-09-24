from django.test import TestCase
from django.utils import timezone

from django.template.loader import render_to_string

class UserTemplateTests(TestCase):
    def test_shows_profile_name(self):
        """It should display the first and last name of the user."""
        user = {
            'username': 'darth-vader',
            'first_name': 'Darth',
            'last_name': 'Vader'
        }

        html = render_to_string('sellotape/user.html', { 'profile': user })
        self.assertTrue('<h2>Darth Vader</h2>' in html)

    def test_shows_no_streams_message(self):
        """It should display an appropriate message when no streams are available."""
        user = { 'username': 'darth-vader' }
        html = render_to_string('sellotape/user.html', { 'profile': user })
        self.assertTrue('<h3>No streams are available.</h3>' in html)

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
            'link': 'linktomystream.com'
        }

        context = {
            'profile': user,
            'live_stream': live_stream
        }

        html = render_to_string('sellotape/user.html', context)
        self.assertTrue('Darth is live now at' in html)
        self.assertTrue('linktomystream.com</a>' in html)

    def test_shows_future_streams(self):
        """It should display future and previous streams."""
        date = timezone.datetime(2025, 1, 1)

        future_streams = [
            { 'title': 'Stream 1', 'airs_on': date },
            { 'title': 'Stream 2', 'airs_on': date }
        ]

        context = { 'future_streams': future_streams }
        html = render_to_string('sellotape/user.html', context)

        self.assertTrue('<h3>Future Streams</h3>' in html)
        self.assertTrue('<h4>Stream 1</h4>' in html)
        self.assertTrue('<h4>Stream 2</h4>' in html)
        self.assertTrue('Airs on Jan. 1, 2025' in html)

    def test_shows_previous_streams(self):
        """It should display future and previous streams."""
        date = timezone.datetime(2018, 1, 1)

        future_streams = [
            { 'title': 'Stream 1', 'airs_on': date },
            { 'title': 'Stream 2', 'airs_on': date }
        ]

        context = { 'future_streams': future_streams }
        html = render_to_string('sellotape/user.html', context)

        self.assertTrue('<h3>Future Streams</h3>' in html)
        self.assertTrue('<h4>Stream 1</h4>' in html)
        self.assertTrue('<h4>Stream 2</h4>' in html)
        self.assertTrue('Airs on Jan. 1, 2018' in html)
