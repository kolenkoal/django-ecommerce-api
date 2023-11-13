import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


user_urls = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]

swagger = [
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += swagger
urlpatterns += user_urls

# urlpatterns += user_urls

if settings.DEBUG:
    urlpatterns += [
        path("__debug__", include(debug_toolbar.urls)),
    ]
