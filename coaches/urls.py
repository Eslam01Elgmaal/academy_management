from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CoachesList, CoachesDetail

app_name = 'coaches'


urlpatterns = [

    path('coaches/', CoachesList.as_view(), name='coaches_list'),
    path('coaches/<int:pk>/', CoachesDetail.as_view(), name='coaches_detail'),
]
