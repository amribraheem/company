from cuisine.models import Restaurant, Menu, Item
from tenants.utils import get_tenant_from_request
from django.shortcuts import get_object_or_404
from .serializers import RestaurantSerializer, MenuSerializer, ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny


class RestaurantListView(ListAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.tenantfilterobject.filter_by_tenant(self.request)
        return queryset


class MenuListView(ListAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.tenantfilterobject.filter_by_tenant(self.request)
        return queryset


class itemListView(ListAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.tenantfilterobject.filter_by_tenant(self.request)
        return queryset


class RestaurantDetailView(RetrieveUpdateAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.tenantfilterobject.filter_by_tenant(self.request)
        return queryset


class MenuDetailView(RetrieveUpdateAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.tenantfilterobject.filter_by_tenant(self.request)
        return queryset


class ItemDetailView(RetrieveUpdateAPIView):
    permissions_classes = (AllowAny, )
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.tenantfilterobject.filter_by_tenant(self.request)
        return queryset


class RestaurantCreateView(APIView):
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MenuCreateView(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ItemCreateView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RestaurantDeleteView(APIView):

    def delete(self, request, pk):
        tenant = get_tenant_from_request(self.request)
        queryset = Restaurant.objects.filter(tenant=tenant)
        restaurant = get_object_or_404(queryset, pk=pk)
        restaurant.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class MenuDeleteView(APIView):

    def delete(self, request, pk):
        tenant = get_tenant_from_request(self.request)
        queryset = Menu.objects.filter(tenant=tenant)
        menu = get_object_or_404(queryset, pk=pk)
        menu.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ItemDeleteView(APIView):

    def delete(self, request, pk):
        tenant = get_tenant_from_request(self.request)
        queryset = Item.objects.filter(tenant=tenant)
        item = get_object_or_404(queryset, pk=pk)
        item.delete()
        return Response(status=HTTP_204_NO_CONTENT)
