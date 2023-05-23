from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("records/", include("records.urls")),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("records_list")),
        name="home",
    ),
]
