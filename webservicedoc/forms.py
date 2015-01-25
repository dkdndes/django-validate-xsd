from django.contrib import admin
from django import forms

# Models
from webservicedoc.models import Webservicedoc

# Utilities
import pyxb # For catching the exceptions
import dwml # The Python-version WADL XSD validator


class WebservicedocAdminForm(forms.ModelForm):
    """
    Custom Validation For DWML
    """
    class Meta:
        model = Webservicedoc

    def clean_dwml_raw(self):
    # Custom WADL validation
        dwml_raw = self.cleaned_data['dwml_raw']
        try:
            this_dwml = dwml.CreateFromDocument(dwml_raw)
        except pyxb.UnrecognizedContentError as e:
            raise forms.ValidationError("Error validating response: %s" % e.details())
	except Exception, e:
	    raise forms.ValidationError("Unknown validation error: %s" % e)
        return dwml_raw
