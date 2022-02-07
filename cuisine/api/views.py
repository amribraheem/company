from tkinter import Menu
from cuisine.models import Restaurant, Menu, Item
from tenants.utils import get_tenant_from_request
from .serializers import RestaurantSerializer, MenuSerializer, ItemSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny


class RestaurantListView(ListAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        queryset = Restaurant.objects.filter(tenant=tenant)
        return queryset


class MenuListView(ListAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = MenuSerializer

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        queryset = Menu.objects.filter(tenant=tenant)
        return queryset


class itemListView(ListAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = ItemSerializer

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        queryset = Item.objects.filter(tenant=tenant)
        return queryset


class RestaurantDetailView(RetrieveUpdateAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        queryset = Restaurant.objects.filter(tenant=tenant)
        return queryset


class MenuDetailView(RetrieveUpdateAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = MenuSerializer

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        queryset = Menu.objects.filter(tenant=tenant)
        return queryset


class ItemDetailView(RetrieveUpdateAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = ItemSerializer

    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        queryset = Item.objects.filter(tenant=tenant)
        return queryset


# class IItemCreate(CreateAPIView):
#     serializer_class = ItemSerializer

#     def perform_create(self, serializer):
#         pk = self.kwargs['pk']
#         tenant = get_tenant_from_request(self.request)
#         item = Menu.objects.filter(tenant).filter(menu_items=pk)

#         return serializer.save(menu_item=item)
