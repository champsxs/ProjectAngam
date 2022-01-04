from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path
from importlib.util import find_spec
from django.conf import settings

from projects.models import Projects




# Export Django settings env variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'angam.settings')

# Get Django WSGI app
django_app = get_wsgi_application()

# Import a model
# And always import your models after you export settings
# and you get Django WSGI app


# Create FasatAPI instance
app = FastAPI()

# Serve Django static files

BASE_DIR = Path(__file__).resolve().parent.parent
app.mount('/static/', 
    StaticFiles(directory=os.path.normpath(os.path.join(BASE_DIR, 'angam', 'static'))), name='static')
app.mount('/app/uploads/', 
    StaticFiles(directory=os.path.normpath(os.path.join(BASE_DIR, 'angam', 'static', 'uploads'))), name='uploads')

# Define a FastAPI route
@app.get('/fastapi-test')
def read_main():
    return {
        'total_accounts': "1",
        'is_debug': settings.DEBUG 
    }

@app.get('/projects')
class get_project(Projects):
    pass
# Mount Django app
app.mount('/app', WSGIMiddleware(django_app))