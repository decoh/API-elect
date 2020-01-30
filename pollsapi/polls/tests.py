from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from pollsapi import polls
#from polls import apiviews


class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.uri = '/polls/'
        self.token.save()

    @staticmethod
    def setup_user():
        user = get_user_model()
        return user.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list2(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        self.client.login(username='test', password='test')
        params = {
            "question": "How are you?",
            "create_by": "1"
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201, 'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

