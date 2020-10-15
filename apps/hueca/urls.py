from django.urls import path
from . import views

urlpatterns = [
	path('huecas', views.huecas, name="huecas-list"),
	path('hueca/<int:pk>', views.hueca, name="hueca-single"),
	path('hueca', views.post_hueca, name="hueca-post"),
	
	path('huecas/<int:user>', views.huecas_user, name="user-huecas-list"),

    path('huecas/search/<str:search>',
         views.huecas_search, name="huecas-search-list"),
	path('huecas/cities/<int:city>', views.huecas_city, name="huecas-city-list"),
	path('huecas/categories/<int:category>',
	     views.huecas_category, name="huecas-category-list"),

	path('images/<int:hueca>', views.images, name="image-hueca-list"),
	path('image/<int:pk>', views.image, name="image-hueca"),
	path('image', views.post_image, name="image-post"),

    path('menus/<int:hueca>', views.menus, name="menu-hueca-list"),
	path('menu/<int:pk>', views.menu, name="menu-hueca"),
	path('menu', views.post_menu, name="menu-post"),

	path('location/<str:latitude>/<str:longitude>/<str:km>', views.huecas_location, name="huecas-near-location-list"),
]
