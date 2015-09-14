import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/taarifa_waterpoints')

from taarifa_waterpoints import app
application.secrete_key = 'ErV8uIbYkkIjn4Xcl5ulU8408DlG5JUL'
