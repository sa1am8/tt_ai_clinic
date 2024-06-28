import django_filters
from .models import Team, Person

class TeamFilter(django_filters.FilterSet):
    class Meta:
        model = Team
        fields = {
            'name': ['exact', 'icontains'],
        }

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
        }
