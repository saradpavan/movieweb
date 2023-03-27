
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings
from saradpavanapp.views import home
from saradpavanapp.views import login
from saradpavanapp.views import signup
from saradpavanapp.views import moviepage
from saradpavanapp.views import logout
from saradpavanapp.views import playvideo
from saradpavanapp.views import search
from contactapp.views import contact
from saradpavanapp.views import language
from saradpavanapp.views import dubbed



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("",home,name="homeget"),
    path("login/",login,name="login"),
    path("signup/",signup,name="signup"),
    path("moviepage/<int:id>",moviepage,name="moviepage"),
    path("playvideo/<int:id>",playvideo,name="playvideo"),
    path("logout/",logout,name="logout"),
    path("search/",search,name="search"),
    path("contact/",contact,name="contact"),
    path("language/",language,name="language"),
    path("dubbed/",dubbed,name="dubbed"),
]

    
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
