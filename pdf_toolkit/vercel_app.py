import os
from django.core.asgi import get_asgi_application

# Set the settings module for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdf_toolkit.settings")  # Replace 'myproject' with your project name

# Define the ASGI app to be served by Vercel
app = get_asgi_application()
