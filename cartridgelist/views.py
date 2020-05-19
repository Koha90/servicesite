from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Cartridges


def index(request):
    carts = Cartridges.objects.all().count()
    return render(request,
                  'index.html',
                  {'carts': carts})


class ClientCartridgeRepairs(LoginRequiredMixin, generic.ListView):
    model = Cartridges
    template_name = 'cartridgelist/cartridge_list_in_repairs.html'

    def get_queryset(self):
        return Cartridges.objects.filter(client=self.request.user).order_by('date_of_repairs')