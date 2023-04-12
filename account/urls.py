from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
import django
urlpatterns = [
    path('', views.index , name="account"),
    path('profile/<int:id>', views.profile , name="profile"),
    path('login', views.login_view , name="login"),
    path('logout', views.logout_view , name="logout"),
    path('register', views.register , name="register"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)