from django.urls import path
from . import views

urlpatterns = [
    path("<str:tag>/",views.hashtag_posts_view, name="hastag_posts"),
    path("suggest/",views.hashtag_suggestions, name="hastag_suggestions"),
]
