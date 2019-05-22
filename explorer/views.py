from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from .serializers import MedBlockSerializer
from .models import MedBlock
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.contrib.auth import views as auth_views

class HospitalView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'hospital.html'

class InsuranceView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'insurance.html'

class ExplorerView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'explorer.html'

class SupplyChainView(generic.TemplateView):
    template_name = 'explorer_tracking.html'
class ExplorerDetailView(generic.DetailView):
    def get_object(self):
        hash = self.kwargs['hash']
        return MedBlock.objects.get(hash=hash)
    context_object_name = 'medblock'
    template_name = 'explorer_detail.html'

# Pass hash in URL /medblock/<hash> 
class MedBlockDetailView(generics.RetrieveUpdateAPIView):
    lookup_field = 'hash'
    queryset = MedBlock.objects.all()
    serializer_class = MedBlockSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(MedBlockDetailView, self).get_serializer(*args, **kwargs)

class MedBlockListCreateView(generics.ListCreateAPIView):
    queryset = MedBlock.objects.all()
    serializer_class = MedBlockSerializer