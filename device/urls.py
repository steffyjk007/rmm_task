from django.urls import path
from . import views
from .views import DeviceCreateView, DeviceListCreateView, DeviceDetailView, DeviceListView2

urlpatterns = [
    path('api/get_device_data/', views.get_device_data, name='get_device_data'),
    path('device/add/', DeviceCreateView.as_view(), name='device-create'),
    # apis
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('devices-list/', DeviceListView2.as_view(), name='device-list2'),
]
