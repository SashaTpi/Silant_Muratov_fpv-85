from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('repser/', ListRepSerView.as_view(), name='repser_list'),
    path('reclamation/', ListReclamationView.as_view(), name='reclamation_list'),
    path('car/<pk>/repser', CarListRepSerView.as_view(), name='car_repser'),
    path('car/<pk>/reclamation', CarListReclamationView.as_view(), name='car_reclamation'),
    path('repser/create', CreateRepSerView.as_view(), name='repser_create'),
    path('reclamation/create', CreateReclamationView.as_view(), name='reclamation_create'),
    path('repser/<pk>/update', UpdateRepSerView.as_view(), name='repser_update'),
    path('reclamation/<pk>/update', UpdateReclamationView.as_view(), name='reclamation_update'),
    path('repser/<pk>/delete', DeleteRepSerView.as_view(), name='repser_delete'),
    path('reclamation/<pk>/delete', DeleteReclamationView.as_view(), name='reclamation_delete'),
    path('repser/<pk>/description/<atribute>', DescriptionRepSerView.as_view(),
         name='repser_description'),
    path('reclamation/<pk>/description/<atribute>', DescriptionReclamationView.as_view(), name='reclamation_description'),

    path('', HomeView.as_view(template_name='/index.html'), name='home'),
    path('search/', SearchCarView.as_view(), name='car_search_list'),
    path('cars/', ListCarView.as_view(), name='car_list'),
    path('car/<pk>/detail', DetailCarView.as_view(), name='car_detail'),
    path('car/create', CreateCarView.as_view(), name='car_create'),
    path('car/<pk>/update', UpdateCarView.as_view(), name='car_update'),
    path('car/<pk>/delete', DeleteCarView.as_view(), name='car_delete'),
    path('car/<pk>/description/<atribute>', DescriptionCarView.as_view(), name='car_description'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)