from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


VERSION = "v1"

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    # path(settings.ADMIN_URL, admin.site.urls),
    # Django-rest-auth urls for authentication and registration
    path(f"api/{VERSION}/auth/", include("dj_rest_auth.urls")),
    path(f"api/{VERSION}/auth/registration", include("dj_rest_auth.registration.urls")),
    # User management
    path(f"api/{VERSION}/users/", include("the_so_so_blog.users.urls", namespace="users")),
    path(f"api/{VERSION}/blog/", include("the_so_so_blog.blog_posts.urls", namespace="blog")),
    # Index view, built with reactjs
    # ALWAYS PLACE THESE AT THE END OF YOUR URL CONFIG
    path("blog/", TemplateView.as_view(template_name="base.html"), name="index"),
    re_path(r"blog/.*", TemplateView.as_view(template_name="base.html"), name="sub_index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # DRF auth token
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
