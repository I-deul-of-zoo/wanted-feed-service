from django.urls import path
from posts import views

app_name = "posts"
# base_url: v1/posts/

urlpatterns =[
    path("", views.SearchPostsList.as_view()),
    path('<int:pk>/', views.PostsDetail.as_view()),

    path('statistics/', views.PostsStatisicsDetailView.as_view()),
    path('<int:pk>/share/', views.SharePosts.as_view()),
    path('<int:pk>/like/', views.LikeView.as_view()),

]
