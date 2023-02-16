from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import testpdf

urlpatterns = [
    path('', views.home, name='home'),
    path('index/login', views.my_login, name='login'),
    path('index/logout', views.logoutUser, name='logout'),
    path('index/register', views.registerPage, name='login'),
    path('index/', views.index, name='index'),
    path('index/about', views.about, name='about'),
    path('index/symptoms', views.symptoms, name='symptoms'),
    path('index/contact', views.contact, name='contact'),
    path('index/profile', views.profile, name='profile'),
    path('index/hospital', views.hospital, name='hospital'),
    path('index/search', views.search, name='search'),
    path('index/editprofile', views.editprofile, name='editprofile'),
    path('index/configuration', views.afterlogin, name='configuration'),
    path('index/download', testpdf, name='download_pdf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)