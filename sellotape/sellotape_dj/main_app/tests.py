from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Stream
from django.contrib.auth.models import User

from django.template.loader import render_to_string


class UserTemplateTests(TestCase):
    def test_shows_profile_name(self):
        """It should display the first and last name of the user."""
        user = {
            'username': 'darth-vader',
            'first_name': 'Darth',
            'last_name': 'Vader'
        }

        html = render_to_string('sellotape/user.html', {'profile': user})
        self.assertTrue('<h2>Darth Vader</h2>' in html)

    def test_shows_no_streams_message(self):
        """It should display an appropriate message when no streams are available."""
        user = {'username': 'darth-vader'}
        html = render_to_string('sellotape/user.html', {'profile': user})
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
            {'title': 'Stream 1', 'airs_on': date},
            {'title': 'Stream 2', 'airs_on': date}
        ]

        context = {'future_streams': future_streams}
        html = render_to_string('sellotape/user.html', context)

        self.assertTrue('<h3>Future Streams</h3>' in html)
        self.assertTrue('<h4>Stream 1</h4>' in html)
        self.assertTrue('<h4>Stream 2</h4>' in html)
        self.assertTrue('Airs on Jan. 1, 2025' in html)

    def test_shows_previous_streams(self):
        """It should display future and previous streams."""
        date = timezone.datetime(2018, 1, 1)

        future_streams = [
            {'title': 'Stream 1', 'airs_on': date},
            {'title': 'Stream 2', 'airs_on': date}
        ]

        context = {'future_streams': future_streams}
        html = render_to_string('sellotape/user.html', context)

        self.assertTrue('<h3>Future Streams</h3>' in html)
        self.assertTrue('<h4>Stream 1</h4>' in html)
        self.assertTrue('<h4>Stream 2</h4>' in html)
        self.assertTrue('Airs on Jan. 1, 2018' in html)

class UserViewTests(TestCase):
    def test_user_does_not_exist(self):
        """
        If user does not exist, it returns a 404.
        """
        url = reverse('main_app:user', args=('non-exist',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_no_streams(self):
        """
        If no streams are available, an appropriate message is displayed.
        """
        username = 'darth-vader'
        create_user(username)

        url = reverse('main_app:user', args=(username,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No streams are available.")
        self.assertQuerysetEqual(response.context['future_streams'], [])
        self.assertQuerysetEqual(response.context['previous_streams'], [])
        self.assertTemplateUsed(response, 'sellotape/user.html')

    def test_finds_live_stream(self):
        """
        If there is a live stream happening at the moment,
        it should be passed to the response context.
        """
        username = 'darth-vader'
        user = create_user(username)
        
        now = timezone.now()
        streams = [
            {
                'author': user,
                'airs_on': now.replace(hour=(now.hour - 1)),
                'ends_on': now.replace(hour=(now.hour + 1)),
                'title': 'Live Stream',
                'added_on': now
            },
        ]
        create_streams(streams)

        url = reverse('main_app:user', args=(username,))
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['live_stream'])
        self.assertEqual(response.context['live_stream'].title, 'Live Stream')

    def test_splits_streams(self):
        """
        The view should split future and previous streams based on the current time
        and the streams data.
        """
        username = 'darth-vader'
        user = create_user(username)

        now = timezone.now()
        streams = [
            {
                'author': user,
                'airs_on': now.replace(year=(now.year + 1)),
                'ends_on': None,
                'title': 'Future Stream',
                'added_on': now
            },
            {
                'author': user,
                'airs_on': now.replace(year=(now.year - 1)),
                'ends_on': now.replace(hour=now.hour),
                'title': 'Previous Stream',
                'added_on': now
              }

        ]
        create_streams(streams)

        url = reverse('main_app:user', args=(username,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        future_streams = response.context['future_streams']
        previous_streams = response.context['previous_streams']
        
        self.assertTrue(len(future_streams))
        self.assertTrue(len(previous_streams))
        self.assertEqual(future_streams[0].title, 'Future Stream')
        self.assertEqual(previous_streams[0].title, 'Previous Stream')
