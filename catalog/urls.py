from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import goods, home, category_stuff

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('goods/', goods, name='goods'),
    path('<int:pk>/stuff', category_stuff, name='category_stuff')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)