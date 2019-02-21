from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from userprofiles.views import DashboardView

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('', include('scand.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('comment/', include('comment.urls')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
