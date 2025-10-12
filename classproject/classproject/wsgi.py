"""
WSGI config for classproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys #this is new

path = '/home/TryMe/classproject/classproject/settings.py' #this is new
if path not in sys.path: #This if statement is also new
    sys.path.append(path)


from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classproject.settings')#This does not work
os.environ['DJANGO_SETTINGS_MODULE'] = 'classproject.settings'

application = get_wsgi_application()
#-----------------------------------------------------
# ## assuming your django settings file is at '/home/newtest3r/mysite/mysite/settings.py'
# ## and your manage.py is is at '/home/newtest3r/mysite/manage.py'
# path = '/home/newtest3r/classproject/classproject'
# if path not in sys.path:
#     sys.path.append(path)
# #
# os.environ['DJANGO_SETTINGS_MODULE'] = 'classproject.settings'
# #
# ## then:
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()