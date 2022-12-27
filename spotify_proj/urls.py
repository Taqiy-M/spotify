
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from spotapp.views import ArtistViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




r = DefaultRouter()
r.register('artist', ArtistViewSet, basename='artistlar')


urlpatterns = [
   path('admin/', admin.site.urls),
   path('get-token/', TokenObtainPairView.as_view(), name='token_obtain'),
   path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('update-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(r.urls)),
    # path('ss/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('rr/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
