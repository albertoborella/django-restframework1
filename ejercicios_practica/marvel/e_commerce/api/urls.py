from django.urls import path
from e_commerce.api.views_api import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('primera_vista_api/', primera_vista_api),
    path('segunda_vista_api/', segunda_vista_api),
    path('tercera_vista_api/', tercera_vista_api),
    path('get-comics/',get_comics),
    path('purchased-item/',purchased_item),
]