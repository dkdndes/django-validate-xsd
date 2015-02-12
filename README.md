Validate XSD - XML Schema
===

Example for the usage of PyXB and Django to generate a generic "wadl.py" file for the validation of related "wadl.xml" documents via django. In this example I use the po.xsd file as a basis for the generated "wadl.py" file. The "po.xml" file will be checked via our webservice admin interface.

Install
-------
* git clone https://github.com/dkdndes/validatexsd.git
* cd validatexsd
* virtualenv env
* source env/bin/activate
* pip install -f requirements.txt

Run
---
* python manage.py check 
* python manage.py migrate 
* python manage.py makemigrations
* python manage.py runserver 0:8000

You can regenerate a alternative "wadl.py" fiel within the "webservicedocs" directory with the following command:

* pyxbgen -u po.xsd -m wadl

Now you are able to take "po.xml" and add it the contents in the admin entry. check out what happens if you change the tags, etc. 

You find more xsd/xml examples in the [pyxb source code on githut](https://github.com/pabigot/pyxb/)

Have fun!

Remarks: The source code follows initialy ideas set out in a blog by [Robert Newman](http://www.robertnewmanconsulting.com/blog/2013/apr/03/using-pyxb-django-validate-xml-docs-xsd-schemas/)

If you are new to the subject, I suggest reading the blog: [Thomas Nurkiewic](http://www.nurkiewicz.com/2012/01/gentle-introduction-to-wadl-in-java.html)

Copyright (C) 2015 Peter Rosemann

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
