from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        'social-auth',
        include(
            'social_django.urls',
            namespace='social')),
    path(
        'reg/',
        userViews.register,
        name='reg'),
    path(
        'profile/',
        userViews.profile,
        name='profile'),
    path(
        '',
        authViews.LoginView.as_view(
            template_name='users/user.html'),
        name='user'),
    path(
        'list/',
        userViews.ShowNewsView.as_view(),
        name='list'),
    path(
        'list/<int:pk>/',
        userViews.NewsDetailView.as_view(),
        name='list-detail'),
    path(
        'exit/',
        authViews.LogoutView.as_view(
            template_name='users/exit.html'),
        name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
