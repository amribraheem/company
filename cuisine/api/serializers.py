from rest_framework import serializers
from cuisine.models import Restaurant, Menu, Item


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        # fields = ("__all__")
        exclude = ("pub_date", "last_updated")


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        # fields = ("__all__")
        exclude = ("pub_date", "last_updated")


class MenuSerializer(serializers.ModelSerializer):
    menu_items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        # fields = ("__all__")
        exclude = ("pub_date", "last_updated")
