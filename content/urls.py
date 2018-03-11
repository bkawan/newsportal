from django.urls import path

from . import views

urlpatterns = [
    # path('', views.all_posts, name='index'),
    path('', views.HomePageView.as_view(), name='index'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
]
