from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('gtran/', include('gtranslate.urls')),
    path('gtran/', include('gtranslate.urls_auth')),
]

urlpatterns += i18n_patterns(
    path('', include('dictionary.urls', namespace='dictionary'))
)

handler500 = 'dictionary.views.error_500'