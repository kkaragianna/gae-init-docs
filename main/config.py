# -*- coding: utf-8 -*-

import os
try:
  # This part is surrounded in try/except because the this config.py file is
  # also used in the run.py script which is used to compile/minify the client
  # side files (*.less, *.coffee, *.js) and is not aware of the GAE
  import model
  from datetime import datetime
  CONFIG_DB = model.Config.get_master_db()
  SECRET_KEY = CONFIG_DB.flask_secret_key.encode('ascii')
  CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
  CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]
  CURRENT_VERSION_TIMESTAMP = long(CURRENT_VERSION_ID.split('.')[1]) >> 28
  CURRENT_VERSION_DATE = datetime.fromtimestamp(CURRENT_VERSION_TIMESTAMP)
except:
  pass

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine')
DEVELOPMENT = not PRODUCTION
DEBUG = DEVELOPMENT

DEFAULT_DB_LIMIT = 64

################################################################################
# Client modules, also used by the run.py script.
################################################################################
STYLES = [
    'src/less/style.less',
  ]

SCRIPTS_MODULES = [
    'libs',
    'scripts',
  ]

SCRIPTS = {
    'libs': [
        'lib/jquery.js',
        'lib/nprogress.js',
        'lib/moment.js',
        'lib/bootstrap/js/alert.js',
        'lib/bootstrap/js/button.js',
        'lib/bootstrap/js/collapse.js',
        'lib/bootstrap/js/dropdown.js',
        'lib/bootstrap/js/tooltip.js',
      ],
    'scripts': [
        'src/coffee/common/util.coffee',
        'src/coffee/common/service.coffee',
        'src/coffee/site/app.coffee',
        'src/coffee/site/profile.coffee',
        'src/coffee/site/admin.coffee',
        'src/coffee/site/github.coffee',
      ],
  }
