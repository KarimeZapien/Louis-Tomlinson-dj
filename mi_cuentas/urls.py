from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login 

urlpatterns = [
    path('', login, name='home'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Redirección después del logout
]
