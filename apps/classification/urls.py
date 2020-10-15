from django.urls import path
from . import views

urlpatterns = [
	path('cities', views.cities, name="cities-list"),
	path('categories', views.categories, name="categories-list"),
    path('city/<int:pk>', views.city, name="city-single"),
    path('category/<int:pk>', views.category, name="category-single"),
]
