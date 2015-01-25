# ./dwml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-01-25 19:54:19.432034 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7d1f2157-a4c3-11e4-9968-6c4008b819d2')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 67, 12)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.circle = STD_ANON._CF_enumeration.addEnumeration(unicode_value='circle', tag='circle')
STD_ANON.rectangle = STD_ANON._CF_enumeration.addEnumeration(unicode_value='rectangle', tag='rectangle')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 87, 11)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.statute_miles = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='statute miles', tag='statute_miles')
STD_ANON_.kilometers = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='kilometers', tag='kilometers')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: datumType
class datumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'datumType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 128, 5)
    _Documentation = None
datumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=datumType, enum_prefix=None)
datumType.surface = datumType._CF_enumeration.addEnumeration(unicode_value='surface', tag='surface')
datumType.mean_sea_level = datumType._CF_enumeration.addEnumeration(unicode_value='mean sea level', tag='mean_sea_level')
datumType._InitializeFacetMap(datumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'datumType', datumType)

# Atomic simple type: height-unitsType
class height_unitsType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'height-unitsType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 135, 5)
    _Documentation = None
height_unitsType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=height_unitsType, enum_prefix=None)
height_unitsType.feet = height_unitsType._CF_enumeration.addEnumeration(unicode_value='feet', tag='feet')
height_unitsType.meters = height_unitsType._CF_enumeration.addEnumeration(unicode_value='meters', tag='meters')
height_unitsType._InitializeFacetMap(height_unitsType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'height-unitsType', height_unitsType)

# Atomic simple type: fieldType
class fieldType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fieldType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 33, 4)
    _Documentation = None
fieldType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fieldType, enum_prefix=None)
fieldType.meteorological = fieldType._CF_enumeration.addEnumeration(unicode_value='meteorological', tag='meteorological')
fieldType._InitializeFacetMap(fieldType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fieldType', fieldType)

# Atomic simple type: categoryType
class categoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'categoryType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 39, 4)
    _Documentation = None
categoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=categoryType, enum_prefix=None)
categoryType.analysis = categoryType._CF_enumeration.addEnumeration(unicode_value='analysis', tag='analysis')
categoryType.forecast = categoryType._CF_enumeration.addEnumeration(unicode_value='forecast', tag='forecast')
categoryType.analysis_and_forecast = categoryType._CF_enumeration.addEnumeration(unicode_value='analysis and forecast', tag='analysis_and_forecast')
categoryType.current_observations_and_forecast = categoryType._CF_enumeration.addEnumeration(unicode_value='current observations and forecast', tag='current_observations_and_forecast')
categoryType.observations = categoryType._CF_enumeration.addEnumeration(unicode_value='observations', tag='observations')
categoryType.guidance = categoryType._CF_enumeration.addEnumeration(unicode_value='guidance', tag='guidance')
categoryType._InitializeFacetMap(categoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'categoryType', categoryType)

# Atomic simple type: concise-nameType
class concise_nameType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'concise-nameType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 75, 4)
    _Documentation = None
concise_nameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=concise_nameType, enum_prefix=None)
concise_nameType.time_series = concise_nameType._CF_enumeration.addEnumeration(unicode_value='time-series', tag='time_series')
concise_nameType.glance = concise_nameType._CF_enumeration.addEnumeration(unicode_value='glance', tag='glance')
concise_nameType.tabular_digital = concise_nameType._CF_enumeration.addEnumeration(unicode_value='tabular-digital', tag='tabular_digital')
concise_nameType.digital_zone = concise_nameType._CF_enumeration.addEnumeration(unicode_value='digital-zone', tag='digital_zone')
concise_nameType.dwmlByDay = concise_nameType._CF_enumeration.addEnumeration(unicode_value='dwmlByDay', tag='dwmlByDay')
concise_nameType._InitializeFacetMap(concise_nameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'concise-nameType', concise_nameType)

# Atomic simple type: operational-modeType
class operational_modeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'operational-modeType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 85, 4)
    _Documentation = None
operational_modeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=operational_modeType, enum_prefix=None)
operational_modeType.official = operational_modeType._CF_enumeration.addEnumeration(unicode_value='official', tag='official')
operational_modeType.developmental = operational_modeType._CF_enumeration.addEnumeration(unicode_value='developmental', tag='developmental')
operational_modeType.experimental = operational_modeType._CF_enumeration.addEnumeration(unicode_value='experimental', tag='experimental')
operational_modeType.test = operational_modeType._CF_enumeration.addEnumeration(unicode_value='test', tag='test')
operational_modeType._InitializeFacetMap(operational_modeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'operational-modeType', operational_modeType)

# Atomic simple type: srsNameType
class srsNameType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'srsNameType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 94, 4)
    _Documentation = None
srsNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=srsNameType, enum_prefix=None)
srsNameType.WGS_1984 = srsNameType._CF_enumeration.addEnumeration(unicode_value='WGS 1984', tag='WGS_1984')
srsNameType._InitializeFacetMap(srsNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'srsNameType', srsNameType)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 32, 12)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.forecast = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='forecast', tag='forecast')
STD_ANON_2.current_observations = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='current observations', tag='current_observations')
STD_ANON_2.analysis = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='analysis', tag='analysis')
STD_ANON_2.guidance = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='guidance', tag='guidance')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 52, 24)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.maximum = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='maximum', tag='maximum')
STD_ANON_3.ekdmos_maximum = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ekdmos-maximum', tag='ekdmos_maximum')
STD_ANON_3.minimum = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='minimum', tag='minimum')
STD_ANON_3.ekdmos_minimum = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ekdmos-minimum', tag='ekdmos_minimum')
STD_ANON_3.hourly = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='hourly', tag='hourly')
STD_ANON_3.rtma_hourly = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='rtma-hourly', tag='rtma_hourly')
STD_ANON_3.ekdmos_hourly = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ekdmos-hourly', tag='ekdmos_hourly')
STD_ANON_3.dew_point = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='dew point', tag='dew_point')
STD_ANON_3.rtma_dew_point = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='rtma-dew point', tag='rtma_dew_point')
STD_ANON_3.ekdmos_dew_point = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ekdmos-dew point', tag='ekdmos_dew_point')
STD_ANON_3.heat_index = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='heat index', tag='heat_index')
STD_ANON_3.wind_chill = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='wind chill', tag='wind_chill')
STD_ANON_3.apparent = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='apparent', tag='apparent')
STD_ANON_3.ekdmos_apparent = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ekdmos-apparent', tag='ekdmos_apparent')
STD_ANON_3.n8_14_day_anomolies = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='8-14 day anomolies', tag='n8_14_day_anomolies')
STD_ANON_3.monthly_anomolies = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='monthly anomolies', tag='monthly_anomolies')
STD_ANON_3.seasonal_anomolies = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='seasonal anomolies', tag='seasonal_anomolies')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 75, 24)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.Fahrenheit = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Fahrenheit', tag='Fahrenheit')
STD_ANON_4.Celsius = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Celsius', tag='Celsius')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 115, 24)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.liquid = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='liquid', tag='liquid')
STD_ANON_5.rtma_liquid = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='rtma-liquid', tag='rtma_liquid')
STD_ANON_5.ekdmos_liquid = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='ekdmos-liquid', tag='ekdmos_liquid')
STD_ANON_5.snow = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='snow', tag='snow')
STD_ANON_5.ice = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='ice', tag='ice')
STD_ANON_5.n8_14_day_anomolies = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='8-14 day anomolies', tag='n8_14_day_anomolies')
STD_ANON_5.monthly_anomolies = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='monthly anomolies', tag='monthly_anomolies')
STD_ANON_5.seasonal_anomolies = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='seasonal anomolies', tag='seasonal_anomolies')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 129, 24)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.inches = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='inches', tag='inches')
STD_ANON_6.centimeters = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='centimeters', tag='centimeters')
STD_ANON_6.hundredths_of_inches = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='hundredths of inches', tag='hundredths_of_inches')
STD_ANON_6.hundredths_of_centimeters = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='hundredths of centimeters', tag='hundredths_of_centimeters')
STD_ANON_6.meters = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='meters', tag='meters')
STD_ANON_6.kilograms_per_meter_squared = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='kilograms per meter squared', tag='kilograms_per_meter_squared')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 160, 24)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.n12_hour = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='12 hour', tag='n12_hour')
STD_ANON_7.floating = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='floating', tag='floating')
STD_ANON_7.ekdmos_6_hour = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='ekdmos-6 hour', tag='ekdmos_6_hour')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 185, 28)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.No_Areas = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='No Areas', tag='No_Areas')
STD_ANON_8.Critical_Areas = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Critical Areas', tag='Critical_Areas')
STD_ANON_8.Extremely_Critical_Areas = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Extremely Critical Areas', tag='Extremely_Critical_Areas')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 195, 24)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.risk_from_wind_and_relative_humidity = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='risk from wind and relative humidity', tag='risk_from_wind_and_relative_humidity')
STD_ANON_9.risk_from_dry_thunderstorms = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='risk from dry thunderstorms', tag='risk_from_dry_thunderstorms')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 218, 38)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.No_Thunderstorms = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='No Thunderstorms', tag='No_Thunderstorms')
STD_ANON_10.General_Thunderstorms = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='General Thunderstorms', tag='General_Thunderstorms')
STD_ANON_10.Slight_Risk_of_Severe_Thunderstorms = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='Slight Risk of Severe Thunderstorms', tag='Slight_Risk_of_Severe_Thunderstorms')
STD_ANON_10.Moderate_Risk_of_Severe_Thunderstorms = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='Moderate Risk of Severe Thunderstorms', tag='Moderate_Risk_of_Severe_Thunderstorms')
STD_ANON_10.High_Risk_of_Severe_Thunderstorms = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='High Risk of Severe Thunderstorms', tag='High_Risk_of_Severe_Thunderstorms')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 250, 34)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.tornadoes = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='tornadoes', tag='tornadoes')
STD_ANON_11.hail = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='hail', tag='hail')
STD_ANON_11.damaging_thunderstorm_winds = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='damaging thunderstorm winds', tag='damaging_thunderstorm_winds')
STD_ANON_11.extreme_tornadoes = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='extreme tornadoes', tag='extreme_tornadoes')
STD_ANON_11.extreme_hail = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='extreme hail', tag='extreme_hail')
STD_ANON_11.extreme_thunderstorm_winds = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='extreme thunderstorm winds', tag='extreme_thunderstorm_winds')
STD_ANON_11.severe_thunderstorms = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='severe thunderstorms', tag='severe_thunderstorms')
STD_ANON_11.extreme_severe_thunderstorms = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='extreme severe thunderstorms', tag='extreme_severe_thunderstorms')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 308, 24)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.sustained = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='sustained', tag='sustained')
STD_ANON_12.rtma_sustained = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='rtma-sustained', tag='rtma_sustained')
STD_ANON_12.gust = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='gust', tag='gust')
STD_ANON_12.transport = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='transport', tag='transport')
STD_ANON_12.cumulative34 = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='cumulative34', tag='cumulative34')
STD_ANON_12.cumulative50 = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='cumulative50', tag='cumulative50')
STD_ANON_12.cumulative64 = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='cumulative64', tag='cumulative64')
STD_ANON_12.incremental34 = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='incremental34', tag='incremental34')
STD_ANON_12.incremental50 = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='incremental50', tag='incremental50')
STD_ANON_12.incremental64 = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='incremental64', tag='incremental64')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 324, 23)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.knots = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='knots', tag='knots')
STD_ANON_13.meterssecond = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='meters/second', tag='meterssecond')
STD_ANON_13.percent = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='percent', tag='percent')
STD_ANON_13.miles_per_hour = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='miles per hour', tag='miles_per_hour')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 362, 24)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.wind = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='wind', tag='wind')
STD_ANON_14.rtma_wind = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='rtma-wind', tag='rtma_wind')
STD_ANON_14.swell = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='swell', tag='swell')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 400, 24)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.total = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='total', tag='total')
STD_ANON_15.rtma_total = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='rtma-total', tag='rtma_total')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 432, 24)
    _Documentation = None
STD_ANON_16._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_16, enum_prefix=None)
STD_ANON_16.relative = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='relative', tag='relative')
STD_ANON_16.maximum_relative = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='maximum relative', tag='maximum_relative')
STD_ANON_16.minimum_relative = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='minimum relative', tag='minimum_relative')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 464, 64)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.statute_miles = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='statute miles', tag='statute_miles')
STD_ANON_17.kilometers = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='kilometers', tag='kilometers')
STD_ANON_17.meters = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='meters', tag='meters')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 478, 48)
    _Documentation = None
STD_ANON_18._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_18, enum_prefix=None)
STD_ANON_18.slight_chance = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='slight chance', tag='slight_chance')
STD_ANON_18.chance = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='chance', tag='chance')
STD_ANON_18.likely = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='likely', tag='likely')
STD_ANON_18.occasional = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='occasional', tag='occasional')
STD_ANON_18.definitely = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='definitely', tag='definitely')
STD_ANON_18.isolated = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='isolated', tag='isolated')
STD_ANON_18.scattered = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='scattered', tag='scattered')
STD_ANON_18.numerous = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='numerous', tag='numerous')
STD_ANON_18.patchy = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='patchy', tag='patchy')
STD_ANON_18.areas = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='areas', tag='areas')
STD_ANON_18.widespread = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='widespread', tag='widespread')
STD_ANON_18.periods_of = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='periods of', tag='periods_of')
STD_ANON_18.frequent = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='frequent', tag='frequent')
STD_ANON_18.intermittent = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='intermittent', tag='intermittent')
STD_ANON_18.none = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 499, 48)
    _Documentation = None
STD_ANON_19._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_19, enum_prefix=None)
STD_ANON_19.freezing_drizzle = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='freezing drizzle', tag='freezing_drizzle')
STD_ANON_19.freezing_rain = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='freezing rain', tag='freezing_rain')
STD_ANON_19.snow_showers = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='snow showers', tag='snow_showers')
STD_ANON_19.blowing_snow = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='blowing snow', tag='blowing_snow')
STD_ANON_19.blowing_dust = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='blowing dust', tag='blowing_dust')
STD_ANON_19.rain_showers = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='rain showers', tag='rain_showers')
STD_ANON_19.ice_pellets = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='ice pellets', tag='ice_pellets')
STD_ANON_19.frost = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='frost', tag='frost')
STD_ANON_19.rain = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='rain', tag='rain')
STD_ANON_19.hail = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='hail', tag='hail')
STD_ANON_19.snow = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='snow', tag='snow')
STD_ANON_19.thunderstorms = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='thunderstorms', tag='thunderstorms')
STD_ANON_19.drizzle = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='drizzle', tag='drizzle')
STD_ANON_19.fog = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='fog', tag='fog')
STD_ANON_19.haze = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='haze', tag='haze')
STD_ANON_19.smoke = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='smoke', tag='smoke')
STD_ANON_19.freezing_spray = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='freezing spray', tag='freezing_spray')
STD_ANON_19.ice_fog = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='ice fog', tag='ice_fog')
STD_ANON_19.freezing_fog = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='freezing fog', tag='freezing_fog')
STD_ANON_19.water_spouts = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='water spouts', tag='water_spouts')
STD_ANON_19.volcanic_ash = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='volcanic ash', tag='volcanic_ash')
STD_ANON_19.ice_crystals = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='ice crystals', tag='ice_crystals')
STD_ANON_19.blowing_sand = STD_ANON_19._CF_enumeration.addEnumeration(unicode_value='blowing sand', tag='blowing_sand')
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 528, 48)
    _Documentation = None
STD_ANON_20._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_20, enum_prefix=None)
STD_ANON_20.very_light = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='very light', tag='very_light')
STD_ANON_20.light = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='light', tag='light')
STD_ANON_20.moderate = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='moderate', tag='moderate')
STD_ANON_20.heavy = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='heavy', tag='heavy')
STD_ANON_20.none = STD_ANON_20._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 539, 48)
    _Documentation = None
STD_ANON_21._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_21, enum_prefix=None)
STD_ANON_21.and_ = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='and', tag='and_')
STD_ANON_21.or_ = STD_ANON_21._CF_enumeration.addEnumeration(unicode_value='or', tag='or_')
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 547, 52)
    _Documentation = None
STD_ANON_22._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_22._CF_pattern.addPattern(pattern='(\\p{L}* ?\\p{L}*)?(,\\p{L}+ ?\\p{L}*)*')
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 581, 24)
    _Documentation = None
STD_ANON_23._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_23, enum_prefix=None)
STD_ANON_23.forecast_NWS = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='forecast-NWS', tag='forecast_NWS')
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 607, 48)
    _Documentation = None
STD_ANON_24._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_24, enum_prefix=None)
STD_ANON_24.Ashfall = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Ashfall', tag='Ashfall')
STD_ANON_24.Air_Quality = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Air Quality', tag='Air_Quality')
STD_ANON_24.Air_Stagnation = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Air Stagnation', tag='Air_Stagnation')
STD_ANON_24.Blowing_Snow = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Blowing Snow', tag='Blowing_Snow')
STD_ANON_24.Brisk_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Brisk Wind', tag='Brisk_Wind')
STD_ANON_24.Blizzard = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Blizzard', tag='Blizzard')
STD_ANON_24.Coastal_Flood = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Coastal Flood', tag='Coastal_Flood')
STD_ANON_24.Dust_Storm = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Dust Storm', tag='Dust_Storm')
STD_ANON_24.Blowing_Dust = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Blowing Dust', tag='Blowing_Dust')
STD_ANON_24.Excessive_Cold = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Excessive Cold', tag='Excessive_Cold')
STD_ANON_24.Excessive_Heat = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Excessive Heat', tag='Excessive_Heat')
STD_ANON_24.Excessive_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Excessive Wind', tag='Excessive_Wind')
STD_ANON_24.Areal_Flood = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Areal Flood', tag='Areal_Flood')
STD_ANON_24.Flash_Flood = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Flash Flood', tag='Flash_Flood')
STD_ANON_24.Dense_Fog = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Dense Fog', tag='Dense_Fog')
STD_ANON_24.Flood = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Flood', tag='Flood')
STD_ANON_24.Frost = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Frost', tag='Frost')
STD_ANON_24.Red_Flag = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Red Flag', tag='Red_Flag')
STD_ANON_24.Fire_Weather = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Fire Weather', tag='Fire_Weather')
STD_ANON_24.Freeze = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Freeze', tag='Freeze')
STD_ANON_24.Gale = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Gale', tag='Gale')
STD_ANON_24.Hurricane_Force_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Hurricane Force Wind', tag='Hurricane_Force_Wind')
STD_ANON_24.Hurricane_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Hurricane Wind', tag='Hurricane_Wind')
STD_ANON_24.Heavy_Snow = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Heavy Snow', tag='Heavy_Snow')
STD_ANON_24.Heat = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Heat', tag='Heat')
STD_ANON_24.Hurricane = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Hurricane', tag='Hurricane')
STD_ANON_24.High_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='High Wind', tag='High_Wind')
STD_ANON_24.Hard_Freeze = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Hard Freeze', tag='Hard_Freeze')
STD_ANON_24.Sleet = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Sleet', tag='Sleet')
STD_ANON_24.Ice_Storm = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Ice Storm', tag='Ice_Storm')
STD_ANON_24.Lake_Effect_Snow_and_Blowing_Snow = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Lake Effect Snow and Blowing Snow', tag='Lake_Effect_Snow_and_Blowing_Snow')
STD_ANON_24.Lake_Effect_Snow = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Lake Effect Snow', tag='Lake_Effect_Snow')
STD_ANON_24.Low_Water = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Low Water', tag='Low_Water')
STD_ANON_24.Lakeshore_Flood = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Lakeshore Flood', tag='Lakeshore_Flood')
STD_ANON_24.Lake_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Lake Wind', tag='Lake_Wind')
STD_ANON_24.Marine = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Marine', tag='Marine')
STD_ANON_24.Special_Marine = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Special Marine', tag='Special_Marine')
STD_ANON_24.Small_Craft_for_Rough_Bar = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Small Craft, for Rough Bar', tag='Small_Craft_for_Rough_Bar')
STD_ANON_24.Snow_and_Blowing_Snow = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Snow and Blowing Snow', tag='Snow_and_Blowing_Snow')
STD_ANON_24.Small_Craft = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Small Craft', tag='Small_Craft')
STD_ANON_24.Hazardous_Seas = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Hazardous Seas', tag='Hazardous_Seas')
STD_ANON_24.Small_Craft_for_Winds = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Small Craft, for Winds', tag='Small_Craft_for_Winds')
STD_ANON_24.Dense_Smoke = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Dense Smoke', tag='Dense_Smoke')
STD_ANON_24.Snow = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Snow', tag='Snow')
STD_ANON_24.Storm = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Storm', tag='Storm')
STD_ANON_24.High_Surf = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='High Surf', tag='High_Surf')
STD_ANON_24.Severe_Thunderstorm = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Severe Thunderstorm', tag='Severe_Thunderstorm')
STD_ANON_24.Small_Craft_for_Hazardous_Seas = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Small Craft, for Hazardous Seas', tag='Small_Craft_for_Hazardous_Seas')
STD_ANON_24.Tropical_Storm_Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Tropical Storm Wind', tag='Tropical_Storm_Wind')
STD_ANON_24.Tornado = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Tornado', tag='Tornado')
STD_ANON_24.Tropical_Storm = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Tropical Storm', tag='Tropical_Storm')
STD_ANON_24.Tsunami = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Tsunami', tag='Tsunami')
STD_ANON_24.Typhoon = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Typhoon', tag='Typhoon')
STD_ANON_24.Freezing_Spray = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Freezing Spray', tag='Freezing_Spray')
STD_ANON_24.Wind_Chill = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Wind Chill', tag='Wind_Chill')
STD_ANON_24.Wind = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Wind', tag='Wind')
STD_ANON_24.Winter_Storm = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Winter Storm', tag='Winter_Storm')
STD_ANON_24.Winter_Weather = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Winter Weather', tag='Winter_Weather')
STD_ANON_24.Freezing_Fog = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Freezing Fog', tag='Freezing_Fog')
STD_ANON_24.Freezing_Rain = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Freezing Rain', tag='Freezing_Rain')
STD_ANON_24.Record_High_Temperature_Possible = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Record High Temperature Possible', tag='Record_High_Temperature_Possible')
STD_ANON_24.Record_Low_Temperature_Possible = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='Record Low Temperature Possible', tag='Record_Low_Temperature_Possible')
STD_ANON_24.none = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 676, 48)
    _Documentation = None
STD_ANON_25._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_25, enum_prefix=None)
STD_ANON_25.Watch = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Watch', tag='Watch')
STD_ANON_25.Statement = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Statement', tag='Statement')
STD_ANON_25.Warning = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Warning', tag='Warning')
STD_ANON_25.Advisory = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='Advisory', tag='Advisory')
STD_ANON_25.none = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 687, 48)
    _Documentation = None
STD_ANON_26._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_26, enum_prefix=None)
STD_ANON_26.long_duration = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='long duration', tag='long_duration')
STD_ANON_26.short_duration = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='short duration', tag='short_duration')
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 729, 24)
    _Documentation = None
STD_ANON_27._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_27, enum_prefix=None)
STD_ANON_27.barometer = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='barometer', tag='barometer')
STD_ANON_27.absolute = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='absolute', tag='absolute')
STD_ANON_27.mean_sea_level = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='mean sea level', tag='mean_sea_level')
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 738, 24)
    _Documentation = None
STD_ANON_28._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_28, enum_prefix=None)
STD_ANON_28.millibars = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='millibars', tag='millibars')
STD_ANON_28.pascals = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='pascals', tag='pascals')
STD_ANON_28.kilopascals = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='kilopascals', tag='kilopascals')
STD_ANON_28.hectopascals = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='hectopascals', tag='hectopascals')
STD_ANON_28.pounds_per_square_inch = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='pounds per square inch', tag='pounds_per_square_inch')
STD_ANON_28.inches_of_mercury = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='inches of mercury', tag='inches_of_mercury')
STD_ANON_28.millimeters_of_mercury = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='millimeters of mercury', tag='millimeters_of_mercury')
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 768, 24)
    _Documentation = None
STD_ANON_29._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_29, enum_prefix=None)
STD_ANON_29.LAMP_VIS = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_VIS', tag='LAMP_VIS')
STD_ANON_29.LAMP_VISCAT = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_VISCAT', tag='LAMP_VISCAT')
STD_ANON_29.LAMP_CVIS = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_CVIS', tag='LAMP_CVIS')
STD_ANON_29.LAMP_CVISCAT = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_CVISCAT', tag='LAMP_CVISCAT')
STD_ANON_29.LAMP_CLD = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_CLD', tag='LAMP_CLD')
STD_ANON_29.LAMP_TP2 = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_TP2', tag='LAMP_TP2')
STD_ANON_29.LAMP_TC2 = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='LAMP_TC2', tag='LAMP_TC2')
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 804, 44)
    _Documentation = None
STD_ANON_30._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_30, enum_prefix=None)
STD_ANON_30.wind = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='wind', tag='wind')
STD_ANON_30.significant = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='significant', tag='significant')
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 812, 44)
    _Documentation = None
STD_ANON_31._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_31, enum_prefix=None)
STD_ANON_31.feet = STD_ANON_31._CF_enumeration.addEnumeration(unicode_value='feet', tag='feet')
STD_ANON_31.meters = STD_ANON_31._CF_enumeration.addEnumeration(unicode_value='meters', tag='meters')
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 844, 44)
    _Documentation = None
STD_ANON_32._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_32, enum_prefix=None)
STD_ANON_32.wind = STD_ANON_32._CF_enumeration.addEnumeration(unicode_value='wind', tag='wind')
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 851, 44)
    _Documentation = None
STD_ANON_33._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_33, enum_prefix=None)
STD_ANON_33.feet = STD_ANON_33._CF_enumeration.addEnumeration(unicode_value='feet', tag='feet')
STD_ANON_33.meters = STD_ANON_33._CF_enumeration.addEnumeration(unicode_value='meters', tag='meters')
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 872, 40)
    _Documentation = None
STD_ANON_34._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_34, enum_prefix=None)
STD_ANON_34.combined = STD_ANON_34._CF_enumeration.addEnumeration(unicode_value='combined', tag='combined')
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 879, 40)
    _Documentation = None
STD_ANON_35._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_35, enum_prefix=None)
STD_ANON_35.feet = STD_ANON_35._CF_enumeration.addEnumeration(unicode_value='feet', tag='feet')
STD_ANON_35.meters = STD_ANON_35._CF_enumeration.addEnumeration(unicode_value='meters', tag='meters')
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 906, 20)
    _Documentation = None
STD_ANON_36._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_36, value=pyxb.binding.datatypes.integer(-459))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 913, 20)
    _Documentation = None
STD_ANON_37._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_37, value=pyxb.binding.datatypes.integer(-459))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 942, 20)
    _Documentation = None
STD_ANON_38._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_38, value=pyxb.binding.datatypes.nonNegativeInteger(360))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_maxInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 949, 20)
    _Documentation = None
STD_ANON_39._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_39, value=pyxb.binding.datatypes.nonNegativeInteger(360))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_maxInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1001, 12)
    _Documentation = None
STD_ANON_40._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_40, enum_prefix=None)
STD_ANON_40.average_temperature_above_normal = STD_ANON_40._CF_enumeration.addEnumeration(unicode_value='average temperature above normal', tag='average_temperature_above_normal')
STD_ANON_40.average_temperature_below_normal = STD_ANON_40._CF_enumeration.addEnumeration(unicode_value='average temperature below normal', tag='average_temperature_below_normal')
STD_ANON_40.average_precipitation_above_normal = STD_ANON_40._CF_enumeration.addEnumeration(unicode_value='average precipitation above normal', tag='average_precipitation_above_normal')
STD_ANON_40.average_precipitation_below_normal = STD_ANON_40._CF_enumeration.addEnumeration(unicode_value='average precipitation below normal', tag='average_precipitation_below_normal')
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_enumeration)

# Atomic simple type: time-layoutAttributeType
class time_layoutAttributeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'time-layoutAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1018, 4)
    _Documentation = None
time_layoutAttributeType._CF_pattern = pyxb.binding.facets.CF_pattern()
time_layoutAttributeType._CF_pattern.addPattern(pattern='k-p\\d+[h|d|m|y]-n\\d+-\\d+')
time_layoutAttributeType._InitializeFacetMap(time_layoutAttributeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'time-layoutAttributeType', time_layoutAttributeType)

# List simple type: decimalValueListType
# superclasses pyxb.binding.datatypes.anySimpleType
class decimalValueListType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.decimal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'decimalValueListType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1026, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.decimal
decimalValueListType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'decimalValueListType', decimalValueListType)

# List simple type: integerValueListType
# superclasses pyxb.binding.datatypes.anySimpleType
class integerValueListType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerValueListType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1030, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.integer
integerValueListType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerValueListType', integerValueListType)

# Atomic simple type: probability-typeType
class probability_typeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'probability-typeType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1051, 4)
    _Documentation = None
probability_typeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=probability_typeType, enum_prefix=None)
probability_typeType.nonexceedance = probability_typeType._CF_enumeration.addEnumeration(unicode_value='nonexceedance', tag='nonexceedance')
probability_typeType.exceedance = probability_typeType._CF_enumeration.addEnumeration(unicode_value='exceedance', tag='exceedance')
probability_typeType._InitializeFacetMap(probability_typeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'probability-typeType', probability_typeType)

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1067, 10)
    _Documentation = None
STD_ANON_41._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_41, enum_prefix=None)
STD_ANON_41.ekdmos_cdf_percentiles = STD_ANON_41._CF_enumeration.addEnumeration(unicode_value='ekdmos-cdf-percentiles', tag='ekdmos_cdf_percentiles')
STD_ANON_41.ekdmos_qpf_probabilities = STD_ANON_41._CF_enumeration.addEnumeration(unicode_value='ekdmos-qpf-probabilities', tag='ekdmos_qpf_probabilities')
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_enumeration)

# Atomic simple type: dataSourceType
class dataSourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dataSourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1079, 4)
    _Documentation = None
dataSourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dataSourceType, enum_prefix=None)
dataSourceType.NDFD = dataSourceType._CF_enumeration.addEnumeration(unicode_value='NDFD', tag='NDFD')
dataSourceType.RTMA = dataSourceType._CF_enumeration.addEnumeration(unicode_value='RTMA', tag='RTMA')
dataSourceType._InitializeFacetMap(dataSourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dataSourceType', dataSourceType)

# Atomic simple type: qualifierType
class qualifierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualifierType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1088, 4)
    _Documentation = None
qualifierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=qualifierType, enum_prefix=None)
qualifierType.emptyString = qualifierType._CF_enumeration.addEnumeration(unicode_value='+/-', tag='emptyString')
qualifierType.emptyString_ = qualifierType._CF_enumeration.addEnumeration(unicode_value='+', tag='emptyString_')
qualifierType.emptyString_2 = qualifierType._CF_enumeration.addEnumeration(unicode_value='-', tag='emptyString_2')
qualifierType.emptyString_3 = qualifierType._CF_enumeration.addEnumeration(unicode_value='%', tag='emptyString_3')
qualifierType._InitializeFacetMap(qualifierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'qualifierType', qualifierType)

# Atomic simple type: percentRange
class percentRange (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentRange')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1099, 4)
    _Documentation = None
percentRange._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=percentRange, value=pyxb.binding.datatypes.nonNegativeInteger(100))
percentRange._InitializeFacetMap(percentRange._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'percentRange', percentRange)

# Atomic simple type: likelihoodUnitsTypes
class likelihoodUnitsTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'likelihoodUnitsTypes')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1107, 4)
    _Documentation = None
likelihoodUnitsTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=likelihoodUnitsTypes, enum_prefix=None)
likelihoodUnitsTypes.percent = likelihoodUnitsTypes._CF_enumeration.addEnumeration(unicode_value='percent', tag='percent')
likelihoodUnitsTypes._InitializeFacetMap(likelihoodUnitsTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'likelihoodUnitsTypes', likelihoodUnitsTypes)

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1128, 10)
    _Documentation = None
STD_ANON_42._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_42, enum_prefix=None)
STD_ANON_42.analysis_error = STD_ANON_42._CF_enumeration.addEnumeration(unicode_value='analysis error', tag='analysis_error')
STD_ANON_42.forecast_error = STD_ANON_42._CF_enumeration.addEnumeration(unicode_value='forecast error', tag='forecast_error')
STD_ANON_42.likelihood = STD_ANON_42._CF_enumeration.addEnumeration(unicode_value='likelihood', tag='likelihood')
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_enumeration)

# Atomic simple type: numberWithEqualityType
class numberWithEqualityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'numberWithEqualityType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1140, 4)
    _Documentation = None
numberWithEqualityType._CF_pattern = pyxb.binding.facets.CF_pattern()
numberWithEqualityType._CF_pattern.addPattern(pattern='(>|\u2265|<|\u2264)?\\d{1,3}')
numberWithEqualityType._InitializeFacetMap(numberWithEqualityType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'numberWithEqualityType', numberWithEqualityType)

# Atomic simple type: summarizationType
class summarizationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'summarizationType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/summarizationType.xsd', 15, 4)
    _Documentation = None
summarizationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=summarizationType, enum_prefix=None)
summarizationType.none = summarizationType._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
summarizationType.mean = summarizationType._CF_enumeration.addEnumeration(unicode_value='mean', tag='mean')
summarizationType.maximum = summarizationType._CF_enumeration.addEnumeration(unicode_value='maximum', tag='maximum')
summarizationType.minimum = summarizationType._CF_enumeration.addEnumeration(unicode_value='minimum', tag='minimum')
summarizationType.n12hourly = summarizationType._CF_enumeration.addEnumeration(unicode_value='12hourly', tag='n12hourly')
summarizationType.n24hourly = summarizationType._CF_enumeration.addEnumeration(unicode_value='24hourly', tag='n24hourly')
summarizationType.national = summarizationType._CF_enumeration.addEnumeration(unicode_value='national', tag='national')
summarizationType.conus = summarizationType._CF_enumeration.addEnumeration(unicode_value='conus', tag='conus')
summarizationType.alaska = summarizationType._CF_enumeration.addEnumeration(unicode_value='alaska', tag='alaska')
summarizationType._InitializeFacetMap(summarizationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'summarizationType', summarizationType)

# Atomic simple type: time-coordinateType
class time_coordinateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'time-coordinateType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 30, 4)
    _Documentation = None
time_coordinateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=time_coordinateType, enum_prefix=None)
time_coordinateType.UTC = time_coordinateType._CF_enumeration.addEnumeration(unicode_value='UTC', tag='UTC')
time_coordinateType.local = time_coordinateType._CF_enumeration.addEnumeration(unicode_value='local', tag='local')
time_coordinateType._InitializeFacetMap(time_coordinateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'time-coordinateType', time_coordinateType)

# Atomic simple type: layout-keyType
class layout_keyType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'layout-keyType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 45, 4)
    _Documentation = None
layout_keyType._CF_pattern = pyxb.binding.facets.CF_pattern()
layout_keyType._CF_pattern.addPattern(pattern='k-p\\d+[h|d|m|y]-n\\d+-\\d+')
layout_keyType._InitializeFacetMap(layout_keyType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'layout-keyType', layout_keyType)

# Atomic simple type: latLonListType
class latLonListType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'latLonListType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 23, 3)
    _Documentation = None
latLonListType._CF_pattern = pyxb.binding.facets.CF_pattern()
latLonListType._CF_pattern.addPattern(pattern='[\\-]?\\d{1,2}\\.\\d+,[\\-]?\\d{1,3}\\.\\d+( [\\-]?\\d{1,2}\\.\\d+,[\\-]?\\d{1,3}\\.\\d+)*')
latLonListType._InitializeFacetMap(latLonListType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'latLonListType', latLonListType)

# Atomic simple type: cityNameListType
class cityNameListType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cityNameListType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 37, 3)
    _Documentation = None
cityNameListType._CF_pattern = pyxb.binding.facets.CF_pattern()
cityNameListType._CF_pattern.addPattern(pattern="[a-zA-Z'\\-]*( ?[a-zA-Z'\\-]*)*,[A-Z][A-Z](\\|[a-zA-Z'\\-]*( ?[a-zA-Z'\\-]*)*,[A-Z][A-Z])*")
cityNameListType._InitializeFacetMap(cityNameListType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cityNameListType', cityNameListType)

# Union simple type: numberValueListType
# superclasses pyxb.binding.datatypes.anySimpleType
class numberValueListType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of decimalValueListType, integerValueListType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'numberValueListType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1034, 4)
    _Documentation = None

    _MemberTypes = ( decimalValueListType, integerValueListType, )
numberValueListType._CF_pattern = pyxb.binding.facets.CF_pattern()
numberValueListType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=numberValueListType)
numberValueListType._InitializeFacetMap(numberValueListType._CF_pattern,
   numberValueListType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'numberValueListType', numberValueListType)

# Complex type locationType with content type ELEMENT_ONLY
class locationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type locationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 18, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location-key uses Python identifier location_key
    __location_key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location-key'), 'location_key', '__AbsentNamespace0_locationType_location_key', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 20, 11), )

    
    location_key = property(__location_key.value, __location_key.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_locationType_description', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 21, 11), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_locationType_point', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 23, 14), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Element nws-zone uses Python identifier nws_zone
    __nws_zone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'nws-zone'), 'nws_zone', '__AbsentNamespace0_locationType_nws_zone', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 24, 14), )

    
    nws_zone = property(__nws_zone.value, __nws_zone.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_locationType_area', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 25, 14), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__AbsentNamespace0_locationType_city', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 27, 11), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element area-description uses Python identifier area_description
    __area_description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area-description'), 'area_description', '__AbsentNamespace0_locationType_area_description', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 28, 11), )

    
    area_description = property(__area_description.value, __area_description.set, None, None)

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_locationType_height', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 30, 14), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element level uses Python identifier level
    __level = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'level'), 'level', '__AbsentNamespace0_locationType_level', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 31, 14), )

    
    level = property(__level.value, __level.set, None, None)

    
    # Element layer uses Python identifier layer
    __layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'layer'), 'layer', '__AbsentNamespace0_locationType_layer', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 32, 14), )

    
    layer = property(__layer.value, __layer.set, None, None)

    _ElementMap.update({
        __location_key.name() : __location_key,
        __description.name() : __description,
        __point.name() : __point,
        __nws_zone.name() : __nws_zone,
        __area.name() : __area,
        __city.name() : __city,
        __area_description.name() : __area_description,
        __height.name() : __height,
        __level.name() : __level,
        __layer.name() : __layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'locationType', locationType)


# Complex type levelType with content type SIMPLE
class levelType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type levelType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'levelType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 112, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute vertical-coordinate uses Python identifier vertical_coordinate
    __vertical_coordinate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vertical-coordinate'), 'vertical_coordinate', '__AbsentNamespace0_levelType_vertical_coordinate', pyxb.binding.datatypes.string)
    __vertical_coordinate._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 115, 17)
    __vertical_coordinate._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 115, 17)
    
    vertical_coordinate = property(__vertical_coordinate.value, __vertical_coordinate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vertical_coordinate.name() : __vertical_coordinate
    })
Namespace.addCategoryObject('typeBinding', 'levelType', levelType)


# Complex type layerType with content type SIMPLE
class layerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type layerType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'layerType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 120, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute vertical-coordinate uses Python identifier vertical_coordinate
    __vertical_coordinate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vertical-coordinate'), 'vertical_coordinate', '__AbsentNamespace0_layerType_vertical_coordinate', pyxb.binding.datatypes.string)
    __vertical_coordinate._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 123, 17)
    __vertical_coordinate._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 123, 17)
    
    vertical_coordinate = property(__vertical_coordinate.value, __vertical_coordinate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vertical_coordinate.name() : __vertical_coordinate
    })
Namespace.addCategoryObject('typeBinding', 'layerType', layerType)


# Complex type headType with content type ELEMENT_ONLY
class headType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type headType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'headType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element product uses Python identifier product
    __product = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'product'), 'product', '__AbsentNamespace0_headType_product', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 16, 12), )

    
    product = property(__product.value, __product.set, None, None)

    
    # Element source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_headType_source', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 17, 12), )

    
    source = property(__source.value, __source.set, None, None)

    _ElementMap.update({
        __product.name() : __product,
        __source.name() : __source
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'headType', headType)


# Complex type creation-dateType with content type SIMPLE
class creation_dateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type creation-dateType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'creation-dateType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 50, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    
    # Attribute refresh-frequency uses Python identifier refresh_frequency
    __refresh_frequency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refresh-frequency'), 'refresh_frequency', '__AbsentNamespace0_creation_dateType_refresh_frequency', pyxb.binding.datatypes.duration, required=True)
    __refresh_frequency._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 53, 13)
    __refresh_frequency._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 53, 13)
    
    refresh_frequency = property(__refresh_frequency.value, __refresh_frequency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __refresh_frequency.name() : __refresh_frequency
    })
Namespace.addCategoryObject('typeBinding', 'creation-dateType', creation_dateType)


# Complex type sourceType with content type ELEMENT_ONLY
class sourceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type sourceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 58, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element more-information uses Python identifier more_information
    __more_information = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'more-information'), 'more_information', '__AbsentNamespace0_sourceType_more_information', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 60, 10), )

    
    more_information = property(__more_information.value, __more_information.set, None, None)

    
    # Element production-center uses Python identifier production_center
    __production_center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'production-center'), 'production_center', '__AbsentNamespace0_sourceType_production_center', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 61, 10), )

    
    production_center = property(__production_center.value, __production_center.set, None, None)

    
    # Element disclaimer uses Python identifier disclaimer
    __disclaimer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'disclaimer'), 'disclaimer', '__AbsentNamespace0_sourceType_disclaimer', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 62, 10), )

    
    disclaimer = property(__disclaimer.value, __disclaimer.set, None, None)

    
    # Element credit uses Python identifier credit
    __credit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'credit'), 'credit', '__AbsentNamespace0_sourceType_credit', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 63, 10), )

    
    credit = property(__credit.value, __credit.set, None, None)

    
    # Element credit-logo uses Python identifier credit_logo
    __credit_logo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'credit-logo'), 'credit_logo', '__AbsentNamespace0_sourceType_credit_logo', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 64, 10), )

    
    credit_logo = property(__credit_logo.value, __credit_logo.set, None, None)

    
    # Element feedback uses Python identifier feedback
    __feedback = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'feedback'), 'feedback', '__AbsentNamespace0_sourceType_feedback', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 65, 10), )

    
    feedback = property(__feedback.value, __feedback.set, None, None)

    _ElementMap.update({
        __more_information.name() : __more_information,
        __production_center.name() : __production_center,
        __disclaimer.name() : __disclaimer,
        __credit.name() : __credit,
        __credit_logo.name() : __credit_logo,
        __feedback.name() : __feedback
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'sourceType', sourceType)


# Complex type production-centerType with content type MIXED
class production_centerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type production-centerType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'production-centerType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 69, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sub-center uses Python identifier sub_center
    __sub_center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sub-center'), 'sub_center', '__AbsentNamespace0_production_centerType_sub_center', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 71, 10), )

    
    sub_center = property(__sub_center.value, __sub_center.set, None, None)

    _ElementMap.update({
        __sub_center.name() : __sub_center
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'production-centerType', production_centerType)


# Complex type moreWeatherInformationType with content type SIMPLE
class moreWeatherInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type moreWeatherInformationType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'moreWeatherInformationType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/moreWeatherInformation.xsd', 15, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute applicable-location uses Python identifier applicable_location
    __applicable_location = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applicable-location'), 'applicable_location', '__AbsentNamespace0_moreWeatherInformationType_applicable_location', pyxb.binding.datatypes.string, required=True)
    __applicable_location._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/moreWeatherInformation.xsd', 18, 12)
    __applicable_location._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/moreWeatherInformation.xsd', 18, 12)
    
    applicable_location = property(__applicable_location.value, __applicable_location.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __applicable_location.name() : __applicable_location
    })
Namespace.addCategoryObject('typeBinding', 'moreWeatherInformationType', moreWeatherInformationType)


# Complex type parametersType with content type ELEMENT_ONLY
class parametersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type parametersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'parametersType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 21, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element categories uses Python identifier categories
    __categories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'categories'), 'categories', '__AbsentNamespace0_parametersType_categories', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 26, 12), )

    
    categories = property(__categories.value, __categories.set, None, None)

    
    # Element temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'temperature'), 'temperature', '__AbsentNamespace0_parametersType_temperature', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 30, 12), )

    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Element precipitation uses Python identifier precipitation
    __precipitation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'precipitation'), 'precipitation', '__AbsentNamespace0_parametersType_precipitation', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 93, 12), )

    
    precipitation = property(__precipitation.value, __precipitation.set, None, None)

    
    # Element probability-of-precipitation uses Python identifier probability_of_precipitation
    __probability_of_precipitation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'probability-of-precipitation'), 'probability_of_precipitation', '__AbsentNamespace0_parametersType_probability_of_precipitation', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 150, 12), )

    
    probability_of_precipitation = property(__probability_of_precipitation.value, __probability_of_precipitation.set, None, None)

    
    # Element fire-weather uses Python identifier fire_weather
    __fire_weather = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fire-weather'), 'fire_weather', '__AbsentNamespace0_parametersType_fire_weather', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 180, 12), )

    
    fire_weather = property(__fire_weather.value, __fire_weather.set, None, None)

    
    # Element convective-hazard uses Python identifier convective_hazard
    __convective_hazard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'convective-hazard'), 'convective_hazard', '__AbsentNamespace0_parametersType_convective_hazard', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 210, 12), )

    
    convective_hazard = property(__convective_hazard.value, __convective_hazard.set, None, None)

    
    # Element climate-anomaly uses Python identifier climate_anomaly
    __climate_anomaly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'climate-anomaly'), 'climate_anomaly', '__AbsentNamespace0_parametersType_climate_anomaly', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 275, 12), )

    
    climate_anomaly = property(__climate_anomaly.value, __climate_anomaly.set, None, None)

    
    # Element wind-speed uses Python identifier wind_speed
    __wind_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'wind-speed'), 'wind_speed', '__AbsentNamespace0_parametersType_wind_speed', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 287, 12), )

    
    wind_speed = property(__wind_speed.value, __wind_speed.set, None, None)

    
    # Element direction uses Python identifier direction
    __direction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'direction'), 'direction', '__AbsentNamespace0_parametersType_direction', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 341, 12), )

    
    direction = property(__direction.value, __direction.set, None, None)

    
    # Element cloud-amount uses Python identifier cloud_amount
    __cloud_amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cloud-amount'), 'cloud_amount', '__AbsentNamespace0_parametersType_cloud_amount', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 379, 12), )

    
    cloud_amount = property(__cloud_amount.value, __cloud_amount.set, None, None)

    
    # Element humidity uses Python identifier humidity
    __humidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'humidity'), 'humidity', '__AbsentNamespace0_parametersType_humidity', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 416, 12), )

    
    humidity = property(__humidity.value, __humidity.set, None, None)

    
    # Element weather uses Python identifier weather
    __weather = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weather'), 'weather', '__AbsentNamespace0_parametersType_weather', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 449, 12), )

    
    weather = property(__weather.value, __weather.set, None, None)

    
    # Element conditions-icon uses Python identifier conditions_icon
    __conditions_icon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'conditions-icon'), 'conditions_icon', '__AbsentNamespace0_parametersType_conditions_icon', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 573, 12), )

    
    conditions_icon = property(__conditions_icon.value, __conditions_icon.set, None, None)

    
    # Element hazards uses Python identifier hazards
    __hazards = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazards'), 'hazards', '__AbsentNamespace0_parametersType_hazards', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 592, 12), )

    
    hazards = property(__hazards.value, __hazards.set, None, None)

    
    # Element wordedForecast uses Python identifier wordedForecast
    __wordedForecast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'wordedForecast'), 'wordedForecast', '__AbsentNamespace0_parametersType_wordedForecast', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 708, 11), )

    
    wordedForecast = property(__wordedForecast.value, __wordedForecast.set, None, None)

    
    # Element pressure uses Python identifier pressure
    __pressure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pressure'), 'pressure', '__AbsentNamespace0_parametersType_pressure', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 722, 12), )

    
    pressure = property(__pressure.value, __pressure.set, None, None)

    
    # Element probabilisticCondition uses Python identifier probabilisticCondition
    __probabilisticCondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'probabilisticCondition'), 'probabilisticCondition', '__AbsentNamespace0_parametersType_probabilisticCondition', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 758, 12), )

    
    probabilisticCondition = property(__probabilisticCondition.value, __probabilisticCondition.set, None, None)

    
    # Element water-state uses Python identifier water_state
    __water_state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'water-state'), 'water_state', '__AbsentNamespace0_parametersType_water_state', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 792, 12), )

    
    water_state = property(__water_state.value, __water_state.set, None, None)

    
    # Attribute applicable-location uses Python identifier applicable_location
    __applicable_location = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applicable-location'), 'applicable_location', '__AbsentNamespace0_parametersType_applicable_location', pyxb.binding.datatypes.string, required=True)
    __applicable_location._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 897, 8)
    __applicable_location._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 897, 8)
    
    applicable_location = property(__applicable_location.value, __applicable_location.set, None, None)

    _ElementMap.update({
        __categories.name() : __categories,
        __temperature.name() : __temperature,
        __precipitation.name() : __precipitation,
        __probability_of_precipitation.name() : __probability_of_precipitation,
        __fire_weather.name() : __fire_weather,
        __convective_hazard.name() : __convective_hazard,
        __climate_anomaly.name() : __climate_anomaly,
        __wind_speed.name() : __wind_speed,
        __direction.name() : __direction,
        __cloud_amount.name() : __cloud_amount,
        __humidity.name() : __humidity,
        __weather.name() : __weather,
        __conditions_icon.name() : __conditions_icon,
        __hazards.name() : __hazards,
        __wordedForecast.name() : __wordedForecast,
        __pressure.name() : __pressure,
        __probabilisticCondition.name() : __probabilisticCondition,
        __water_state.name() : __water_state
    })
    _AttributeMap.update({
        __applicable_location.name() : __applicable_location
    })
Namespace.addCategoryObject('typeBinding', 'parametersType', parametersType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 211, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element outlook uses Python identifier outlook
    __outlook = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outlook'), 'outlook', '__AbsentNamespace0_CTD_ANON_outlook', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 213, 23), )

    
    outlook = property(__outlook.value, __outlook.set, None, None)

    
    # Element severe-component uses Python identifier severe_component
    __severe_component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'severe-component'), 'severe_component', '__AbsentNamespace0_CTD_ANON_severe_component', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 234, 23), )

    
    severe_component = property(__severe_component.value, __severe_component.set, None, None)

    _ElementMap.update({
        __outlook.name() : __outlook,
        __severe_component.name() : __severe_component
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 276, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element weekly uses Python identifier weekly
    __weekly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weekly'), 'weekly', '__AbsentNamespace0_CTD_ANON__weekly', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 278, 24), )

    
    weekly = property(__weekly.value, __weekly.set, None, None)

    
    # Element monthly uses Python identifier monthly
    __monthly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'monthly'), 'monthly', '__AbsentNamespace0_CTD_ANON__monthly', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 279, 24), )

    
    monthly = property(__monthly.value, __monthly.set, None, None)

    
    # Element seasonal uses Python identifier seasonal
    __seasonal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'seasonal'), 'seasonal', '__AbsentNamespace0_CTD_ANON__seasonal', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 280, 24), )

    
    seasonal = property(__seasonal.value, __seasonal.set, None, None)

    _ElementMap.update({
        __weekly.name() : __weekly,
        __monthly.name() : __monthly,
        __seasonal.name() : __seasonal
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 454, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_2_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 456, 36), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_2_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 561, 32)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 561, 32)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_2_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 562, 32)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 562, 32)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute weather-summary uses Python identifier weather_summary
    __weather_summary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'weather-summary'), 'weather_summary', '__AbsentNamespace0_CTD_ANON_2_weather_summary', pyxb.binding.datatypes.string)
    __weather_summary._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 563, 32)
    __weather_summary._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 563, 32)
    
    weather_summary = property(__weather_summary.value, __weather_summary.set, None, None)

    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __weather_summary.name() : __weather_summary
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 597, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element hazard uses Python identifier hazard
    __hazard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazard'), 'hazard', '__AbsentNamespace0_CTD_ANON_3_hazard', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 599, 36), )

    
    hazard = property(__hazard.value, __hazard.set, None, None)

    _ElementMap.update({
        __hazard.name() : __hazard
    })
    _AttributeMap.update({
        
    })



# Complex type valueForRangeType with content type ELEMENT_ONLY
class valueForRangeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type valueForRangeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'valueForRangeType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1156, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lt uses Python identifier lt
    __lt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lt'), 'lt', '__AbsentNamespace0_valueForRangeType_lt', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1148, 4), )

    
    lt = property(__lt.value, __lt.set, None, None)

    
    # Element le uses Python identifier le
    __le = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'le'), 'le', '__AbsentNamespace0_valueForRangeType_le', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1149, 4), )

    
    le = property(__le.value, __le.set, None, None)

    
    # Element gt uses Python identifier gt
    __gt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gt'), 'gt', '__AbsentNamespace0_valueForRangeType_gt', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1150, 4), )

    
    gt = property(__gt.value, __gt.set, None, None)

    
    # Element ge uses Python identifier ge
    __ge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ge'), 'ge', '__AbsentNamespace0_valueForRangeType_ge', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1151, 4), )

    
    ge = property(__ge.value, __ge.set, None, None)

    
    # Element eq uses Python identifier eq
    __eq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eq'), 'eq', '__AbsentNamespace0_valueForRangeType_eq', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1152, 4), )

    
    eq = property(__eq.value, __eq.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_valueForRangeType_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1158, 8), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __lt.name() : __lt,
        __le.name() : __le,
        __gt.name() : __gt,
        __ge.name() : __ge,
        __eq.name() : __eq,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'valueForRangeType', valueForRangeType)


# Complex type start-valid-timeType with content type SIMPLE
class start_valid_timeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type start-valid-timeType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'start-valid-timeType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    
    # Attribute period-name uses Python identifier period_name
    __period_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period-name'), 'period_name', '__AbsentNamespace0_start_valid_timeType_period_name', pyxb.binding.datatypes.string)
    __period_name._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 40, 16)
    __period_name._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 40, 16)
    
    period_name = property(__period_name.value, __period_name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __period_name.name() : __period_name
    })
Namespace.addCategoryObject('typeBinding', 'start-valid-timeType', start_valid_timeType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 52, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element head uses Python identifier head
    __head = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'head'), 'head', '__AbsentNamespace0_CTD_ANON_4_head', False, pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 55, 15), )

    
    head = property(__head.value, __head.set, None, None)

    
    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'data'), 'data', '__AbsentNamespace0_CTD_ANON_4_data', True, pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 56, 15), )

    
    data = property(__data.value, __data.set, None, None)

    
    # Element minResolution uses Python identifier minResolution
    __minResolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minResolution'), 'minResolution', '__AbsentNamespace0_CTD_ANON_4_minResolution', False, pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 88, 15), )

    
    minResolution = property(__minResolution.value, __minResolution.set, None, None)

    
    # Element latLonList uses Python identifier latLonList
    __latLonList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'latLonList'), 'latLonList', '__AbsentNamespace0_CTD_ANON_4_latLonList', False, pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 89, 15), )

    
    latLonList = property(__latLonList.value, __latLonList.set, None, None)

    
    # Element cityNameList uses Python identifier cityNameList
    __cityNameList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cityNameList'), 'cityNameList', '__AbsentNamespace0_CTD_ANON_4_cityNameList', False, pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 90, 15), )

    
    cityNameList = property(__cityNameList.value, __cityNameList.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_4_version', pyxb.binding.datatypes.string, unicode_default='1.0')
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 93, 9)
    __version._UseLocation = pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 93, 9)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __head.name() : __head,
        __data.name() : __data,
        __minResolution.name() : __minResolution,
        __latLonList.name() : __latLonList,
        __cityNameList.name() : __cityNameList
    })
    _AttributeMap.update({
        __version.name() : __version
    })



# Complex type pointType with content type EMPTY
class pointType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type pointType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pointType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 37, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'latitude'), 'latitude', '__AbsentNamespace0_pointType_latitude', pyxb.binding.datatypes.decimal, required=True)
    __latitude._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 38, 9)
    __latitude._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 38, 9)
    
    latitude = property(__latitude.value, __latitude.set, None, None)

    
    # Attribute longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'longitude'), 'longitude', '__AbsentNamespace0_pointType_longitude', pyxb.binding.datatypes.decimal, required=True)
    __longitude._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 39, 9)
    __longitude._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 39, 9)
    
    longitude = property(__longitude.value, __longitude.set, None, None)

    
    # Attribute summarization uses Python identifier summarization
    __summarization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summarization'), 'summarization', '__AbsentNamespace0_pointType_summarization', summarizationType)
    __summarization._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 40, 9)
    __summarization._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 40, 9)
    
    summarization = property(__summarization.value, __summarization.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __summarization.name() : __summarization
    })
Namespace.addCategoryObject('typeBinding', 'pointType', pointType)


# Complex type cityType with content type SIMPLE
class cityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cityType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cityType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 43, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__AbsentNamespace0_cityType_state', pyxb.binding.datatypes.string, required=True)
    __state._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 46, 17)
    __state._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 46, 17)
    
    state = property(__state.value, __state.set, None, None)

    
    # Attribute summarization uses Python identifier summarization
    __summarization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summarization'), 'summarization', '__AbsentNamespace0_cityType_summarization', summarizationType)
    __summarization._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 47, 17)
    __summarization._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 47, 17)
    
    summarization = property(__summarization.value, __summarization.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __state.name() : __state,
        __summarization.name() : __summarization
    })
Namespace.addCategoryObject('typeBinding', 'cityType', cityType)


# Complex type nws-zoneType with content type SIMPLE
class nws_zoneType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type nws-zoneType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nws-zoneType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 52, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__AbsentNamespace0_nws_zoneType_state', pyxb.binding.datatypes.string, required=True)
    __state._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 55, 17)
    __state._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 55, 17)
    
    state = property(__state.value, __state.set, None, None)

    
    # Attribute summarization uses Python identifier summarization
    __summarization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summarization'), 'summarization', '__AbsentNamespace0_nws_zoneType_summarization', summarizationType)
    __summarization._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 56, 17)
    __summarization._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 56, 17)
    
    summarization = property(__summarization.value, __summarization.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __state.name() : __state,
        __summarization.name() : __summarization
    })
Namespace.addCategoryObject('typeBinding', 'nws-zoneType', nws_zoneType)


# Complex type areaType with content type ELEMENT_ONLY
class areaType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type areaType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'areaType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 61, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element circle uses Python identifier circle
    __circle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'circle'), 'circle', '__AbsentNamespace0_areaType_circle', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 63, 13), )

    
    circle = property(__circle.value, __circle.set, None, None)

    
    # Element rectangle uses Python identifier rectangle
    __rectangle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rectangle'), 'rectangle', '__AbsentNamespace0_areaType_rectangle', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 64, 13), )

    
    rectangle = property(__rectangle.value, __rectangle.set, None, None)

    
    # Attribute area-type uses Python identifier area_type
    __area_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'area-type'), 'area_type', '__AbsentNamespace0_areaType_area_type', STD_ANON)
    __area_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 66, 9)
    __area_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 66, 9)
    
    area_type = property(__area_type.value, __area_type.set, None, None)

    _ElementMap.update({
        __circle.name() : __circle,
        __rectangle.name() : __rectangle
    })
    _AttributeMap.update({
        __area_type.name() : __area_type
    })
Namespace.addCategoryObject('typeBinding', 'areaType', areaType)


# Complex type circleType with content type ELEMENT_ONLY
class circleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type circleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'circleType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 76, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_circleType_point', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 78, 13), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_circleType_radius', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 79, 13), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Attribute summarization uses Python identifier summarization
    __summarization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summarization'), 'summarization', '__AbsentNamespace0_circleType_summarization', summarizationType)
    __summarization._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 82, 9)
    __summarization._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 82, 9)
    
    summarization = property(__summarization.value, __summarization.set, None, None)

    _ElementMap.update({
        __point.name() : __point,
        __radius.name() : __radius
    })
    _AttributeMap.update({
        __summarization.name() : __summarization
    })
Namespace.addCategoryObject('typeBinding', 'circleType', circleType)


# Complex type radiusType with content type EMPTY
class radiusType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type radiusType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'radiusType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 85, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute radius-units uses Python identifier radius_units
    __radius_units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius-units'), 'radius_units', '__AbsentNamespace0_radiusType_radius_units', STD_ANON_, required=True)
    __radius_units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 86, 8)
    __radius_units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 86, 8)
    
    radius_units = property(__radius_units.value, __radius_units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __radius_units.name() : __radius_units
    })
Namespace.addCategoryObject('typeBinding', 'radiusType', radiusType)


# Complex type rectangleType with content type ELEMENT_ONLY
class rectangleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type rectangleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rectangleType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 96, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_rectangleType_point', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 98, 13), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Attribute summarization uses Python identifier summarization
    __summarization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summarization'), 'summarization', '__AbsentNamespace0_rectangleType_summarization', summarizationType)
    __summarization._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 100, 9)
    __summarization._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 100, 9)
    
    summarization = property(__summarization.value, __summarization.set, None, None)

    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        __summarization.name() : __summarization
    })
Namespace.addCategoryObject('typeBinding', 'rectangleType', rectangleType)


# Complex type heightType with content type SIMPLE
class heightType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type heightType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'heightType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 103, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute datum uses Python identifier datum
    __datum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'datum'), 'datum', '__AbsentNamespace0_heightType_datum', datumType, required=True)
    __datum._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 106, 17)
    __datum._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 106, 17)
    
    datum = property(__datum.value, __datum.set, None, None)

    
    # Attribute height-units uses Python identifier height_units
    __height_units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'height-units'), 'height_units', '__AbsentNamespace0_heightType_height_units', height_unitsType)
    __height_units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 107, 17)
    __height_units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 107, 17)
    
    height_units = property(__height_units.value, __height_units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __datum.name() : __datum,
        __height_units.name() : __height_units
    })
Namespace.addCategoryObject('typeBinding', 'heightType', heightType)


# Complex type productType with content type ELEMENT_ONLY
class productType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type productType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'productType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 21, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_productType_title', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 23, 10), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'field'), 'field', '__AbsentNamespace0_productType_field', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 24, 10), )

    
    field = property(__field.value, __field.set, None, None)

    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_productType_category', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 25, 10), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element creation-date uses Python identifier creation_date
    __creation_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'creation-date'), 'creation_date', '__AbsentNamespace0_productType_creation_date', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 26, 10), )

    
    creation_date = property(__creation_date.value, __creation_date.set, None, None)

    
    # Attribute concise-name uses Python identifier concise_name
    __concise_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'concise-name'), 'concise_name', '__AbsentNamespace0_productType_concise_name', concise_nameType, required=True)
    __concise_name._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 28, 7)
    __concise_name._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 28, 7)
    
    concise_name = property(__concise_name.value, __concise_name.set, None, None)

    
    # Attribute operational-mode uses Python identifier operational_mode
    __operational_mode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'operational-mode'), 'operational_mode', '__AbsentNamespace0_productType_operational_mode', operational_modeType, required=True)
    __operational_mode._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 29, 7)
    __operational_mode._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 29, 7)
    
    operational_mode = property(__operational_mode.value, __operational_mode.set, None, None)

    
    # Attribute srsName uses Python identifier srsName
    __srsName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srsName'), 'srsName', '__AbsentNamespace0_productType_srsName', srsNameType, required=True)
    __srsName._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 30, 7)
    __srsName._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 30, 7)
    
    srsName = property(__srsName.value, __srsName.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __field.name() : __field,
        __category.name() : __category,
        __creation_date.name() : __creation_date
    })
    _AttributeMap.update({
        __concise_name.name() : __concise_name,
        __operational_mode.name() : __operational_mode,
        __srsName.name() : __srsName
    })
Namespace.addCategoryObject('typeBinding', 'productType', productType)


# Complex type dataType with content type ELEMENT_ONLY
class dataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type dataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dataType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_dataType_location', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 26, 12), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element moreWeatherInformation uses Python identifier moreWeatherInformation
    __moreWeatherInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'moreWeatherInformation'), 'moreWeatherInformation', '__AbsentNamespace0_dataType_moreWeatherInformation', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 27, 12), )

    
    moreWeatherInformation = property(__moreWeatherInformation.value, __moreWeatherInformation.set, None, None)

    
    # Element time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_dataType_time_layout', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 28, 12), )

    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Element parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameters'), 'parameters', '__AbsentNamespace0_dataType_parameters', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 29, 12), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_dataType_type', STD_ANON_2)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 31, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 31, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __moreWeatherInformation.name() : __moreWeatherInformation,
        __time_layout.name() : __time_layout,
        __parameters.name() : __parameters
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'dataType', dataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 31, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_5_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 33, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_5_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 35, 28), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueList uses Python identifier valueList
    __valueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueList'), 'valueList', '__AbsentNamespace0_CTD_ANON_5_valueList', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 36, 28), )

    
    valueList = property(__valueList.value, __valueList.set, None, None)

    
    # Element valueWithUncertainty uses Python identifier valueWithUncertainty
    __valueWithUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), 'valueWithUncertainty', '__AbsentNamespace0_CTD_ANON_5_valueWithUncertainty', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 37, 28), )

    
    valueWithUncertainty = property(__valueWithUncertainty.value, __valueWithUncertainty.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_5_type', STD_ANON_3, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 51, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 51, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_5_units', STD_ANON_4, unicode_default='Fahrenheit')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 74, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 74, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute likelihoodUnits uses Python identifier likelihoodUnits
    __likelihoodUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'likelihoodUnits'), 'likelihoodUnits', '__AbsentNamespace0_CTD_ANON_5_likelihoodUnits', likelihoodUnitsTypes)
    __likelihoodUnits._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 82, 20)
    __likelihoodUnits._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 82, 20)
    
    likelihoodUnits = property(__likelihoodUnits.value, __likelihoodUnits.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_5_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 83, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 83, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_5_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 84, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 84, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_5_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 85, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 85, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute applicable-categories uses Python identifier applicable_categories
    __applicable_categories = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applicable-categories'), 'applicable_categories', '__AbsentNamespace0_CTD_ANON_5_applicable_categories', pyxb.binding.datatypes.string)
    __applicable_categories._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 86, 20)
    __applicable_categories._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 86, 20)
    
    applicable_categories = property(__applicable_categories.value, __applicable_categories.set, None, None)

    
    # Attribute probability-type uses Python identifier probability_type
    __probability_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability-type'), 'probability_type', '__AbsentNamespace0_CTD_ANON_5_probability_type', probability_typeType)
    __probability_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 87, 20)
    __probability_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 87, 20)
    
    probability_type = property(__probability_type.value, __probability_type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueList.name() : __valueList,
        __valueWithUncertainty.name() : __valueWithUncertainty
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __likelihoodUnits.name() : __likelihoodUnits,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __applicable_categories.name() : __applicable_categories,
        __probability_type.name() : __probability_type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 38, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_6_value', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 40, 40), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__AbsentNamespace0_CTD_ANON_6_uncertainty', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 42, 43), )

    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Element numberWithEquality uses Python identifier numberWithEquality
    __numberWithEquality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), 'numberWithEquality', '__AbsentNamespace0_CTD_ANON_6_numberWithEquality', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 43, 43), )

    
    numberWithEquality = property(__numberWithEquality.value, __numberWithEquality.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_6_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 46, 36)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 46, 36)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __uncertainty.name() : __uncertainty,
        __numberWithEquality.name() : __numberWithEquality
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 94, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_7_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 96, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_7_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 98, 28), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueList uses Python identifier valueList
    __valueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueList'), 'valueList', '__AbsentNamespace0_CTD_ANON_7_valueList', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 99, 28), )

    
    valueList = property(__valueList.value, __valueList.set, None, None)

    
    # Element valueWithUncertainty uses Python identifier valueWithUncertainty
    __valueWithUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), 'valueWithUncertainty', '__AbsentNamespace0_CTD_ANON_7_valueWithUncertainty', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 100, 28), )

    
    valueWithUncertainty = property(__valueWithUncertainty.value, __valueWithUncertainty.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_7_type', STD_ANON_5, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 114, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 114, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_7_units', STD_ANON_6, unicode_default='inches')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 128, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 128, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute likelihoodUnits uses Python identifier likelihoodUnits
    __likelihoodUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'likelihoodUnits'), 'likelihoodUnits', '__AbsentNamespace0_CTD_ANON_7_likelihoodUnits', likelihoodUnitsTypes)
    __likelihoodUnits._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 140, 20)
    __likelihoodUnits._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 140, 20)
    
    likelihoodUnits = property(__likelihoodUnits.value, __likelihoodUnits.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_7_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 141, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 141, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_7_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 142, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 142, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_7_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 143, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 143, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute probability-type uses Python identifier probability_type
    __probability_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability-type'), 'probability_type', '__AbsentNamespace0_CTD_ANON_7_probability_type', probability_typeType)
    __probability_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 144, 20)
    __probability_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 144, 20)
    
    probability_type = property(__probability_type.value, __probability_type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueList.name() : __valueList,
        __valueWithUncertainty.name() : __valueWithUncertainty
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __likelihoodUnits.name() : __likelihoodUnits,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __probability_type.name() : __probability_type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 101, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_8_value', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 103, 40), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__AbsentNamespace0_CTD_ANON_8_uncertainty', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 105, 43), )

    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Element numberWithEquality uses Python identifier numberWithEquality
    __numberWithEquality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), 'numberWithEquality', '__AbsentNamespace0_CTD_ANON_8_numberWithEquality', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 106, 43), )

    
    numberWithEquality = property(__numberWithEquality.value, __numberWithEquality.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_8_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 109, 36)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 109, 36)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __uncertainty.name() : __uncertainty,
        __numberWithEquality.name() : __numberWithEquality
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 151, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_9_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 153, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_9_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 155, 27), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueList uses Python identifier valueList
    __valueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueList'), 'valueList', '__AbsentNamespace0_CTD_ANON_9_valueList', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 156, 27), )

    
    valueList = property(__valueList.value, __valueList.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_9_type', STD_ANON_7, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 159, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 159, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_9_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 168, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 168, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute likelihoodUnits uses Python identifier likelihoodUnits
    __likelihoodUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'likelihoodUnits'), 'likelihoodUnits', '__AbsentNamespace0_CTD_ANON_9_likelihoodUnits', likelihoodUnitsTypes)
    __likelihoodUnits._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 169, 20)
    __likelihoodUnits._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 169, 20)
    
    likelihoodUnits = property(__likelihoodUnits.value, __likelihoodUnits.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_9_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 170, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 170, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_9_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 171, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 171, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_9_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 172, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 172, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute applicable-categories uses Python identifier applicable_categories
    __applicable_categories = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applicable-categories'), 'applicable_categories', '__AbsentNamespace0_CTD_ANON_9_applicable_categories', pyxb.binding.datatypes.string)
    __applicable_categories._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 173, 20)
    __applicable_categories._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 173, 20)
    
    applicable_categories = property(__applicable_categories.value, __applicable_categories.set, None, None)

    
    # Attribute probability-type uses Python identifier probability_type
    __probability_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability-type'), 'probability_type', '__AbsentNamespace0_CTD_ANON_9_probability_type', probability_typeType)
    __probability_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 174, 20)
    __probability_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 174, 20)
    
    probability_type = property(__probability_type.value, __probability_type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueList.name() : __valueList
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __likelihoodUnits.name() : __likelihoodUnits,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __applicable_categories.name() : __applicable_categories,
        __probability_type.name() : __probability_type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 181, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_10_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 183, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_10_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 184, 24), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_10_type', STD_ANON_9, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 194, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 194, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_10_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 202, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 202, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_10_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 203, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 203, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_10_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 204, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 204, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 214, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_11_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 216, 34), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_11_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 217, 34), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_11_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 229, 30)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 229, 30)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_11_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 230, 30)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 230, 30)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_11_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 231, 30)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 231, 30)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 235, 26)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_12_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 237, 34), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_12_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 238, 34), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_12_type', STD_ANON_11, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 249, 30)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 249, 30)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_12_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 263, 30)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 263, 30)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_12_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 264, 30)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 264, 30)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_12_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 265, 30)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 265, 30)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_12_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 266, 30)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 266, 30)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 239, 38)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_CTD_ANON_13_upper_range', percentRange)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 242, 49)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 242, 49)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_CTD_ANON_13_lower_range', percentRange)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 243, 49)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 243, 49)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 288, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_14_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 290, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_14_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 292, 28), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueWithUncertainty uses Python identifier valueWithUncertainty
    __valueWithUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), 'valueWithUncertainty', '__AbsentNamespace0_CTD_ANON_14_valueWithUncertainty', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 293, 28), )

    
    valueWithUncertainty = property(__valueWithUncertainty.value, __valueWithUncertainty.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_14_type', STD_ANON_12, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 307, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 307, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_14_units', STD_ANON_13, unicode_default='knots')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 323, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 323, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_14_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 333, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 333, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_14_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 334, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 334, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_14_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 335, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 335, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueWithUncertainty.name() : __valueWithUncertainty
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 294, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_15_value', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 296, 40), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__AbsentNamespace0_CTD_ANON_15_uncertainty', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 298, 43), )

    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Element numberWithEquality uses Python identifier numberWithEquality
    __numberWithEquality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), 'numberWithEquality', '__AbsentNamespace0_CTD_ANON_15_numberWithEquality', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 299, 43), )

    
    numberWithEquality = property(__numberWithEquality.value, __numberWithEquality.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_15_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 302, 36)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 302, 36)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __uncertainty.name() : __uncertainty,
        __numberWithEquality.name() : __numberWithEquality
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 342, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_16_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 344, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_16_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 346, 28), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueWithUncertainty uses Python identifier valueWithUncertainty
    __valueWithUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), 'valueWithUncertainty', '__AbsentNamespace0_CTD_ANON_16_valueWithUncertainty', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 347, 28), )

    
    valueWithUncertainty = property(__valueWithUncertainty.value, __valueWithUncertainty.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_16_type', STD_ANON_14, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 361, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 361, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_16_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='degrees true')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 370, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 370, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_16_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 371, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 371, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_16_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 372, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 372, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_16_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 373, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 373, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueWithUncertainty.name() : __valueWithUncertainty
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 348, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_17_value', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 350, 40), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__AbsentNamespace0_CTD_ANON_17_uncertainty', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 352, 43), )

    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Element numberWithEquality uses Python identifier numberWithEquality
    __numberWithEquality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), 'numberWithEquality', '__AbsentNamespace0_CTD_ANON_17_numberWithEquality', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 353, 43), )

    
    numberWithEquality = property(__numberWithEquality.value, __numberWithEquality.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_17_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 356, 36)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 356, 36)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __uncertainty.name() : __uncertainty,
        __numberWithEquality.name() : __numberWithEquality
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 380, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_18_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 382, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_18_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 384, 28), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueWithUncertainty uses Python identifier valueWithUncertainty
    __valueWithUncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), 'valueWithUncertainty', '__AbsentNamespace0_CTD_ANON_18_valueWithUncertainty', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 385, 28), )

    
    valueWithUncertainty = property(__valueWithUncertainty.value, __valueWithUncertainty.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_18_type', STD_ANON_15, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 399, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 399, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_18_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 407, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 407, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_18_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 408, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 408, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_18_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 409, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 409, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_18_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 410, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 410, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueWithUncertainty.name() : __valueWithUncertainty
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 386, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_19_value', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 388, 40), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element uncertainty uses Python identifier uncertainty
    __uncertainty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uncertainty'), 'uncertainty', '__AbsentNamespace0_CTD_ANON_19_uncertainty', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 390, 43), )

    
    uncertainty = property(__uncertainty.value, __uncertainty.set, None, None)

    
    # Element numberWithEquality uses Python identifier numberWithEquality
    __numberWithEquality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), 'numberWithEquality', '__AbsentNamespace0_CTD_ANON_19_numberWithEquality', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 391, 43), )

    
    numberWithEquality = property(__numberWithEquality.value, __numberWithEquality.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_19_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 394, 36)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 394, 36)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __uncertainty.name() : __uncertainty,
        __numberWithEquality.name() : __numberWithEquality
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 417, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_20_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 419, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_20_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 420, 24), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_20_type', STD_ANON_16, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 431, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 431, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_20_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 440, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 440, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_20_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 441, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 441, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_20_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 442, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 442, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_20_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 443, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 443, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 421, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_CTD_ANON_21_upper_range', percentRange)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 424, 40)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 424, 40)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_CTD_ANON_21_lower_range', percentRange)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 425, 40)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 425, 40)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 450, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_22_name', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 452, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element weather-conditions uses Python identifier weather_conditions
    __weather_conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weather-conditions'), 'weather_conditions', '__AbsentNamespace0_CTD_ANON_22_weather_conditions', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 453, 24), )

    
    weather_conditions = property(__weather_conditions.value, __weather_conditions.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_22_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 567, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 567, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __weather_conditions.name() : __weather_conditions
    })
    _AttributeMap.update({
        __time_layout.name() : __time_layout
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 457, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element visibility uses Python identifier visibility
    __visibility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visibility'), 'visibility', '__AbsentNamespace0_CTD_ANON_23_visibility', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 459, 48), )

    
    visibility = property(__visibility.value, __visibility.set, None, None)

    
    # Attribute coverage uses Python identifier coverage
    __coverage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coverage'), 'coverage', '__AbsentNamespace0_CTD_ANON_23_coverage', STD_ANON_18)
    __coverage._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 477, 44)
    __coverage._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 477, 44)
    
    coverage = property(__coverage.value, __coverage.set, None, None)

    
    # Attribute weather-type uses Python identifier weather_type
    __weather_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'weather-type'), 'weather_type', '__AbsentNamespace0_CTD_ANON_23_weather_type', STD_ANON_19)
    __weather_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 498, 44)
    __weather_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 498, 44)
    
    weather_type = property(__weather_type.value, __weather_type.set, None, None)

    
    # Attribute intensity uses Python identifier intensity
    __intensity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'intensity'), 'intensity', '__AbsentNamespace0_CTD_ANON_23_intensity', STD_ANON_20)
    __intensity._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 527, 44)
    __intensity._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 527, 44)
    
    intensity = property(__intensity.value, __intensity.set, None, None)

    
    # Attribute additive uses Python identifier additive
    __additive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'additive'), 'additive', '__AbsentNamespace0_CTD_ANON_23_additive', STD_ANON_21)
    __additive._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 538, 44)
    __additive._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 538, 44)
    
    additive = property(__additive.value, __additive.set, None, None)

    
    # Attribute qualifier uses Python identifier qualifier
    __qualifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'qualifier'), 'qualifier', '__AbsentNamespace0_CTD_ANON_23_qualifier', STD_ANON_22)
    __qualifier._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 546, 48)
    __qualifier._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 546, 48)
    
    qualifier = property(__qualifier.value, __qualifier.set, None, None)

    _ElementMap.update({
        __visibility.name() : __visibility
    })
    _AttributeMap.update({
        __coverage.name() : __coverage,
        __weather_type.name() : __weather_type,
        __intensity.name() : __intensity,
        __additive.name() : __additive,
        __qualifier.name() : __qualifier
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 460, 52)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_24_units', STD_ANON_17, unicode_default='statute miles')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 463, 61)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 463, 61)
    
    units = property(__units.value, __units.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __units.name() : __units
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 574, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_25_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 576, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element icon-link uses Python identifier icon_link
    __icon_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'icon-link'), 'icon_link', '__AbsentNamespace0_CTD_ANON_25_icon_link', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 577, 24), )

    
    icon_link = property(__icon_link.value, __icon_link.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_25_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 579, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 579, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_25_type', STD_ANON_23, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 580, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 580, 20)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __icon_link.name() : __icon_link
    })
    _AttributeMap.update({
        __time_layout.name() : __time_layout,
        __type.name() : __type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 593, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_26_name', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 595, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element hazard-conditions uses Python identifier hazard_conditions
    __hazard_conditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazard-conditions'), 'hazard_conditions', '__AbsentNamespace0_CTD_ANON_26_hazard_conditions', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 596, 24), )

    
    hazard_conditions = property(__hazard_conditions.value, __hazard_conditions.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_26_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 702, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 702, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __hazard_conditions.name() : __hazard_conditions
    })
    _AttributeMap.update({
        __time_layout.name() : __time_layout
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 600, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element hazardTextURL uses Python identifier hazardTextURL
    __hazardTextURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazardTextURL'), 'hazardTextURL', '__AbsentNamespace0_CTD_ANON_27_hazardTextURL', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 602, 48), )

    
    hazardTextURL = property(__hazardTextURL.value, __hazardTextURL.set, None, None)

    
    # Element hazardIcon uses Python identifier hazardIcon
    __hazardIcon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazardIcon'), 'hazardIcon', '__AbsentNamespace0_CTD_ANON_27_hazardIcon', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 603, 48), )

    
    hazardIcon = property(__hazardIcon.value, __hazardIcon.set, None, None)

    
    # Attribute hazardCode uses Python identifier hazardCode
    __hazardCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hazardCode'), 'hazardCode', '__AbsentNamespace0_CTD_ANON_27_hazardCode', pyxb.binding.datatypes.string)
    __hazardCode._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 605, 44)
    __hazardCode._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 605, 44)
    
    hazardCode = property(__hazardCode.value, __hazardCode.set, None, None)

    
    # Attribute phenomena uses Python identifier phenomena
    __phenomena = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phenomena'), 'phenomena', '__AbsentNamespace0_CTD_ANON_27_phenomena', STD_ANON_24)
    __phenomena._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 606, 44)
    __phenomena._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 606, 44)
    
    phenomena = property(__phenomena.value, __phenomena.set, None, None)

    
    # Attribute significance uses Python identifier significance
    __significance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'significance'), 'significance', '__AbsentNamespace0_CTD_ANON_27_significance', STD_ANON_25)
    __significance._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 675, 44)
    __significance._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 675, 44)
    
    significance = property(__significance.value, __significance.set, None, None)

    
    # Attribute hazardType uses Python identifier hazardType
    __hazardType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hazardType'), 'hazardType', '__AbsentNamespace0_CTD_ANON_27_hazardType', STD_ANON_26)
    __hazardType._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 686, 44)
    __hazardType._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 686, 44)
    
    hazardType = property(__hazardType.value, __hazardType.set, None, None)

    
    # Attribute eventTrackingNumber uses Python identifier eventTrackingNumber
    __eventTrackingNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'eventTrackingNumber'), 'eventTrackingNumber', '__AbsentNamespace0_CTD_ANON_27_eventTrackingNumber', pyxb.binding.datatypes.integer)
    __eventTrackingNumber._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 694, 44)
    __eventTrackingNumber._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 694, 44)
    
    eventTrackingNumber = property(__eventTrackingNumber.value, __eventTrackingNumber.set, None, None)

    
    # Attribute headline uses Python identifier headline
    __headline = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'headline'), 'headline', '__AbsentNamespace0_CTD_ANON_27_headline', pyxb.binding.datatypes.string)
    __headline._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 695, 44)
    __headline._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 695, 44)
    
    headline = property(__headline.value, __headline.set, None, None)

    _ElementMap.update({
        __hazardTextURL.name() : __hazardTextURL,
        __hazardIcon.name() : __hazardIcon
    })
    _AttributeMap.update({
        __hazardCode.name() : __hazardCode,
        __phenomena.name() : __phenomena,
        __significance.name() : __significance,
        __hazardType.name() : __hazardType,
        __eventTrackingNumber.name() : __eventTrackingNumber,
        __headline.name() : __headline
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 709, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_28_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 711, 20), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'text'), 'text', '__AbsentNamespace0_CTD_ANON_28_text', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 712, 20), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_28_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 714, 17)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 714, 17)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute dataSource uses Python identifier dataSource
    __dataSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dataSource'), 'dataSource', '__AbsentNamespace0_CTD_ANON_28_dataSource', pyxb.binding.datatypes.string)
    __dataSource._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 715, 17)
    __dataSource._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 715, 17)
    
    dataSource = property(__dataSource.value, __dataSource.set, None, None)

    
    # Attribute wordGenerator uses Python identifier wordGenerator
    __wordGenerator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wordGenerator'), 'wordGenerator', '__AbsentNamespace0_CTD_ANON_28_wordGenerator', pyxb.binding.datatypes.string)
    __wordGenerator._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 716, 17)
    __wordGenerator._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 716, 17)
    
    wordGenerator = property(__wordGenerator.value, __wordGenerator.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __text.name() : __text
    })
    _AttributeMap.update({
        __time_layout.name() : __time_layout,
        __dataSource.name() : __dataSource,
        __wordGenerator.name() : __wordGenerator
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 723, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_29_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 725, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_29_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 726, 24), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_29_type', STD_ANON_27, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 728, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 728, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_29_units', STD_ANON_28, unicode_default='millibars')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 737, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 737, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_29_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 750, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 750, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_29_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 751, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 751, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_29_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 752, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 752, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 759, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_30_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 761, 24), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_30_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 763, 27), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element valueForRange uses Python identifier valueForRange
    __valueForRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueForRange'), 'valueForRange', '__AbsentNamespace0_CTD_ANON_30_valueForRange', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 764, 27), )

    
    valueForRange = property(__valueForRange.value, __valueForRange.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_30_type', STD_ANON_29, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 767, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 767, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_30_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 780, 20)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 780, 20)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute likelihoodUnits uses Python identifier likelihoodUnits
    __likelihoodUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'likelihoodUnits'), 'likelihoodUnits', '__AbsentNamespace0_CTD_ANON_30_likelihoodUnits', likelihoodUnitsTypes)
    __likelihoodUnits._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 781, 20)
    __likelihoodUnits._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 781, 20)
    
    likelihoodUnits = property(__likelihoodUnits.value, __likelihoodUnits.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_30_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 782, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 782, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_30_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 783, 20)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 783, 20)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_30_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 784, 20)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 784, 20)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute applicable-categories uses Python identifier applicable_categories
    __applicable_categories = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applicable-categories'), 'applicable_categories', '__AbsentNamespace0_CTD_ANON_30_applicable_categories', pyxb.binding.datatypes.string)
    __applicable_categories._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 785, 20)
    __applicable_categories._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 785, 20)
    
    applicable_categories = property(__applicable_categories.value, __applicable_categories.set, None, None)

    
    # Attribute probability-type uses Python identifier probability_type
    __probability_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability-type'), 'probability_type', '__AbsentNamespace0_CTD_ANON_30_probability_type', probability_typeType)
    __probability_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 786, 20)
    __probability_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 786, 20)
    
    probability_type = property(__probability_type.value, __probability_type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __valueForRange.name() : __valueForRange
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __likelihoodUnits.name() : __likelihoodUnits,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __applicable_categories.name() : __applicable_categories,
        __probability_type.name() : __probability_type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 793, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element waves uses Python identifier waves
    __waves = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'waves'), 'waves', '__AbsentNamespace0_CTD_ANON_31_waves', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 797, 32), )

    
    waves = property(__waves.value, __waves.set, None, None)

    
    # Element swell uses Python identifier swell
    __swell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'swell'), 'swell', '__AbsentNamespace0_CTD_ANON_31_swell', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 825, 32), )

    
    swell = property(__swell.value, __swell.set, None, None)

    
    # Element seas uses Python identifier seas
    __seas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'seas'), 'seas', '__AbsentNamespace0_CTD_ANON_31_seas', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 865, 28), )

    
    seas = property(__seas.value, __seas.set, None, None)

    
    # Element ice-coverage uses Python identifier ice_coverage
    __ice_coverage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ice-coverage'), 'ice_coverage', '__AbsentNamespace0_CTD_ANON_31_ice_coverage', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 891, 24), )

    
    ice_coverage = property(__ice_coverage.value, __ice_coverage.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_CTD_ANON_31_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 893, 20)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 893, 20)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    _ElementMap.update({
        __waves.name() : __waves,
        __swell.name() : __swell,
        __seas.name() : __seas,
        __ice_coverage.name() : __ice_coverage
    })
    _AttributeMap.update({
        __time_layout.name() : __time_layout
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 798, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_32_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 800, 44), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_32_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 801, 44), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_32_type', STD_ANON_30, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 803, 40)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 803, 40)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_32_units', STD_ANON_31, unicode_default='feet')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 811, 40)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 811, 40)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_32_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 819, 40)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 819, 40)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_32_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 820, 40)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 820, 40)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute period uses Python identifier period
    __period = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period'), 'period', '__AbsentNamespace0_CTD_ANON_32_period', pyxb.binding.datatypes.nonNegativeInteger)
    __period._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 821, 40)
    __period._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 821, 40)
    
    period = property(__period.value, __period.set, None, None)

    
    # Attribute steepness uses Python identifier steepness
    __steepness = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'steepness'), 'steepness', '__AbsentNamespace0_CTD_ANON_32_steepness', pyxb.binding.datatypes.nonNegativeInteger)
    __steepness._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 822, 40)
    __steepness._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 822, 40)
    
    steepness = property(__steepness.value, __steepness.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __period.name() : __period,
        __steepness.name() : __steepness
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 826, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_33_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 828, 44), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_33_value', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 830, 48), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element direction uses Python identifier direction
    __direction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'direction'), 'direction', '__AbsentNamespace0_CTD_ANON_33_direction', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 831, 48), )

    
    direction = property(__direction.value, __direction.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_33_type', STD_ANON_32, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 843, 40)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 843, 40)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_33_units', STD_ANON_33, unicode_default='feet')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 850, 40)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 850, 40)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_33_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 858, 40)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 858, 40)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_33_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 859, 40)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 859, 40)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    
    # Attribute period uses Python identifier period
    __period = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period'), 'period', '__AbsentNamespace0_CTD_ANON_33_period', pyxb.binding.datatypes.nonNegativeInteger)
    __period._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 860, 40)
    __period._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 860, 40)
    
    period = property(__period.value, __period.set, None, None)

    
    # Attribute steepness uses Python identifier steepness
    __steepness = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'steepness'), 'steepness', '__AbsentNamespace0_CTD_ANON_33_steepness', pyxb.binding.datatypes.nonNegativeInteger)
    __steepness._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 861, 40)
    __steepness._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 861, 40)
    
    steepness = property(__steepness.value, __steepness.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __direction.name() : __direction
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table,
        __period.name() : __period,
        __steepness.name() : __steepness
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 832, 52)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_CTD_ANON_34_upper_range', percentRange)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 835, 63)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 835, 63)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_CTD_ANON_34_lower_range', percentRange)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 836, 63)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 836, 63)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 866, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_35_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 868, 40), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_35_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 869, 40), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_35_type', STD_ANON_34, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 871, 36)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 871, 36)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_CTD_ANON_35_units', STD_ANON_35, unicode_default='feet')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 878, 36)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 878, 36)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_CTD_ANON_35_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 886, 36)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 886, 36)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_CTD_ANON_35_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 887, 36)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 887, 36)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })



# Complex type tempValType with content type SIMPLE
class tempValType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tempValType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.integer
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tempValType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 902, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.integer
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_tempValType_upper_range', STD_ANON_36)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 905, 16)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 905, 16)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_tempValType_lower_range', STD_ANON_37)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 912, 16)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 912, 16)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_tempValType_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 919, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 919, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'tempValType', tempValType)


# Complex type wspdValType with content type SIMPLE
class wspdValType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type wspdValType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wspdValType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 926, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_wspdValType_upper_range', pyxb.binding.datatypes.nonNegativeInteger)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 929, 16)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 929, 16)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_wspdValType_lower_range', pyxb.binding.datatypes.nonNegativeInteger)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 930, 16)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 930, 16)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_wspdValType_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 931, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 931, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'wspdValType', wspdValType)


# Complex type wdirValType with content type SIMPLE
class wdirValType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type wdirValType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'wdirValType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 938, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_wdirValType_upper_range', STD_ANON_38)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 941, 16)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 941, 16)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_wdirValType_lower_range', STD_ANON_39)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 948, 16)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 948, 16)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_wdirValType_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 955, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 955, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'wdirValType', wdirValType)


# Complex type percentageValType with content type SIMPLE
class percentageValType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type percentageValType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'percentageValType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 962, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_percentageValType_upper_range', percentRange)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 965, 16)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 965, 16)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_percentageValType_lower_range', percentRange)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 966, 16)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 966, 16)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_percentageValType_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 967, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 967, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'percentageValType', percentageValType)


# Complex type decimalValType with content type SIMPLE
class decimalValType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type decimalValType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'decimalValType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 974, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_decimalValType_upper_range', percentRange)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 977, 16)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 977, 16)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_decimalValType_lower_range', percentRange)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 978, 16)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 978, 16)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_decimalValType_type', dataSourceType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 979, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 979, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'decimalValType', decimalValType)


# Complex type anomalyType with content type ELEMENT_ONLY
class anomalyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type anomalyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'anomalyType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 986, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_anomalyType_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 988, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_anomalyType_value', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 989, 12), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_anomalyType_type', STD_ANON_40, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1000, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1000, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'units'), 'units', '__AbsentNamespace0_anomalyType_units', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __units._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1010, 8)
    __units._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1010, 8)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute time-layout uses Python identifier time_layout
    __time_layout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-layout'), 'time_layout', '__AbsentNamespace0_anomalyType_time_layout', time_layoutAttributeType, required=True)
    __time_layout._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1011, 8)
    __time_layout._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1011, 8)
    
    time_layout = property(__time_layout.value, __time_layout.set, None, None)

    
    # Attribute categorical-table uses Python identifier categorical_table
    __categorical_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'categorical-table'), 'categorical_table', '__AbsentNamespace0_anomalyType_categorical_table', pyxb.binding.datatypes.string)
    __categorical_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1012, 8)
    __categorical_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1012, 8)
    
    categorical_table = property(__categorical_table.value, __categorical_table.set, None, None)

    
    # Attribute conversion-table uses Python identifier conversion_table
    __conversion_table = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conversion-table'), 'conversion_table', '__AbsentNamespace0_anomalyType_conversion_table', pyxb.binding.datatypes.string)
    __conversion_table._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1013, 8)
    __conversion_table._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1013, 8)
    
    conversion_table = property(__conversion_table.value, __conversion_table.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
    _AttributeMap.update({
        __type.name() : __type,
        __units.name() : __units,
        __time_layout.name() : __time_layout,
        __categorical_table.name() : __categorical_table,
        __conversion_table.name() : __conversion_table
    })
Namespace.addCategoryObject('typeBinding', 'anomalyType', anomalyType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.nonNegativeInteger
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 990, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.nonNegativeInteger
    
    # Attribute upper-range uses Python identifier upper_range
    __upper_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper-range'), 'upper_range', '__AbsentNamespace0_CTD_ANON_36_upper_range', percentRange)
    __upper_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 993, 24)
    __upper_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 993, 24)
    
    upper_range = property(__upper_range.value, __upper_range.set, None, None)

    
    # Attribute lower-range uses Python identifier lower_range
    __lower_range = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower-range'), 'lower_range', '__AbsentNamespace0_CTD_ANON_36_lower_range', percentRange)
    __lower_range._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 994, 24)
    __lower_range._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 994, 24)
    
    lower_range = property(__lower_range.value, __lower_range.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upper_range.name() : __upper_range,
        __lower_range.name() : __lower_range
    })



# Complex type categoriesType with content type ELEMENT_ONLY
class categoriesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type categoriesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'categoriesType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1060, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_categoriesType_name', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1062, 10), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element categories-key uses Python identifier categories_key
    __categories_key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'categories-key'), 'categories_key', '__AbsentNamespace0_categoriesType_categories_key', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1063, 10), )

    
    categories_key = property(__categories_key.value, __categories_key.set, None, None)

    
    # Element valueList uses Python identifier valueList
    __valueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'valueList'), 'valueList', '__AbsentNamespace0_categoriesType_valueList', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1064, 10), )

    
    valueList = property(__valueList.value, __valueList.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_categoriesType_type', STD_ANON_41, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1066, 7)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1066, 7)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute probability-type uses Python identifier probability_type
    __probability_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability-type'), 'probability_type', '__AbsentNamespace0_categoriesType_probability_type', probability_typeType)
    __probability_type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1074, 7)
    __probability_type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1074, 7)
    
    probability_type = property(__probability_type.value, __probability_type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __categories_key.name() : __categories_key,
        __valueList.name() : __valueList
    })
    _AttributeMap.update({
        __type.name() : __type,
        __probability_type.name() : __probability_type
    })
Namespace.addCategoryObject('typeBinding', 'categoriesType', categoriesType)


# Complex type uncertaintyType with content type ELEMENT_ONLY
class uncertaintyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type uncertaintyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uncertaintyType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1115, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element error uses Python identifier error
    __error = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'error'), 'error', '__AbsentNamespace0_uncertaintyType_error', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1117, 10), )

    
    error = property(__error.value, __error.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_uncertaintyType_type', STD_ANON_42, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1127, 7)
    __type._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1127, 7)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __error.name() : __error
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'uncertaintyType', uncertaintyType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.decimal
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1118, 13)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.decimal
    
    # Attribute qualifier uses Python identifier qualifier
    __qualifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'qualifier'), 'qualifier', '__AbsentNamespace0_CTD_ANON_37_qualifier', qualifierType, unicode_default='+/-')
    __qualifier._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1121, 22)
    __qualifier._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1121, 22)
    
    qualifier = property(__qualifier.value, __qualifier.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __qualifier.name() : __qualifier
    })



# Complex type time-layoutElementType with content type ELEMENT_ONLY
class time_layoutElementType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type time-layoutElementType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'time-layoutElementType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 18, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element layout-key uses Python identifier layout_key
    __layout_key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'layout-key'), 'layout_key', '__AbsentNamespace0_time_layoutElementType_layout_key', False, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 20, 12), )

    
    layout_key = property(__layout_key.value, __layout_key.set, None, None)

    
    # Element start-valid-time uses Python identifier start_valid_time
    __start_valid_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'start-valid-time'), 'start_valid_time', '__AbsentNamespace0_time_layoutElementType_start_valid_time', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 22, 16), )

    
    start_valid_time = property(__start_valid_time.value, __start_valid_time.set, None, None)

    
    # Element end-valid-time uses Python identifier end_valid_time
    __end_valid_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'end-valid-time'), 'end_valid_time', '__AbsentNamespace0_time_layoutElementType_end_valid_time', True, pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 23, 16), )

    
    end_valid_time = property(__end_valid_time.value, __end_valid_time.set, None, None)

    
    # Attribute time-coordinate uses Python identifier time_coordinate
    __time_coordinate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'time-coordinate'), 'time_coordinate', '__AbsentNamespace0_time_layoutElementType_time_coordinate', time_coordinateType, required=True)
    __time_coordinate._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 26, 8)
    __time_coordinate._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 26, 8)
    
    time_coordinate = property(__time_coordinate.value, __time_coordinate.set, None, None)

    
    # Attribute summarization uses Python identifier summarization
    __summarization = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'summarization'), 'summarization', '__AbsentNamespace0_time_layoutElementType_summarization', summarizationType)
    __summarization._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 27, 8)
    __summarization._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 27, 8)
    
    summarization = property(__summarization.value, __summarization.set, None, None)

    _ElementMap.update({
        __layout_key.name() : __layout_key,
        __start_valid_time.name() : __start_valid_time,
        __end_valid_time.name() : __end_valid_time
    })
    _AttributeMap.update({
        __time_coordinate.name() : __time_coordinate,
        __summarization.name() : __summarization
    })
Namespace.addCategoryObject('typeBinding', 'time-layoutElementType', time_layoutElementType)


# Complex type valueListType with content type SIMPLE
class valueListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type valueListType with content type SIMPLE"""
    _TypeDefinition = numberValueListType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'valueListType')
    _XSDLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1038, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is numberValueListType
    
    # Attribute median uses Python identifier median
    __median = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'median'), 'median', '__AbsentNamespace0_valueListType_median', pyxb.binding.datatypes.decimal)
    __median._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1041, 13)
    __median._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1041, 13)
    
    median = property(__median.value, __median.set, None, None)

    
    # Attribute confidenceInterval50 uses Python identifier confidenceInterval50
    __confidenceInterval50 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'confidenceInterval50'), 'confidenceInterval50', '__AbsentNamespace0_valueListType_confidenceInterval50', pyxb.binding.datatypes.decimal)
    __confidenceInterval50._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1042, 13)
    __confidenceInterval50._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1042, 13)
    
    confidenceInterval50 = property(__confidenceInterval50.value, __confidenceInterval50.set, None, None)

    
    # Attribute confidenceInterval80 uses Python identifier confidenceInterval80
    __confidenceInterval80 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'confidenceInterval80'), 'confidenceInterval80', '__AbsentNamespace0_valueListType_confidenceInterval80', pyxb.binding.datatypes.decimal)
    __confidenceInterval80._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1043, 13)
    __confidenceInterval80._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1043, 13)
    
    confidenceInterval80 = property(__confidenceInterval80.value, __confidenceInterval80.set, None, None)

    
    # Attribute skew80 uses Python identifier skew80
    __skew80 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skew80'), 'skew80', '__AbsentNamespace0_valueListType_skew80', pyxb.binding.datatypes.decimal)
    __skew80._DeclarationLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1044, 13)
    __skew80._UseLocation = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1044, 13)
    
    skew80 = property(__skew80.value, __skew80.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __median.name() : __median,
        __confidenceInterval50.name() : __confidenceInterval50,
        __confidenceInterval80.name() : __confidenceInterval80,
        __skew80.name() : __skew80
    })
Namespace.addCategoryObject('typeBinding', 'valueListType', valueListType)


dwml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dwml'), CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 51, 3))
Namespace.addCategoryObject('elementBinding', dwml.name().localName(), dwml)

lt = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lt'), numberValueListType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1148, 4))
Namespace.addCategoryObject('elementBinding', lt.name().localName(), lt)

le = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'le'), numberValueListType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1149, 4))
Namespace.addCategoryObject('elementBinding', le.name().localName(), le)

gt = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gt'), numberValueListType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1150, 4))
Namespace.addCategoryObject('elementBinding', gt.name().localName(), gt)

ge = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ge'), numberValueListType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1151, 4))
Namespace.addCategoryObject('elementBinding', ge.name().localName(), ge)

eq = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eq'), numberValueListType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1152, 4))
Namespace.addCategoryObject('elementBinding', eq.name().localName(), eq)



locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location-key'), pyxb.binding.datatypes.string, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 20, 11)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 21, 11)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), pointType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 23, 14)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'nws-zone'), nws_zoneType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 24, 14)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), areaType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 25, 14)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'city'), cityType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 27, 11)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area-description'), pyxb.binding.datatypes.string, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 28, 11)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), heightType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 30, 14)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'level'), levelType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 31, 14)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'layer'), layerType, scope=locationType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 32, 14)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 21, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 23, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 24, 14))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 25, 14))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 27, 11))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 28, 11))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 30, 14))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 31, 14))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 32, 14))
    counters.add(cc_8)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'location-key')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 20, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 21, 11))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 23, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'nws-zone')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 24, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 25, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'city')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 27, 11))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'area-description')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 28, 11))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 30, 14))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'level')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 31, 14))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(None, 'layer')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 32, 14))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
locationType._Automaton = _BuildAutomaton()




headType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'product'), productType, scope=headType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 16, 12)))

headType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'source'), sourceType, scope=headType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 17, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(headType._UseForTag(pyxb.namespace.ExpandedName(None, 'product')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(headType._UseForTag(pyxb.namespace.ExpandedName(None, 'source')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 17, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
headType._Automaton = _BuildAutomaton_()




sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'more-information'), pyxb.binding.datatypes.anyURI, scope=sourceType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 60, 10)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'production-center'), production_centerType, scope=sourceType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 61, 10)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'disclaimer'), pyxb.binding.datatypes.anyURI, scope=sourceType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 62, 10)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'credit'), pyxb.binding.datatypes.anyURI, scope=sourceType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 63, 10)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'credit-logo'), pyxb.binding.datatypes.anyURI, scope=sourceType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 64, 10)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'feedback'), pyxb.binding.datatypes.anyURI, scope=sourceType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 65, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(None, 'more-information')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 60, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 61, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(None, 'production-center')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 61, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 62, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(None, 'disclaimer')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 62, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 63, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(None, 'credit')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 63, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 64, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(None, 'credit-logo')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 64, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 65, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(None, 'feedback')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 65, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 61, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 62, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 63, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 64, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 65, 10))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 59, 7)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
sourceType._Automaton = _BuildAutomaton_2()




production_centerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sub-center'), pyxb.binding.datatypes.string, scope=production_centerType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 71, 10)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 71, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(production_centerType._UseForTag(pyxb.namespace.ExpandedName(None, 'sub-center')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 71, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
production_centerType._Automaton = _BuildAutomaton_9()




parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'categories'), categoriesType, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 26, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'temperature'), CTD_ANON_5, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 30, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'precipitation'), CTD_ANON_7, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 93, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'probability-of-precipitation'), CTD_ANON_9, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 150, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fire-weather'), CTD_ANON_10, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 180, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'convective-hazard'), CTD_ANON, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 210, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'climate-anomaly'), CTD_ANON_, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 275, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'wind-speed'), CTD_ANON_14, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 287, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'direction'), CTD_ANON_16, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 341, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cloud-amount'), CTD_ANON_18, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 379, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'humidity'), CTD_ANON_20, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 416, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weather'), CTD_ANON_22, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 449, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'conditions-icon'), CTD_ANON_25, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 573, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazards'), CTD_ANON_26, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 592, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'wordedForecast'), CTD_ANON_28, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 708, 11)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pressure'), CTD_ANON_29, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 722, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'probabilisticCondition'), CTD_ANON_30, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 758, 12)))

parametersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'water-state'), CTD_ANON_31, scope=parametersType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 792, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 26, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 30, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 93, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 150, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 180, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 210, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 275, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 287, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 341, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 379, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 416, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 449, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 573, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 592, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 708, 11))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 722, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 758, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 792, 12))
    counters.add(cc_17)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'categories')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 26, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'temperature')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 30, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'precipitation')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 93, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'probability-of-precipitation')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 150, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'fire-weather')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 180, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'convective-hazard')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 210, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'climate-anomaly')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 275, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'wind-speed')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 287, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'direction')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 341, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'cloud-amount')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 379, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'humidity')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 416, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'weather')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 449, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'conditions-icon')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 573, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'hazards')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 592, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'wordedForecast')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 708, 11))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'pressure')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 722, 12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'probabilisticCondition')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 758, 12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(parametersType._UseForTag(pyxb.namespace.ExpandedName(None, 'water-state')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 792, 12))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
parametersType._Automaton = _BuildAutomaton_10()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outlook'), CTD_ANON_11, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 213, 23)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'severe-component'), CTD_ANON_12, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 234, 23)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 213, 23))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=8, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 234, 23))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'outlook')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 213, 23))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'severe-component')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 234, 23))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_11()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weekly'), anomalyType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 278, 24)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'monthly'), anomalyType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 279, 24)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'seasonal'), anomalyType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 280, 24)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=4, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 278, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=4, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 279, 24))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=4, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 280, 24))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'weekly')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 278, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'monthly')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 279, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'seasonal')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 280, 24))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_12()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), CTD_ANON_23, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 456, 36)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 456, 36))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 456, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_13()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazard'), CTD_ANON_27, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 599, 36)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 599, 36))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'hazard')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 599, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_14()




valueForRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lt'), numberValueListType, scope=valueForRangeType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1148, 4)))

valueForRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'le'), numberValueListType, scope=valueForRangeType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1149, 4)))

valueForRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gt'), numberValueListType, scope=valueForRangeType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1150, 4)))

valueForRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ge'), numberValueListType, scope=valueForRangeType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1151, 4)))

valueForRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eq'), numberValueListType, scope=valueForRangeType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1152, 4)))

valueForRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), percentageValType, nillable=pyxb.binding.datatypes.boolean(1), scope=valueForRangeType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1158, 8)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1158, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1160, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1161, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1164, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1165, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1168, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(valueForRangeType._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1158, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(valueForRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gt')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1160, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(valueForRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ge')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1161, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(valueForRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lt')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1164, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(valueForRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'le')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1165, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(valueForRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eq')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1168, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
valueForRangeType._Automaton = _BuildAutomaton_15()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'head'), headType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 55, 15)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'data'), dataType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 56, 15)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minResolution'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 88, 15)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'latLonList'), latLonListType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 89, 15)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cityNameList'), cityNameListType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 90, 15)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 88, 15))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 90, 15))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'head')), pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 55, 15))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'data')), pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 56, 15))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'minResolution')), pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 88, 15))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'latLonList')), pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 89, 15))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'cityNameList')), pyxb.utils.utility.Location('http://www.weather.gov/forecasts/xml/DWMLgen/schema/DWML.xsd', 90, 15))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_16()




areaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'circle'), circleType, scope=areaType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 63, 13)))

areaType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rectangle'), rectangleType, scope=areaType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 64, 13)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(areaType._UseForTag(pyxb.namespace.ExpandedName(None, 'circle')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 63, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(areaType._UseForTag(pyxb.namespace.ExpandedName(None, 'rectangle')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 64, 13))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
areaType._Automaton = _BuildAutomaton_17()




circleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), pointType, scope=circleType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 78, 13)))

circleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), radiusType, scope=circleType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 79, 13)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(circleType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 78, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(circleType._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 79, 13))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
circleType._Automaton = _BuildAutomaton_18()




rectangleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), pointType, scope=rectangleType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 98, 13)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=4, max=4, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 98, 13))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(rectangleType._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/location.xsd', 98, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
rectangleType._Automaton = _BuildAutomaton_19()




productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=productType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 23, 10)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'field'), fieldType, scope=productType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 24, 10)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'category'), categoryType, scope=productType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 25, 10)))

productType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'creation-date'), creation_dateType, scope=productType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 26, 10)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 23, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 23, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 24, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'field')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 24, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 25, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'category')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 25, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(productType._UseForTag(pyxb.namespace.ExpandedName(None, 'creation-date')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 26, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 23, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 24, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 25, 10))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/meta_data.xsd', 22, 7)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
productType._Automaton = _BuildAutomaton_20()




dataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), locationType, scope=dataType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 26, 12)))

dataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'moreWeatherInformation'), moreWeatherInformationType, scope=dataType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 27, 12)))

dataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time-layout'), time_layoutElementType, scope=dataType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 28, 12)))

dataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameters'), parametersType, scope=dataType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 29, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 26, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataType._UseForTag(pyxb.namespace.ExpandedName(None, 'moreWeatherInformation')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 27, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(dataType._UseForTag(pyxb.namespace.ExpandedName(None, 'time-layout')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 28, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dataType._UseForTag(pyxb.namespace.ExpandedName(None, 'parameters')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/ndfd_data.xsd', 29, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
dataType._Automaton = _BuildAutomaton_25()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 33, 24)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), tempValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 35, 28)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueList'), valueListType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 36, 28)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), CTD_ANON_6, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 37, 28)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 33, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 35, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 36, 28))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 37, 28))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 33, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 35, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'valueList')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 36, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 37, 28))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_26()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), tempValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 40, 40)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uncertainty'), uncertaintyType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 42, 43)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), numberWithEqualityType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 43, 43)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 40, 40))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 42, 43))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 43, 43))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 40, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'uncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 42, 43))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'numberWithEquality')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 43, 43))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_27()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 96, 24)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), decimalValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 98, 28)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueList'), valueListType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 99, 28)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), CTD_ANON_8, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 100, 28)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 96, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 98, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 99, 28))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 100, 28))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 96, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 98, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'valueList')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 99, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 100, 28))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_28()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), decimalValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 103, 40)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uncertainty'), uncertaintyType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 105, 43)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), numberWithEqualityType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 106, 43)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 105, 43))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 106, 43))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 103, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'uncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 105, 43))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'numberWithEquality')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 106, 43))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_29()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 153, 24)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), percentageValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 155, 27)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueList'), valueListType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 156, 27)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 153, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 155, 27))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 156, 27))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 153, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 155, 27))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'valueList')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 156, 27))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_30()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 183, 24)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), STD_ANON_8, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 184, 24)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 183, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 184, 24))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 183, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 184, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_31()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 216, 34)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), STD_ANON_10, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 217, 34)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 216, 34))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 217, 34))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 216, 34))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 217, 34))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_32()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 237, 34)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), CTD_ANON_13, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 238, 34)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 237, 34))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 238, 34))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 237, 34))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 238, 34))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_33()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 290, 24)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), wspdValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 292, 28)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), CTD_ANON_15, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 293, 28)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 290, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 292, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 293, 28))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 290, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 292, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 293, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_34()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), wspdValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 296, 40)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uncertainty'), uncertaintyType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 298, 43)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), numberWithEqualityType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 299, 43)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 296, 40))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 298, 43))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 299, 43))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 296, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'uncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 298, 43))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'numberWithEquality')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 299, 43))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_35()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 344, 24)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), wdirValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_16, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 346, 28)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), CTD_ANON_17, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_16, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 347, 28)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 344, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 346, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 347, 28))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 344, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 346, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 347, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_36()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), wdirValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 350, 40)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uncertainty'), uncertaintyType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 352, 43)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), numberWithEqualityType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 353, 43)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 350, 40))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 352, 43))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 353, 43))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 350, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'uncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 352, 43))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'numberWithEquality')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 353, 43))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_37()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 382, 24)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), percentageValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 384, 28)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty'), CTD_ANON_19, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 385, 28)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 382, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 384, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 385, 28))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 382, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 384, 28))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'valueWithUncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 385, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_38()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), percentageValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 388, 40)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uncertainty'), uncertaintyType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 390, 43)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numberWithEquality'), numberWithEqualityType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 391, 43)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 388, 40))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 390, 43))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 391, 43))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 388, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'uncertainty')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 390, 43))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'numberWithEquality')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 391, 43))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_39()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 419, 24)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), CTD_ANON_21, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_20, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 420, 24)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 419, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 420, 24))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 419, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 420, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_40()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 452, 24)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weather-conditions'), CTD_ANON_2, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 453, 24)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 452, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 452, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'weather-conditions')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 453, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_41()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visibility'), CTD_ANON_24, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_23, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 459, 48)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 459, 48))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(None, 'visibility')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 459, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_42()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 576, 24)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'icon-link'), pyxb.binding.datatypes.anyURI, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_25, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 577, 24)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 576, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 576, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, 'icon-link')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 577, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_43()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 595, 24)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazard-conditions'), CTD_ANON_3, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_26, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 596, 24)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 595, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 595, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(None, 'hazard-conditions')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 596, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_44()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazardTextURL'), pyxb.binding.datatypes.anyURI, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_27, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 602, 48)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazardIcon'), pyxb.binding.datatypes.anyURI, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_27, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 603, 48)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 602, 48))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 603, 48))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, 'hazardTextURL')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 602, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(None, 'hazardIcon')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 603, 48))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_45()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 711, 20)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'text'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 712, 20)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 711, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 712, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 711, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(None, 'text')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 712, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_46()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 725, 24)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), decimalValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_29, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 726, 24)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 725, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 726, 24))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 725, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 726, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_47()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 761, 24)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), percentageValType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_30, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 763, 27)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueForRange'), valueForRangeType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_30, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 764, 27)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 761, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 763, 27))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 764, 27))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 761, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 763, 27))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'valueForRange')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 764, 27))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_48()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'waves'), CTD_ANON_32, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_31, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 797, 32)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'swell'), CTD_ANON_33, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_31, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 825, 32)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'seas'), CTD_ANON_35, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 865, 28)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ice-coverage'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 891, 24)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 797, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 825, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 865, 28))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 891, 24))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'waves')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 797, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'swell')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 825, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'seas')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 865, 28))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'ice-coverage')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 891, 24))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_49()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 800, 44)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.nonNegativeInteger, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_32, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 801, 44)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 800, 44))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 800, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 801, 44))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_50()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 828, 44)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_33, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 830, 48)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'direction'), CTD_ANON_34, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 831, 48)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 828, 44))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 830, 48))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 831, 48))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 828, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 830, 48))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'direction')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 831, 48))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_51()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 868, 40)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), pyxb.binding.datatypes.nonNegativeInteger, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_35, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 869, 40)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 868, 40))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 868, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 869, 40))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_52()




anomalyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=anomalyType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 988, 12)))

anomalyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), CTD_ANON_36, nillable=pyxb.binding.datatypes.boolean(1), scope=anomalyType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 989, 12)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 988, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 989, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(anomalyType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 988, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(anomalyType._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 989, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
anomalyType._Automaton = _BuildAutomaton_53()




categoriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=categoriesType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1062, 10)))

categoriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'categories-key'), pyxb.binding.datatypes.string, scope=categoriesType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1063, 10)))

categoriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'valueList'), valueListType, scope=categoriesType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1064, 10)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1062, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1064, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(categoriesType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1062, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(categoriesType._UseForTag(pyxb.namespace.ExpandedName(None, 'categories-key')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1063, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(categoriesType._UseForTag(pyxb.namespace.ExpandedName(None, 'valueList')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1064, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
categoriesType._Automaton = _BuildAutomaton_54()




uncertaintyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'error'), CTD_ANON_37, scope=uncertaintyType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1117, 10)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1117, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(uncertaintyType._UseForTag(pyxb.namespace.ExpandedName(None, 'error')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/parameters.xsd', 1117, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
uncertaintyType._Automaton = _BuildAutomaton_55()




time_layoutElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'layout-key'), layout_keyType, scope=time_layoutElementType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 20, 12)))

time_layoutElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'start-valid-time'), start_valid_timeType, scope=time_layoutElementType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 22, 16)))

time_layoutElementType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'end-valid-time'), pyxb.binding.datatypes.dateTime, scope=time_layoutElementType, location=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 23, 16)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 23, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(time_layoutElementType._UseForTag(pyxb.namespace.ExpandedName(None, 'layout-key')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 20, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(time_layoutElementType._UseForTag(pyxb.namespace.ExpandedName(None, 'start-valid-time')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 22, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(time_layoutElementType._UseForTag(pyxb.namespace.ExpandedName(None, 'end-valid-time')), pyxb.utils.utility.Location('http://graphical.weather.gov/xml/DWMLgen/schema/time_layout.xsd', 23, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
time_layoutElementType._Automaton = _BuildAutomaton_56()

