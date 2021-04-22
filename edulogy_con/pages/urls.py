from django.urls import path
from pages.views import ContactView, IndexView

urlpatterns = [
    path('', IndexView, name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
]
