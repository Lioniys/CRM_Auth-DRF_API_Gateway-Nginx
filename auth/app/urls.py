from django.urls import path
from .views import Test
urlpatterns = [
    path("count/", Test.as_view())
]
