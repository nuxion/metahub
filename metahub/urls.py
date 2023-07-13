"""
URL configuration for metahub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.accounts.api import views as accounts_api
from apps.assets.api import views as assets_api
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = routers.DefaultRouter()
# router.register(r"users", accounts_api.UserViewSet)
# router.register(r"groups", accounts_api.GroupViewSet)
router.register(r"objects", assets_api.ObjectViewSet)
router.register(r"buckets", assets_api.BucketViewSet)


urlpatterns = [
    path("_/admin/", admin.site.urls),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
