from django.urls import path
from .views import PostSetView
from rest_framework.routers import SimpleRouter


from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView
)

app_name="api"
urlpatterns = [
  # path("",PostListCreateAPIView.as_view(),name="list"),
  # path("<int:pk>/",PostDetailView.as_view(),name="detail_view"),

  path("token/",TokenObtainPairView.as_view(),name="token_obtain_pair"),
  path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
  
]
router = SimpleRouter()
router.register("",PostSetView,basename='post')
urlpatterns += router.urls