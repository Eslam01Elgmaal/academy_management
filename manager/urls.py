from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Manager_detail

app_name = 'managers'


urlpatterns = [

    path('<int:pk>/', Manager_detail.as_view(), name='manager_detail'),
]
