# ./wadl.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:05f5b6da780284c094d893a53505b7c6c26136a6
# Generated 2013-04-03 15:21:42.322077 by PyXB version 1.2.1
# Namespace http://wadl.dev.java.net/2009/02

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dbbe028f-9cac-11e2-aaf2-406c8f442187')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.xml_

Namespace = pyxb.namespace.NamespaceForURI(u'http://wadl.dev.java.net/2009/02', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
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
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# List simple type: {http://wadl.dev.java.net/2009/02}resource_type_list
# superclasses pyxb.binding.datatypes.anySimpleType
class resource_type_list (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.anyURI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'resource_type_list')
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 87, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.anyURI
resource_type_list._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'resource_type_list', resource_type_list)

# Atomic simple type: {http://wadl.dev.java.net/2009/02}HTTPMethods
class HTTPMethods (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HTTPMethods')
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 129, 2)
    _Documentation = None
HTTPMethods._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HTTPMethods, enum_prefix=None)
HTTPMethods.GET = HTTPMethods._CF_enumeration.addEnumeration(unicode_value=u'GET', tag=u'GET')
HTTPMethods.POST = HTTPMethods._CF_enumeration.addEnumeration(unicode_value=u'POST', tag=u'POST')
HTTPMethods.PUT = HTTPMethods._CF_enumeration.addEnumeration(unicode_value=u'PUT', tag=u'PUT')
HTTPMethods.HEAD = HTTPMethods._CF_enumeration.addEnumeration(unicode_value=u'HEAD', tag=u'HEAD')
HTTPMethods.DELETE = HTTPMethods._CF_enumeration.addEnumeration(unicode_value=u'DELETE', tag=u'DELETE')
HTTPMethods._InitializeFacetMap(HTTPMethods._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'HTTPMethods', HTTPMethods)

# List simple type: {http://wadl.dev.java.net/2009/02}uriList
# superclasses pyxb.binding.datatypes.anySimpleType
class uriList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.anyURI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uriList')
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 178, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.anyURI
uriList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uriList', uriList)

# List simple type: {http://wadl.dev.java.net/2009/02}statusCodeList
# superclasses pyxb.binding.datatypes.anySimpleType
class statusCodeList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.unsignedInt."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'statusCodeList')
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 199, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.unsignedInt
statusCodeList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'statusCodeList', statusCodeList)

# Atomic simple type: {http://wadl.dev.java.net/2009/02}ParamStyle
class ParamStyle (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ParamStyle')
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 203, 2)
    _Documentation = None
ParamStyle._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ParamStyle, enum_prefix=None)
ParamStyle.plain = ParamStyle._CF_enumeration.addEnumeration(unicode_value=u'plain', tag=u'plain')
ParamStyle.query = ParamStyle._CF_enumeration.addEnumeration(unicode_value=u'query', tag=u'query')
ParamStyle.matrix = ParamStyle._CF_enumeration.addEnumeration(unicode_value=u'matrix', tag=u'matrix')
ParamStyle.header = ParamStyle._CF_enumeration.addEnumeration(unicode_value=u'header', tag=u'header')
ParamStyle.template = ParamStyle._CF_enumeration.addEnumeration(unicode_value=u'template', tag=u'template')
ParamStyle._InitializeFacetMap(ParamStyle._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ParamStyle', ParamStyle)

# Union simple type: {http://wadl.dev.java.net/2009/02}Method
# superclasses pyxb.binding.datatypes.anySimpleType
class Method (pyxb.binding.basis.STD_union):

    """Simple type that is a union of HTTPMethods, pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Method')
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 125, 2)
    _Documentation = None

    _MemberTypes = ( HTTPMethods, pyxb.binding.datatypes.NMTOKEN, )
Method._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Method)
Method._CF_pattern = pyxb.binding.facets.CF_pattern()
Method.GET = u'GET'                               # originally HTTPMethods.GET
Method.POST = u'POST'                             # originally HTTPMethods.POST
Method.PUT = u'PUT'                               # originally HTTPMethods.PUT
Method.HEAD = u'HEAD'                             # originally HTTPMethods.HEAD
Method.DELETE = u'DELETE'                         # originally HTTPMethods.DELETE
Method._InitializeFacetMap(Method._CF_enumeration,
   Method._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Method', Method)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 12, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}grammars uses Python identifier grammars
    __grammars = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'grammars'), 'grammars', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902grammars', False, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 42, 2), )

    
    grammars = property(__grammars.value, __grammars.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}resources uses Python identifier resources
    __resources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resources'), 'resources', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902resources', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 53, 2), )

    
    resources = property(__resources.value, __resources.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}resource_type uses Python identifier resource_type
    __resource_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resource_type'), 'resource_type', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902resource_type', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 91, 2), )

    
    resource_type = property(__resource_type.value, __resource_type.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'method'), 'method', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902method', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2), )

    
    method = property(__method.value, __method.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}representation uses Python identifier representation
    __representation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'representation'), 'representation', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902representation', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2), )

    
    representation = property(__representation.value, __representation.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwadl_dev_java_net200902_CTD_ANON_httpwadl_dev_java_net200902param', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2), )

    
    param = property(__param.value, __param.set, None, None)

    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __grammars.name() : __grammars,
        __resources.name() : __resources,
        __resource_type.name() : __resource_type,
        __method.name() : __method,
        __representation.name() : __representation,
        __param.name() : __param
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type MIXED
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 31, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwadl_dev_java_net200902_CTD_ANON__httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 37, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__httpwadl_dev_java_net200902_CTD_ANON__title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 36, 6)
    __title._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 36, 6)
    
    title = property(__title.value, __title.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __lang.name() : __lang,
        __title.name() : __title
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 43, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_2_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'include'), 'include', '__httpwadl_dev_java_net200902_CTD_ANON_2_httpwadl_dev_java_net200902include', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 139, 2), )

    
    include = property(__include.value, __include.set, None, None)

    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __include.name() : __include
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 54, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_3_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resource'), 'resource', '__httpwadl_dev_java_net200902_CTD_ANON_3_httpwadl_dev_java_net200902resource', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2), )

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Attribute base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'base'), 'base', '__httpwadl_dev_java_net200902_CTD_ANON_3_base', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 61, 6)
    __base._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 61, 6)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __resource.name() : __resource
    }
    _AttributeMap = {
        __base.name() : __base
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 92, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_4_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resource'), 'resource', '__httpwadl_dev_java_net200902_CTD_ANON_4_httpwadl_dev_java_net200902resource', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2), )

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'method'), 'method', '__httpwadl_dev_java_net200902_CTD_ANON_4_httpwadl_dev_java_net200902method', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2), )

    
    method = property(__method.value, __method.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwadl_dev_java_net200902_CTD_ANON_4_httpwadl_dev_java_net200902param', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwadl_dev_java_net200902_CTD_ANON_4_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 103, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 103, 6)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __resource.name() : __resource,
        __method.name() : __method,
        __param.name() : __param
    }
    _AttributeMap = {
        __id.name() : __id
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 140, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_5_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwadl_dev_java_net200902_CTD_ANON_5_href', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 144, 6)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 144, 6)
    
    href = property(__href.value, __href.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))

    _ElementMap = {
        __doc.name() : __doc
    }
    _AttributeMap = {
        __href.name() : __href
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 150, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_6_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}representation uses Python identifier representation
    __representation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'representation'), 'representation', '__httpwadl_dev_java_net200902_CTD_ANON_6_httpwadl_dev_java_net200902representation', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2), )

    
    representation = property(__representation.value, __representation.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwadl_dev_java_net200902_CTD_ANON_6_httpwadl_dev_java_net200902param', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2), )

    
    param = property(__param.value, __param.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __representation.name() : __representation,
        __param.name() : __param
    }
    _AttributeMap = {
        
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 237, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_7_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpwadl_dev_java_net200902_CTD_ANON_7_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 243, 6)
    __value._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 243, 6)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute mediaType uses Python identifier mediaType
    __mediaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mediaType'), 'mediaType', '__httpwadl_dev_java_net200902_CTD_ANON_7_mediaType', pyxb.binding.datatypes.string)
    __mediaType._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 244, 6)
    __mediaType._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 244, 6)
    
    mediaType = property(__mediaType.value, __mediaType.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc
    }
    _AttributeMap = {
        __value.name() : __value,
        __mediaType.name() : __mediaType
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 250, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_8_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Attribute resource_type uses Python identifier resource_type
    __resource_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'resource_type'), 'resource_type', '__httpwadl_dev_java_net200902_CTD_ANON_8_resource_type', pyxb.binding.datatypes.anyURI)
    __resource_type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 256, 6)
    __resource_type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 256, 6)
    
    resource_type = property(__resource_type.value, __resource_type.set, None, None)

    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rel'), 'rel', '__httpwadl_dev_java_net200902_CTD_ANON_8_rel', pyxb.binding.datatypes.token)
    __rel._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 257, 6)
    __rel._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 257, 6)
    
    rel = property(__rel.value, __rel.set, None, None)

    
    # Attribute rev uses Python identifier rev
    __rev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rev'), 'rev', '__httpwadl_dev_java_net200902_CTD_ANON_8_rev', pyxb.binding.datatypes.token)
    __rev._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 258, 6)
    __rev._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 258, 6)
    
    rev = property(__rev.value, __rev.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc
    }
    _AttributeMap = {
        __resource_type.name() : __resource_type,
        __rel.name() : __rel,
        __rev.name() : __rev
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 67, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_9_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resource'), 'resource', '__httpwadl_dev_java_net200902_CTD_ANON_9_httpwadl_dev_java_net200902resource', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2), )

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'method'), 'method', '__httpwadl_dev_java_net200902_CTD_ANON_9_httpwadl_dev_java_net200902method', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2), )

    
    method = property(__method.value, __method.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwadl_dev_java_net200902_CTD_ANON_9_httpwadl_dev_java_net200902param', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwadl_dev_java_net200902_CTD_ANON_9_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 78, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 78, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwadl_dev_java_net200902_CTD_ANON_9_type', resource_type_list)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 79, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 79, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute queryType uses Python identifier queryType
    __queryType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'queryType'), 'queryType', '__httpwadl_dev_java_net200902_CTD_ANON_9_queryType', pyxb.binding.datatypes.string, unicode_default=u'application/x-www-form-urlencoded')
    __queryType._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 80, 6)
    __queryType._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 80, 6)
    
    queryType = property(__queryType.value, __queryType.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'path'), 'path', '__httpwadl_dev_java_net200902_CTD_ANON_9_path', pyxb.binding.datatypes.string)
    __path._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 82, 6)
    __path._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 82, 6)
    
    path = property(__path.value, __path.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __resource.name() : __resource,
        __method.name() : __method,
        __param.name() : __param
    }
    _AttributeMap = {
        __id.name() : __id,
        __type.name() : __type,
        __queryType.name() : __queryType,
        __path.name() : __path
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 164, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_10_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}representation uses Python identifier representation
    __representation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'representation'), 'representation', '__httpwadl_dev_java_net200902_CTD_ANON_10_httpwadl_dev_java_net200902representation', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2), )

    
    representation = property(__representation.value, __representation.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwadl_dev_java_net200902_CTD_ANON_10_httpwadl_dev_java_net200902param', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpwadl_dev_java_net200902_CTD_ANON_10_status', statusCodeList)
    __status._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 173, 6)
    __status._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 173, 6)
    
    status = property(__status.value, __status.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __representation.name() : __representation,
        __param.name() : __param
    }
    _AttributeMap = {
        __status.name() : __status
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 183, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_11_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param'), 'param', '__httpwadl_dev_java_net200902_CTD_ANON_11_httpwadl_dev_java_net200902param', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwadl_dev_java_net200902_CTD_ANON_11_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 190, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 190, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute element uses Python identifier element
    __element = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'element'), 'element', '__httpwadl_dev_java_net200902_CTD_ANON_11_element', pyxb.binding.datatypes.QName)
    __element._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 191, 6)
    __element._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 191, 6)
    
    element = property(__element.value, __element.set, None, None)

    
    # Attribute mediaType uses Python identifier mediaType
    __mediaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mediaType'), 'mediaType', '__httpwadl_dev_java_net200902_CTD_ANON_11_mediaType', pyxb.binding.datatypes.string)
    __mediaType._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 192, 6)
    __mediaType._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 192, 6)
    
    mediaType = property(__mediaType.value, __mediaType.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwadl_dev_java_net200902_CTD_ANON_11_href', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 193, 6)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 193, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute profile uses Python identifier profile
    __profile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'profile'), 'profile', '__httpwadl_dev_java_net200902_CTD_ANON_11_profile', uriList)
    __profile._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 194, 6)
    __profile._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 194, 6)
    
    profile = property(__profile.value, __profile.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __param.name() : __param
    }
    _AttributeMap = {
        __id.name() : __id,
        __element.name() : __element,
        __mediaType.name() : __mediaType,
        __href.name() : __href,
        __profile.name() : __profile
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 214, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_12_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}option uses Python identifier option
    __option = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'option'), 'option', '__httpwadl_dev_java_net200902_CTD_ANON_12_httpwadl_dev_java_net200902option', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 236, 2), )

    
    option = property(__option.value, __option.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'link'), 'link', '__httpwadl_dev_java_net200902_CTD_ANON_12_httpwadl_dev_java_net200902link', False, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 249, 2), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwadl_dev_java_net200902_CTD_ANON_12_href', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 222, 6)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 222, 6)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwadl_dev_java_net200902_CTD_ANON_12_name', pyxb.binding.datatypes.NMTOKEN)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 223, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 223, 6)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'style'), 'style', '__httpwadl_dev_java_net200902_CTD_ANON_12_style', ParamStyle)
    __style._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 224, 6)
    __style._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 224, 6)
    
    style = property(__style.value, __style.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwadl_dev_java_net200902_CTD_ANON_12_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 225, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 225, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwadl_dev_java_net200902_CTD_ANON_12_type', pyxb.binding.datatypes.QName, unicode_default=u'xs:string')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 226, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 226, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute default uses Python identifier default
    __default = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'default'), 'default', '__httpwadl_dev_java_net200902_CTD_ANON_12_default', pyxb.binding.datatypes.string)
    __default._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 227, 6)
    __default._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 227, 6)
    
    default = property(__default.value, __default.set, None, None)

    
    # Attribute required uses Python identifier required
    __required = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'required'), 'required', '__httpwadl_dev_java_net200902_CTD_ANON_12_required', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __required._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 228, 6)
    __required._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 228, 6)
    
    required = property(__required.value, __required.set, None, None)

    
    # Attribute repeating uses Python identifier repeating
    __repeating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'repeating'), 'repeating', '__httpwadl_dev_java_net200902_CTD_ANON_12_repeating', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __repeating._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 229, 6)
    __repeating._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 229, 6)
    
    repeating = property(__repeating.value, __repeating.set, None, None)

    
    # Attribute fixed uses Python identifier fixed
    __fixed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed'), 'fixed', '__httpwadl_dev_java_net200902_CTD_ANON_12_fixed', pyxb.binding.datatypes.string)
    __fixed._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 230, 6)
    __fixed._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 230, 6)
    
    fixed = property(__fixed.value, __fixed.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'path'), 'path', '__httpwadl_dev_java_net200902_CTD_ANON_12_path', pyxb.binding.datatypes.string)
    __path._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 231, 6)
    __path._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 231, 6)
    
    path = property(__path.value, __path.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __option.name() : __option,
        __link.name() : __link
    }
    _AttributeMap = {
        __href.name() : __href,
        __name.name() : __name,
        __style.name() : __style,
        __id.name() : __id,
        __type.name() : __type,
        __default.name() : __default,
        __required.name() : __required,
        __repeating.name() : __repeating,
        __fixed.name() : __fixed,
        __path.name() : __path
    }



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 109, 4)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://wadl.dev.java.net/2009/02}doc uses Python identifier doc
    __doc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'doc'), 'doc', '__httpwadl_dev_java_net200902_CTD_ANON_13_httpwadl_dev_java_net200902doc', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2), )

    
    doc = property(__doc.value, __doc.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}request uses Python identifier request
    __request = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'request'), 'request', '__httpwadl_dev_java_net200902_CTD_ANON_13_httpwadl_dev_java_net200902request', False, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 149, 2), )

    
    request = property(__request.value, __request.set, None, None)

    
    # Element {http://wadl.dev.java.net/2009/02}response uses Python identifier response
    __response = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'response'), 'response', '__httpwadl_dev_java_net200902_CTD_ANON_13_httpwadl_dev_java_net200902response', True, pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 163, 2), )

    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwadl_dev_java_net200902_CTD_ANON_13_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 118, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 118, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwadl_dev_java_net200902_CTD_ANON_13_name', Method)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 119, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 119, 6)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwadl_dev_java_net200902_CTD_ANON_13_href', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 120, 6)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 120, 6)
    
    href = property(__href.value, __href.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02'))
    _HasWildcardElement = True

    _ElementMap = {
        __doc.name() : __doc,
        __request.name() : __request,
        __response.name() : __response
    }
    _AttributeMap = {
        __id.name() : __id,
        __name.name() : __name,
        __href.name() : __href
    }



application = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'application'), CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', application.name().localName(), application)

doc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', doc.name().localName(), doc)

grammars = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grammars'), CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 42, 2))
Namespace.addCategoryObject('elementBinding', grammars.name().localName(), grammars)

resources = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resources'), CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 53, 2))
Namespace.addCategoryObject('elementBinding', resources.name().localName(), resources)

resource_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource_type'), CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 91, 2))
Namespace.addCategoryObject('elementBinding', resource_type.name().localName(), resource_type)

include = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include'), CTD_ANON_5, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 139, 2))
Namespace.addCategoryObject('elementBinding', include.name().localName(), include)

request = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'request'), CTD_ANON_6, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 149, 2))
Namespace.addCategoryObject('elementBinding', request.name().localName(), request)

option = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'option'), CTD_ANON_7, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 236, 2))
Namespace.addCategoryObject('elementBinding', option.name().localName(), option)

link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 249, 2))
Namespace.addCategoryObject('elementBinding', link.name().localName(), link)

resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2))
Namespace.addCategoryObject('elementBinding', resource.name().localName(), resource)

response = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 163, 2))
Namespace.addCategoryObject('elementBinding', response.name().localName(), response)

representation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'representation'), CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2))
Namespace.addCategoryObject('elementBinding', representation.name().localName(), representation)

param = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2))
Namespace.addCategoryObject('elementBinding', param.name().localName(), param)

method = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), CTD_ANON_13, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2))
Namespace.addCategoryObject('elementBinding', method.name().localName(), method)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grammars'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 42, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resources'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 53, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource_type'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 91, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), CTD_ANON_13, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'representation'), CTD_ANON_11, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 14, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 15, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 16, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 18, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 24, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 14, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grammars')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 15, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resources')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 16, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource_type')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 19, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'method')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 20, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'representation')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 21, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 22, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 24, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 33, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 33, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include'), CTD_ANON_5, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 139, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 45, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 46, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 47, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 45, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'include')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 46, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 47, 8))
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
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), CTD_ANON_9, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 56, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 58, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 56, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 57, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 58, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), CTD_ANON_9, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), CTD_ANON_13, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 94, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 95, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 96, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 100, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 94, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 95, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'method')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 97, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 98, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 100, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 142, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 142, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'representation'), CTD_ANON_11, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 152, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 153, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 154, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 156, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 152, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 153, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'representation')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 154, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 156, 8))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 239, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 240, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 239, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 240, 8))
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
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 252, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 253, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 252, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 253, 8))
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
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), CTD_ANON_9, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 66, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), CTD_ANON_13, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 108, 2)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 69, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 70, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 71, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 75, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 69, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 70, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'method')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 72, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 73, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 75, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'representation'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 182, 2)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 166, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 167, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 168, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 170, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 166, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 167, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'representation')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 168, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 170, 8))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param'), CTD_ANON_12, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 213, 2)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 185, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 186, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 187, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 185, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 186, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 187, 8))
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
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'option'), CTD_ANON_7, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 236, 2)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), CTD_ANON_8, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 249, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 216, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 217, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 218, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 219, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 216, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'option')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 217, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 218, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 219, 8))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doc'), CTD_ANON_, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 30, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'request'), CTD_ANON_6, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 149, 2)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), CTD_ANON_10, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 163, 2)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 111, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 112, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 113, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 115, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doc')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 111, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'request')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 112, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'response')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 113, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://wadl.dev.java.net/2009/02')), pyxb.utils.utility.Location('http://www.w3.org/Submission/wadl/wadl.xsd', 115, 8))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
CTD_ANON_13._Automaton = _BuildAutomaton_13()

