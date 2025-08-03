from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PlayerList, PlayerDetail

app_name = 'players'


urlpatterns = [

    path('players/', PlayerList.as_view(), name='players_list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='players_detail'),
]
