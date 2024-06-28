from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, Person

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list-create')
        data = {'name': 'Team A'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_teams(self):
        url = reverse('team-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PersonTests(APITestCase):
    def test_create_person(self):
        team = Team.objects.create(name='Team A')
        url = reverse('person-list-create')
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'team': team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_persons(self):
        url = reverse('person-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
