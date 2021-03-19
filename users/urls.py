from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/login/', views.loginUser, name='login'),
    path('auth/logout/', views.logoutUser, name='logout'),
    path('auth/signup/', views.signupUser, name='signup'),
    path('auth/register/', views.registerOutlet, name='register'),
    path('auth/forgot/', views.forgot, name='forgot'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
