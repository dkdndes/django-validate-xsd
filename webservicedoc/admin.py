from django.contrib import admin
from forms import WebservicedocAdminForm
from models import Webservicedoc


class WebservicedocAdmin(admin.ModelAdmin):
    """Customize WebservicedocAdmin
    """
    form = WebservicedocAdminForm
    fields = ('wadl_raw',)
    save_as = True


admin.site.register(Webservicedoc, WebservicedocAdmin)
