from django.contrib import admin
from django import forms

# Models
from webservicedoc.models import Webservicedoc

# Utilities
import pyxb # For catching the exceptions
import wadl # The Python-version WADL XSD validator


class MyWebservicedocAdminForm(forms.ModelForm):
    """
    Custom Validation For WADLs
    """
    class Meta:
        model = Webservicedoc
        def clean_wadl_raw(self):
        # Custom WADL validation
            wadl_raw = self.cleaned_data['wadl_raw']
            try:
	        this_wadl = wadl.CreateFromDocument(wadl_raw)
	    except pyxb.UnrecognizedContentError as e:
	        raise forms.ValidationError("Error validating response: %s" % e.details())
	    except Exception, e:
	        raise forms.ValidationError("Unknown validation error: %s" % e)
            return wadl_raw
