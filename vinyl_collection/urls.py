from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from records.views import SignUpView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("records/", include("records.urls")),
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("records_list")),
        name="home",
    ),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
