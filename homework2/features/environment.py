import os
import sys
import django

# Add the correct project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "movie_theater_booking"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Initialize Django
django.setup()