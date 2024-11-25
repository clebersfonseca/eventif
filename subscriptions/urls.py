from django.urls import path
from subscriptions.views import subscribe, detail

app_name = 'subscriptions'

urlpatterns = [
    path('', subscribe, name='new'),
    path('<int:pk>/', detail, name='detail'),
]
