from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from rest_framework import generics
from .serializers import DeviceSerializer

from .forms import DeviceForm
from .models import Device


def get_device_data(request):
    devices = Device.objects.all()
    data = [{'device_name': device.device_name, 'status': device.status, 'last_update_time': device.last_update_time}
            for device in devices]
    return JsonResponse(data, safe=False)


class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device/device_form.html'

    def get_success_url(self):
        return reverse_lazy('device-list2')


# APIS


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceListView2(ListView):
    model = Device
    template_name = 'device/device_list.html'
    context_object_name = 'device_list'
