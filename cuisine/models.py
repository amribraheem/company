from pydoc import describe
from django.db import models
from tenants.models import TenantAwareModel


class Restaurant(TenantAwareModel):
    name = models.CharField(max_length=100)
    describtion = models.CharField(max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Menu(TenantAwareModel):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    rest = models.ForeignKey(
        Restaurant, related_name='rest', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(TenantAwareModel):
    menu_items = models.ForeignKey(
        Menu, related_name="menu_items", on_delete=models.CASCADE, null=True)
    menu_item = models.CharField(max_length=255)
    Ingredients = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_item
