import os

from django.core.asgi import get_asgi_application
from django.urls import path # new

from channels.routing import ProtocolTypeRouter, URLRouter # changed

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')

django_asgi_application = get_asgi_application()

from trips.consumers import TaxiConsumer
from taxi.middleware import TokenAuthMiddlewareStack # new

application = ProtocolTypeRouter({
    'http': django_asgi_application,# new
    'websocket': TokenAuthMiddlewareStack( # changed
        URLRouter([
            path('taxi/', TaxiConsumer.as_asgi()),
        ])
    ),
})