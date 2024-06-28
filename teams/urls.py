from django.urls import path
from .views import TeamListCreate, TeamDetail, PersonListCreate, PersonDetail

urlpatterns = [
    path('teams/', TeamListCreate.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetail.as_view(), name='team-detail'),
    path('persons/', PersonListCreate.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
]
