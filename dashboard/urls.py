from django.urls import path, include

from dashboard.views import sign_in, sign_out, index

urlpatterns = [
    path("", sign_in, name="sign-in"),
    path('index/', index, name="home"),
    path("logout/", sign_out, name="sign-out"),
    path("logout/<conf>/", sign_out, name="sign-out-conf"),


    path('ctg/', include('dashboard.category.urls')),
    path('teach/', include('dashboard.teacher.urls')),
    path('aboutc/', include('dashboard.aboutc.urls')),
    path('aboutv/', include('dashboard.aboutv.urls')),
    path('onlinew/', include('dashboard.onlinew.urls')),
    path('why/', include('dashboard.why.urls')),
    path('part/', include('dashboard.part.urls')),
    path('sifat/', include('dashboard.sifat.urls')),
    path('rate/', include('dashboard.rate.urls')),


]
