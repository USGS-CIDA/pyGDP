from __future__ import (absolute_import, division, print_function)

__version__ = '2.1.2'

# dependencies: lxml.etree, owslib
# =============================================================================
# Authors : Xao Yang, Jordan Walker, Jordan Read, Curtis Price, David Blodgett,
# Parker Norton, Steve Kochaver
#
# Contact email: jread@usgs.gov
# =============================================================================
from . import shapefile_value_handle, shapefile_id_handle, _get_geotype
from . import webdata_handle, _webdata_xml_generate
from . import fwgs, _execute_request, feature_coverage
from . import upload_shapefile, shape_to_zip

# This series of import functions brings in the namespaces, url, and pyGDP utility
# variables from the pyGDP_Namespaces file, as well as owslib's own namespaces
# Check out the pyGDP_Namespaces file to see precisely how things are
# what URLs pyGDP is pointing to. It's good to be aware.
from .pyGDPwebProcessing import pyGDPwebProcessing
from .GDP_XML_Generator import gdpXMLGenerator
from .namespaces import upload_URL, WPS_URL, WPS_Service, CSW_URL
from .namespaces import WFS_URL
from .namespaces import WPS_DEFAULT_VERSION, WPS_DEFAULT_SCHEMA_LOCATION, GML_SCHEMA_LOCATION
from .namespaces import WPS_DEFAULT_NAMESPACE, CSW_NAMESPACE, WPS_DEFAULT_NAMESPACE
from .namespaces import WFS_NAMESPACE, OGC_NAMESPACE, GML_NAMESPACE
from .namespaces import DRAW_NAMESPACE, SMPL_NAMESPACE, UPLD_NAMESPACE
from .namespaces import URL_timeout, WPS_attempts
from .namespaces import namespaces

# try:
#     from urllib import urlencode
# except ImportError:
#     from urllib.parse import urlencode

# Currently unused
# from time import sleep
# import cgi
# import sys
# from io import BytesIO
# from owslib.ows import DEFAULT_OWS_NAMESPACE, XSI_NAMESPACE, XLINK_NAMESPACE
# from owslib.wps import WebProcessingService, monitorExecution
#
# import logging
