from django.db import router
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "blog_api"

# router = DefaultRouter()
# router.register("", PostList, basename="post")
# urlpatterns = router.urls

urlpatterns = [
    path("posts/", PostDetail.as_view(), name="detailcreate"),
    path("search/", PostSearch.as_view(), name="postsearch"),
    path("", PostList.as_view(), name="listcreate"),
]
