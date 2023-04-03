"""
ASGI config for CPP_MarketPlace project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import Messaging.routing

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
#from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CPP_MarketPlace.settings')

application = get_asgi_application() #original

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': #AllowedHostsOriginValidator(
        AuthMiddlewareStack(
        URLRouter(
            Messaging.routing.websocket_urlpatterns
        )
    )
    #)
})