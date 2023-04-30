from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),

    path('gastos/', views.GastoListView.as_view(), name='lista_de_gastos'),
    path('gastos/crear/', views.GastoCreateView.as_view(), name='crear_gasto'),
    path('gastos/<int:pk>/', views.GastoDetailView.as_view(), name='detalle_gasto'),
    path('gastos/<int:pk>/modificar/', views.GastoUpdateView.as_view(), name='modificar_gasto'),
    path('gastos/<int:pk>/eliminar/', views.GastoDeleteView.as_view(), name='eliminar_gasto'),
]
