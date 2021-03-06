from django.urls import path
from .views import SnacksList, SnacksDetail


urlpatterns = [
    path('', SnacksList.as_view(), name='snack-list'),
    path('<int:pk>', SnacksDetail.as_view(), name='snack-detail')
]
