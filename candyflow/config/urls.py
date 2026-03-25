from django.contrib import admin
from django.urls import path
from apps.core.views import dashboard
from apps.catalog.views import candy_list
from apps.production.views import production_list
from apps.inventory.views import inventory_movements
from apps.sales.views import sale_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('catalogo/', candy_list, name='candy_list'),
    path('produccion/', production_list, name='production_list'),
    path('inventario/', inventory_movements, name='inventory_movements'),
    path('ventas/', sale_list, name='sale_list'),
]
