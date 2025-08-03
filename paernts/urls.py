from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PaerntList, PaerntDetail

app_name = 'paernt'


urlpatterns = [

    path('paernt/', PaerntList.as_view(), name='paernt_list'),
    path('paernt/<int:pk>/', PaerntDetail.as_view(), name='paernt_detail'),
]
