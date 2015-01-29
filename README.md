validate xsd
===
Example for the usage of PyXB in Django to validate XML docs from XSD


Install
---

   virtualenv env
   source env/bin/activate
   pip install -f requirements.txt

Run
---
   python manage.py check
   python manage.py migrate
   python manage.py makemigrations

If you like to newly generate dwml.py, run in webservicedocs the following command:

   pyxbgen -u DWML.xsd -m dwml

Remarks: The source code follows initialy ideas set out in a blog by [Robert Newman](http://www.robertnewmanconsulting.com/blog/2013/apr/03/using-pyxb-django-validate-xml-docs-xsd-schemas/)

If you are new to the subject, I suggest reading the blog: [Thomas Nurkiewic](http://www.nurkiewicz.com/2012/01/gentle-introduction-to-wadl-in-java.html)

Copyright (C) 2015 Peter Rosemann

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
