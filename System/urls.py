from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),

]
