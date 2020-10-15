from django.urls import path
from . import views

urlpatterns = [
	path('likes/<int:hueca>', views.likes, name="likes-hueca-list"),
	path('like/<int:hueca>/<int:user>', views.like, name="like-hueca-user"),
	path('like', views.post_like, name="like-post"),
	path('likes/user/<int:user>', views.likes_user, name="hueca-user-like-list"),

	path('ratings/<int:hueca>', views.ratings, name="ratings-hueca-list"),
	path('rating/<int:hueca>/<int:user>', views.rating, name="rating-hueca-user"),
	path('rating', views.post_rating, name="rating-post"),

	path('comments/<int:hueca>', views.comments, name="comments-hueca-list"),
	path('comment/<int:pk>', views.comment, name="comment-hueca-user"),
	path('comment', views.post_comment, name="comment-post"),
]
