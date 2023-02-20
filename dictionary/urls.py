from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from . import views
from django.urls import path
from django.urls import include
from django.utils.translation import gettext_lazy as _
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = 'dictionary'

imi_patterns = [
    path('', views.imi),
    path('imi_kekka', views.imi_kekka),
    path('about/', views.about)
]

bunsho_patterns = [
    path('', views.bunsho),
    path('bunsho_kekka', views.bunsho_kekka),
    path('about/', views.about)
]

tango_patterns = [
    path('', views.tango_sentaku),
    path('tango_eigo_rosiago/', views.tango_eigo_rosiago),
    path('tango_nihongo_eigo/', views.tango_nihongo_eigo),
    path('tango_rosiago_nihongo/', views.tango_rosiago_nihongo),
    path('tango_sonota/', views.tango_sonota),
    path('tango_sonota/tango_kekka_sonota', views.tango_kekka_sonota),
    path('tango_eigo_rosiago/tango_kekka_eigo_rosiago', views.tango_kekka_eigo_rosiago),
    path('tango_nihongo_eigo/tango_kekka_nihongo_eigo', views.tango_kekka_nihongo_eigo),
    path('tango_rosiago_nihongo/tango_kekka_rosiago_nihongo', views.tango_kekka_rosiago_nihongo),
    path('tango_eigo_rosiago/about/', views.about),
    path('tango_nihongo_eigo/about/', views.about),
    path('tango_rosiago_nihongo/about/', views.about),
    path('tango_sonota/about/', views.about),
    path('tango_sonota/tango_kekka_sonota/about/', views.about),
    path('tango_eigo_rosiago/tango_kekka_eigo_rosiago/about/', views.about),
    path('tango_nihongo_eigo/tango_kekka_nihongo_eigo/about/', views.about),
    path('tango_rosiago_nihongo/tango_kekka_rosiago_nihongo/about/', views.about),
    path('about/', views.about)
]

urlpatterns = [
    path('', views.menuView, name='menu'),
    path('about/', views.about),
    path('imi/', include(imi_patterns)),
    path('bunsho/', include(bunsho_patterns)),
    path('tango_sentaku/', include(tango_patterns)),
]