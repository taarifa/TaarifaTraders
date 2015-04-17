from csv import DictReader
from datetime import datetime
from pprint import pprint

from flask.ext.script import Manager

from taarifa_api import add_document, delete_documents, get_schema
from taarifa_waterpoints import app
from taarifa_waterpoints.schemas import facility_schema, service_schema

manager = Manager(app)


def check(response, success=201, print_status=True):
    data, _, _, status = response
    if status == success:
        if print_status:
            print " Succeeded"
        return True

    print "Failed with status", status
    pprint(data)
    return False


@manager.option("resource", help="Resource to show the schema for")
def show_schema(resource):
    """Show the schema for a given resource."""
    pprint(get_schema(resource))


@manager.command
def list_routes():
    """List all routes defined for the application."""
    import urllib
    for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.endpoint):
        methods = ','.join(rule.methods)
        print urllib.unquote("{:40s} {:40s} {}".format(rule.endpoint, methods,
                                                       rule))


@manager.command
def create_facility():
    """Create facility for waterpoints."""
    check(add_document('facilities', facility_schema))


@manager.command
def create_service():
    """Create service for waterpoints."""
    check(add_document('services', service_schema))


@manager.command
def delete_facilities():
    """Delete all facilities."""
    check(delete_documents('facilities'), 200)


@manager.command
def delete_services():
    """Delete all services."""
    check(delete_documents('services'), 200)


@manager.command
def delete_requests():
    """Delete all requests."""
    check(delete_documents('requests'), 200)


# @manager.option("filename", help="CSV file to upload (required)")
# @manager.option("--skip", type=int, default=0, help="Skip a number of records")
# @manager.option("--limit", type=int, help="Only upload a number of records")
@manager.command
def upload_traders():
    """Upload waterpoints from a CSV file."""
    # Use sys.stdout.write so waterpoints can be printed nicely and succinctly
    d = {
        'gid': 12,
        'objectid': 346,
        'issue_phone_number': '0782978899',
        'issue_keyword': 'Customs',
        'issue_date': datetime.now(),
        'location': {'type': 'Point', 'coordinates': [35.786, -3.648]},
        'issue_status': 'Wanacharge bei kubwa sana. Naombeni wachukuliwe hatua!',
        'issue_status_group': 'pending',
        'issue_type': 'TB',
        'issue_agency': 'TANTRADE',
        'facility_code':'trd001',
    }
    check(add_document('traders', d), 201, False)


@manager.command
def ensure_indexes():
    """Make sure all important database indexes are created."""
    print "Ensuring resources:location 2dsphere index is created ..."
    app.data.driver.db['resources'].ensure_index([('location', '2dsphere')])
    print "Done!"


@manager.option("status", help="Status (functional or non functional)")
@manager.option("wp", help="Waterpoint id")
def create_request(wp, status):
    """Create an example request reporting a broken waterpoint"""
    r = {"service_code": "wps001",
         "attribute": {"waterpoint_id": wp,
                       "status": status}}
    check(add_document("requests", r))


@manager.command
def delete_waterpoints():
    """Delete all existing waterpoints."""
    print delete_documents('waterpoints')

if __name__ == "__main__":
    manager.run()
