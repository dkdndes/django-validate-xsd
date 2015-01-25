from django.contrib import admin
from forms import MyWebservicedocAdminForm

"""
Customize Admin
"""
class WebservicedocAdmin(admin.ModelAdmin):
    form = MyWebservicedocAdminForm
    save_as = True
    # lots more unrelated custom admin such as field definitions
