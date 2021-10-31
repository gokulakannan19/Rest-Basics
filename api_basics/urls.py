from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views


router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename="article-view-set")


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<str:pk>/', include(router.urls)),
    # path('article/', views.article_list, name="articles"),
    path('article/', views.ArticleApiView.as_view(), name="articles"),
    # path('article-detail/<str:pk>/', views.article_detail, name="article")
    path('article-detail/<str:pk>/',
         views.ArticleDetails.as_view(), name="article"),
    path('generic/article/<str:pk>/', views.GenericApiView.as_view(),
         name="generic-api-view"),
]
