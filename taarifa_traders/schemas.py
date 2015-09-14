# trader_schema stores issues reported by the traders
# FIXME: change name to issue_schema
trader_schema = {
    'gid': {
        'type': 'integer',
        'label': 'GID',
        # FIXME: not really unique...
        # 'unique': True
    },
    'objectid': {
        'type': 'integer',
        'label': 'Object ID',
        # FIXME: not really unique...
        # 'unique': True
    },
    'issue_phone_number': {
        'type': 'string',
        'label': 'Phone Number',
    },
    'issue_code': {
        'type': 'string',
        'label': 'Issue Code',
    },
    'issue_keyword': {
        'type': 'string',
        'label': 'Keyword',
        'allowed': ['Customs', 'TRA', 'ZRA', 'MRA', 'Immigration', 'Police', 'Bureau', 'Standards', 'Duty', 'Passport', 'BorderPass', 'Corruption', 'Harassment', 'Bribe'],
    },
    'issue_type': {
        'type': 'string',
        'label': 'Issue Type',
        'allowed': ['Non-Tarriff Barriers (NTB)', 'Tarriff Barriers (TB)'],
    },
    'issue_agency': {
        'type': 'string',
        'label': 'Agency',
    },
    'issue_date': {
        'type': 'datetime',
        'label': 'Date recorded',
    },
    'location': {
        'type': 'point',
    },
    'issue_status': {
        'type': 'string',
        'label': 'Status detail',
    },
    'issue_status_group': {
        'type': 'string',
        'label': 'Status group',
        'allowed': ['complete', 'pending'],
    },
}

subscriber_schema = {
    'issue_phone_number': {
        'type': 'string',
        'label': 'Phone Number',
    },
    'issue_code': {
        'type': 'string',
        'label': 'Issue Code',
    },
    'issue_keyword': {
        'type': 'string',
        'label': 'Keyword',
        'allowed': ['Customs', 'TRA', 'ZRA', 'MRA', 'Immigration', 'Police', 'Bureau', 'Standards', 'Duty', 'Passport', 'BorderPass', 'Corruption', 'Harassment', 'Bribe'],
    },
    'issue_status': {
        'type': 'integer',
        'label': 'Status',
        'allowed': [0, 1],
    },
    'issue_description': {
        'type': 'string',
        'label': 'Description',
    }
}

# Facility and resources go hand in hand. Following Open311 the facility
# schema uses its fields attribute to define the schema resources must
# have that are part of the facility.
# FIXME: facility/service code duplicated here and in manage.py, should be in
# settings.py
facility_schema = {'facility_code': "trd001",
                    'facility_name': "Cross-Border Traders",
                    # this defines the schema of a resource within this facility
                    'fields': trader_schema,
                    'description': "Cross-Border Traders",
                    'keywords': ["Customs", "TRA", "ZRA", "MRA", "Immigration", "Police", "Bureau", "Standards", "Duty", "Passport", "BorderPass", "Corruption", "Harassment", "Bribe"],
                    'group': "trader",
                    'endpoint': "traders"}
#facility_schema = {'facility_code': "sub001",
#                   'facility_name': "Cross-Border Traders Subscribers",
#                   # this defines the schema of a resource within this facility
#                   'fields': subscriber_schema,
#                   'description': "Cross-Border Traders Subscribers",
#                   'keywords': ["Customs", "TRA", "ZRA", "MRA", "Immigration", "Police", "Bureau", "Standards", "Duty", "Passport", "BorderPass", "Corruption", "Harassment", "Bribe"],
#                   'group': "subscribers",
#                   'endpoint': "subscribers"}

# Services and requests go hand in hand too. Here its the attributes field of a
# service that defines what the schema of a request (report) should look like.
service_schema = {
    "service_name": "Cross-Border Traders service",
    "attributes": [
        # This defines the schema of a request for this service
        # FIXME: how to refer to fields defined in the base schema in
        # TaarfaAPI?
        {"variable": True,
         # FIXME: we need to enforce a foreign key constraint here
         "code": "issue_id",
         "datatype": "string",
         "required": True,
         "datatype_description": "Enter a valid Issue id",
         "order": 1,
         "description": "Unique id of this issue",
         "relation": {"resource": "traders",
                      "field": "issue_code"}},
        {"variable": True,
         "code": "status_group",
         "datatype": "singlevaluelist",
         "required": True,
         "datatype_description": "Select an option from the list",
         "order": 2,
         "description": "Status of this issue",
         "values": [{"key": "complete",
                     "name": "Complete"},
                    {"key": "pending",
                     "name": "Pending"}]},
        {"variable": True,
         "code": "status_detail",
         "datatype": "string",
         "required": False,
         "datatype_description": "Describe the status of the issue",
         "order": 3,
         "description": "Detailed description of the issue status"}
    ],
    "description": "Location and status of a issue",
    "keywords": ["location", "issue", "traders"],
    "group": "issue",
    "service_code": "trd001"
}
