"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import *
from vege.views import *

urlpatterns = [
    
    path('', home, name='home'),
    
    path('ecomerce/' , ecomerce, name='ecomerce'),
    
    path('ecomerce/product/' , product, name='product'),
    
    path('ecomerce/contactus/' , contactus, name='contactus'),
    
    path('ecomerce/aboutus/' , aboutus, name='aboutus'),
    
    # path('login-form/', login, name='login'),    
    # path('register/', register, name='register'),
    # path('contacts/' , contact, name='contact'),    
    # path('about/' , about, name='about'),
    

    
    # Create vege urls hear
    
    path('receipes/', receipes, name='receipes'), 
    path('add_receipes/' , add_receipes, name='add_receipes'), 
    
    path('delete_receipe/<id>/' , delete_receipe, name='delete_rece'),
    path('update_receipe/<id>/' , update_receipe, name='update_rece'), 


    path('user_login/',login_page, name='login'),
    path('user_register/',register_page, name='register'),
    path('/logout/', logout_page, name='logout' ),
    
    
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()

