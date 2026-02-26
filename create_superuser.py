import os
import sys

# Add the project direct to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(username='admin', email='admin@gmail.com', password='12345678')
    print("Superuser 'admin' created successfully.")
else:
    print("Superuser 'admin' already exists.")
