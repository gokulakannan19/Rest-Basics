from django.urls import path
from rest_framework.generics import GenericAPIView
from .import views

urlpatterns = [
    # path('article/', views.article_list, name="articles"),
    path('article/', views.ArticleApiView.as_view(), name="articles"),
    # path('article-detail/<str:pk>/', views.article_detail, name="article")
    path('article-detail/<str:pk>/',
         views.ArticleDetails.as_view(), name="article"),
    path('generic/article/<str:pk>/', views.GenericApiView.as_view(),
         name="generic-api-view"),
]
