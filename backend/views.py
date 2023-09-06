from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404 
from rest_framework import generics 
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from .models import *
from .forms import *
from api.serializers import *


class HomeView(TemplateView): 
    template_name = '/index.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('car_list')
        else:
            return redirect('car_search_list')


class ListCarView(LoginRequiredMixin, ListView): 
    model = Mashins,
    template_name = 'backend/car/car_list.html'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = CustomUser.objects.get(pk=self.request.user.pk)
            try:
                clients = Client.objects.get(name_id=user)
                car = Mashins.objects.filter(client=clients)
                return car
            except:
                servis = ServiceComp.objects.get(name_id=user)
                car = Mashins.objects.filter(service_company=servis)
                return car
        else:
            return Mashins.objects.all()


class ListRepSerView(LoginRequiredMixin, ListView): 
    permission_required = 'backend.view_TO'
    model = TO,
    template_name = 'backend/to/repser_list.html'
    context_object_name = 'mashins_TO'
    ordering = 'mashins_TO'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = CustomUser.objects.get(pk=self.request.user.pk)

            try:
                clients = Client.objects.get(name_id=user.pk)
                mashins = Mashins.objects.filter(client=clients)
                for m in mashins:
                    yield TO.objects.filter(mashins_TO=m)
            except:
                servis = ServiceComp.objects.get(name_id=user.pk)
                mashins = Mashins.objects.filter(service_company=servis)
                for i in list(mashins):
                    yield TO.objects.filter(mashins_TO=i)
        else:
            yield TO.objects.all()


class ListReclamationView(LoginRequiredMixin, ListView): 
    permission_required = 'backend.view_reclamation'
    model = Reclamation,
    template_name = 'backend/reclamation/reclamation_list.html'
    ordering = 'mashins_c'
    context_object_name = 'mashins_c'

    def get_queryset(self):
        if not self.request.user.is_staff:
            user = CustomUser.objects.get(pk=self.request.user.pk)

            try:
                clients = Client.objects.get(name_id=user.pk)
                mashins = Mashins.objects.filter(client=clients)
                for m in mashins:
                    yield Reclamation.objects.filter(mashins_c=m)
            except:
                servis = ServiceComp.objects.get(name_id=user)
                mashins = Mashins.objects.filter(service_company=servis)
                for i in list(mashins):
                    yield Reclamation.objects.filter(mashins_c=i)
        else:
            yield Reclamation.objects.all()


class SearchCarView(ListView): 
    model = Mashins
    template_name = 'backend/car/car_search.html'
    queryset = Mashins.objects.all()


class DetailCarView(LoginRequiredMixin, DetailView):
    permission_required = 'backend.view_car'
    model = Mashins
    template_name = 'backend/car/car_view.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateCarView(LoginRequiredMixin, CreateView):
    permission_required = 'backend.add_car'
    model = Mashins
    form_class = FormCar
    template_name = 'backend/car/car_create.html'
    success_url = reverse_lazy('car_list')


class UpdateCarView(LoginRequiredMixin, UpdateView):
    permission_required = 'backend.change_car'
    model = Mashins
    form_class = FormCar
    template_name = 'backend/car/car_update.html'
    success_url = reverse_lazy('car_list')


class DescriptionCarView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'model_mashins':
            context['atribute'] = car.model_mashins
            context['description'] = car.model_mashins.description
        elif atribute == 'model_motor':
            context['atribute'] = car.model_motor
            context['description'] = car.model_motor.description
        elif atribute == 'model_transmission':
            context['atribute'] = car.model_transmission
            context['description'] = car.model_transmission.description
        elif atribute == 'model_main_bridge':
            context['atribute'] = car.model_main_bridge
            context['description'] = car.model_main_bridge.description
        elif atribute == 'model_controll_bridge':
            context['atribute'] = car.model_controll_bridge
            context['description'] = car.model_controll_bridge.description
        elif atribute == 'outfitting':
            context['atribute'] = 'Комплектация'
            context['description'] = car.outfitting
        elif atribute == 'service_company':
            context['atribute'] = car.service_company
            context['description'] = car.service_company.description
        return context


class DeleteCarView(LoginRequiredMixin, DeleteView):
    permission_required = 'backend.delete_car'
    model = Mashins
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('car_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'car'
        return context


class ListCarAPI(generics.ListAPIView): 
    serializer_class = MashinsSerializer
    queryset = Mashins.objects.all()


class UserListCarAPI(generics.ListAPIView):
    serializer_class = MashinsSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Mashins.objects.filter(client=user)
        elif type(user) == str:
            queryset = Mashins.objects.filter(client__username=user)
        return queryset


class DetaiCarAPI(generics.RetrieveAPIView): 
    serializer_class = MashinsSerializer

    def get_object(self):
        obj = Mashins.objects.get(pk=self.kwargs['pk'])
        return obj


class CreateRepSerView(LoginRequiredMixin, CreateView):
    permission_required = 'backend.add_TO'
    model = TO
    form_class = FormRepSer
    template_name = 'backend/to/repser_create.html'
    success_url = reverse_lazy('repser_list')


class UpdateRepSerView(LoginRequiredMixin, UpdateView):
    permission_required = 'backend.change_TO'
    model = TO
    form_class = FormRepSer
    template_name = 'backend/to/repser_update.html'
    success_url = reverse_lazy('repser_list')


class DeleteRepSerView(LoginRequiredMixin, DeleteView):
    permission_required = 'backend.delete_TO'
    model = TO
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('repser_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vid_TO"] = 'repser'
        return context


class CarListRepSerView(LoginRequiredMixin, ListView):
    permission_required = 'backend.view_TO'
    model = TO
    template_name = 'backend/to/repser_car.html'

    def get_queryset(self):
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        return TO.objects.filter(mashins_TO=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Mashins.objects.get(pk=self.kwargs["pk"])
        return context


class DescriptionRepSerView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        repser = TO.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'type':
            context['atribute'] = repser.vid_TO
            context['description'] = repser.vid_TO.description
        elif atribute == 'service_TO':
            context['atribute'] = repser.service_TO
            context['description'] = repser.service_TO.description
        return context


class CreateReclamationView(LoginRequiredMixin, CreateView):
    permission_required = 'backend.add_reclamation'
    model = Reclamation
    form_class = FormReclamation
    template_name = 'backend/reclamation/reclamation_create.html'
    success_url = reverse_lazy('reclamation_list')


class UpdateReclamationView(LoginRequiredMixin, UpdateView):
    permission_required = 'backend.change_reclamation'
    model = Reclamation
    form_class = FormReclamation
    template_name = 'backend/reclamation/reclamation_update.html'
    success_url = reverse_lazy('reclamation_list')


class DeleteReclamationView(LoginRequiredMixin, DeleteView): 
    permission_required = 'backend.delete_reclamation'
    model = Reclamation
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('reclamation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'reclamation'
        return context


class CarListReclamationView(LoginRequiredMixin, ListView):
    permission_required = 'backend.view_reclamation'
    model = Reclamation
    template_name = 'backend/reclamation/reclamation_car.html'

    def get_queryset(self):
        car = Mashins.objects.get(pk=self.kwargs["pk"])
        return Reclamation.objects.filter(mashins_c=car)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Mashins.objects.get(pk=self.kwargs["pk"])
        return context


class DescriptionReclamationView(TemplateView):
    template_name = 'backend/modal_description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reclamation = Reclamation.objects.get(pk=self.kwargs["pk"])
        atribute = context['atribute']
        if atribute == 'failure_node':
            context['atribute'] = reclamation.failure_node
            context['description'] = reclamation.failure_node.description
        elif atribute == 'recovery_method':
            context['atribute'] = reclamation.recovery_method
            context['description'] = reclamation.recovery_method.description
        elif atribute == 'mashins_c':
            context['atribute'] = reclamation.mashins_c
            context['description'] = reclamation.mashins_c.description 
        elif atribute == 'service':
            context['atribute'] = reclamation.service
            context['description'] = reclamation.service.description
        return context



class ListRepSerAPI(generics.ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class = TOSerializer
    queryset = TO.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class UserRepSerListAPI(generics.ListAPIView):
    serializer_class = TOSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class DetaiRepSerlAPI(generics.RetrieveAPIView):
    serializer_class = TOSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = TO.objects.get(pk=self.kwargs['pk'])
        return obj


class ListReclamationAPI(generics.ListAPIView):
    serializer_class = ReclamationSerializer
    queryset = Reclamation.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class UserReclamationListAPI(generics.ListAPIView):
    serializer_class = ReclamationSerializer

    def get_queryset(self):
        try:
            user = int(self.kwargs['user'])
        except:
            user = self.kwargs['user']
        if type(user) == int:
            queryset = Reclamation.objects.filter(car__client=user)
        elif type(user) == str:
            queryset = Reclamation.objects.filter(car__client__username=user)
        return queryset


class DetailReclamationAPI(generics.RetrieveAPIView):
    serializer_class = ReclamationSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj