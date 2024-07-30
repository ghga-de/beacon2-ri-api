import yaml

with open("beacon/api_version.yml") as api_version_file:
    api_version_yaml = yaml.safe_load(api_version_file)

"""Beacon Configuration."""


#
# Beacon general info
#
beacon_id = 'de.dkfz.ghga.beacon'  # ID of the Beacon
beacon_name = 'Beaconv2 at DKFZ.de in Heidelberg, Germany'  # Name of the Beacon service
api_version = 'v2.0.0'  # Version of the Beacon implementation
uri = 'https://beacon.gdi.dkfz.de/api/'

#
# Beacon granularity
#
default_beacon_granularity = "record"
max_beacon_granularity = "record"

#
#  Organization info
#
org_id = 'ghga.de'  # Id of the organization
org_name = 'The German Human Genome-Phenome Archive (GHGA)'  # Full name
org_description = ('The German Human Genome-Phenome Archive is a consortium within the national data infrastructure.'
                   'GHGA aims to create a secure national data infrastructure for human omics data in order to make '
                   'these data available for scientific research while preventing the misuse of data.')
org_adress = ('C/ Im Neuenheimer Feld 280,'
              '69120, Heidelberg, Germany')
org_welcome_url = 'https://ghga.de/'
org_contact_url = 'mailto:contact@ghga.de'
org_logo_url = 'https://www.ghga.de/fileadmin/_processed_/e/3/csm_GHGA_CMYK_Bright_Orange_c925771725.webp'
org_info = ''

#
# Project info
#
#description = (r"This <a href='https://beacon-project.io/'>Beacon</a> "
#               r"is based on the GA4GH Beacon "
#               r"<a href='https://github.com/ga4gh-beacon/specification-v2/blob/master/beacon.yaml'>v2.0</a>")
description = r"This is the german Beacon hosted at the dkfz.de it is currently based on synthetic data hosted at the <a href='https://ega-archive.org/datasets/EGAD00001003338'>EGA</a>. The dataset contains 2504 samples including genetic data based on 1K Genomes data, and 76 individual attributes and phenotypic data derived from UKBiobank."
version = 'v2.0'
welcome_url = 'https://beacon.gdi.dkfz.de/'
alternative_url = 'https://beacon.gdi.dkfz.de/api'
create_datetime = '2021-11-29T12:00:00.000000'
update_datetime = ''
# update_datetime will be created when initializing the beacon, using the ISO 8601 format

#
# Service
#
service_type = 'org.ga4gh:beacon:1.0.0'  # service type
service_url = 'https://beacon.biodata.pt/api/service-info'
entry_point = False
is_open = True
documentation_url = 'https://github.com/EGA-archive/beacon-2.x/'  # Documentation of the service
environment = 'test'  # Environment (production, development or testing/staging deployments)

# GA4GH
ga4gh_service_type_group = 'org.ga4gh'
ga4gh_service_type_artifact = 'beacon'
ga4gh_service_type_version = '1.0'

# Beacon handovers
beacon_handovers ={
        'handoverType': {
            'id': 'CUSTOM:000001',
            'label': 'Project description'
        },
        'note': 'Project description',
        'url': 'https://www.nist.gov/programs-projects/genome-bottle'
    }

#
# Database connection
#
database_host = 'mongo' #'host.docker.internal'
database_port = 27017
database_user = 'root'
database_password = 'example'
database_name = 'beacon'
database_auth_source = 'admin'
# database_schema = 'public' # comma-separated list of schemas
# database_app_name = 'beacon-appname' # Useful to track connections

#
# Web server configuration
# Note: a Unix Socket path is used when behind a server, not host:port
#
beacon_host = '0.0.0.0'
beacon_port = 5050
beacon_tls_enabled = False
beacon_tls_client = False
beacon_cert = '/etc/ega/server.cert'
beacon_key = '/etc/ega/server.key'
CA_cert = '/etc/ega/CA.cert'

#
# Permissions server configuration
#
permissions_url = 'http://beacon-permissions:5051/'

#
# IdP endpoints (OpenID Connect/Oauth2)
#
# or use Elixir AAI (see https://elixir-europe.org/services/compute/aai)
#

idp_url = 'http://idp:8080/'
#idp_url = 'http://localhost:8080/'

#
# UI
#
autocomplete_limit = 16
autocomplete_ellipsis = '...'

#
# Ontologies
#
ontologies_folder = "ontologies"

alphanumeric_terms = ['libraryStrategy', 'molecularAttributes.geneIds', 'diseases.ageOfOnset.iso8601duration', 'molecularAttributes.aminoacidChanges']

ontology_files={"NCIT": "http://purl.obolibrary.org/obo/NCIT.obo"}
