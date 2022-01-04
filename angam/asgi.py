from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
from pathlib import Path
from importlib.util import find_spec
from fastapi.staticfiles import StaticFiles



# Export Django settings env variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'angam.settings')
