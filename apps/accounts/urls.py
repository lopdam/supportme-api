from django.urls import path
from . import views

urlpatterns = [
	path('users', views.users, name="users-list"),
	path('user/<int:pk>', views.user, name="user-info"),
	path('login', views.login, name="login-user"),
	path('signup', views.createUser, name="registrer-user"),
	path('logout/<int:pk>', views.logout, name="cerrar-session-user"),
	path('delete/<int:pk>', views.deleteAccount, name="delete-account-user"),
	path('update/<int:pk>', views.updateUser, name="update-account-user"),

	path('active/<int:user>', views.isActiveToken, name="active-user-token"),

]
