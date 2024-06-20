from django.urls import path
from .views import HomePageView, sub_county_dataset, incidences_dataset

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('sub_county_data/', sub_county_dataset, name='sub_county'),
    path('incidence_data/', incidences_dataset, name='incidence'),
]