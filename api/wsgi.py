import os
from django.core.wsgi import get_wsgi_application
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
application = get_wsgi_application()

sys.path.append("/home/moringa/Documents/project/optica-backend/api")