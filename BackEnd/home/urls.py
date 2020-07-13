from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView #for registration and login logout forms and use LoginView.as_view(),LogoutView.as_view()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexView,name='home'),
    path("dashboard/",views.dashboardView,name='dasdhboard'), #views.dashboardView points to the dashboardView function in views 
    path('register/',views.registerView,name='register_url'), #views.registerView points to the registerView function in views
    path('login/',LoginView.as_view(),name='login_url'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('/profile/',views.profile,name='profile'),
    
   # path('/qualification/',views.qualification,name='qualification'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)