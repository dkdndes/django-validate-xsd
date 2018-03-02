Validate XSD - XML Schema
===

Example for the usage of PyXB and Django.

XSD to WADL
-----------

We use PyXB to generate a generic "wadl.py" file for the XML Schema validation of related XML file "wadl.xml" documents via django. 

Basis for the validation is the XML Schema described in "wadl.xsd". It functions as our basis for the generated "wadl.py" file. And then "po.xml" files can be entered and checked in our webservice admin interface.

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

* pyxbgen -u wadl.xsd -m wadl

Now test it with a valid XML file "wadl.xml" and start changing tags, etc. 

You find xsd/xml examples in the [pyxb source code on githut](https://github.com/pabigot/pyxb/)

Have fun!

Remarks: The source code follows initialy ideas set out in a blog by Robert Newman [now offline](http://www.robertnewmanconsulting.com/blog/2013/apr/03/using-pyxb-django-validate-xml-docs-xsd-schemas/)

If you are new to the subject, I suggest reading the blog: [Thomas Nurkiewic, 2012](http://www.nurkiewicz.com/2012/01/gentle-introduction-to-wadl-in-java.html)

Copyright (C) 2015 Peter Rosemann

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
