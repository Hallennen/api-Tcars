from django.contrib import admin
from django.urls import path
from carrosAPI.views import CarsListView, CarDetailsView, BrandListView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('cars/', CarsListView.as_view(), name='list-cars-api'),
    path('cars/<int:pk>/', CarDetailsView.as_view(), name='detail-cars-api'),

    path('brand/', BrandListView.as_view(), name='list-brand-api')
]
