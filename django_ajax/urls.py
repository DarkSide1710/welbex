from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from crud_ajax.views import CreateCrudWelbex, main, DeleteCrudWelbex, UpdateCrudWelbex

urlpatterns = [
                  path('admin/', admin.site.urls),


                  # Django Ajax CRUD Operations
                  path('', main, name='crud_ajax'),
                  path('ajax/crud/create/', CreateCrudWelbex.as_view(), name='crud_ajax_create'),
                  path('ajax/crud/delete/', DeleteCrudWelbex.as_view(), name='crud_ajax_delete'),
                  path('ajax/crud/update/', UpdateCrudWelbex.as_view(), name='crud_ajax_update'),



              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
