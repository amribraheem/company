from django.urls import path
from cuisine.api.views import (RestaurantListView,
                               MenuListView,
                               itemListView,
                               RestaurantDetailView,
                               MenuDetailView,
                               ItemDetailView,
                               MenuCreateView,
                               ItemCreateView,
                               RestaurantCreateView,
                               RestaurantDeleteView,
                               MenuDeleteView,
                               ItemDeleteView
                               )


urlpatterns = [
    path('restaurant/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurant/menu/', MenuListView.as_view(), name='menu-list'),
    path('restaurant/menu/items/', itemListView.as_view(), name='item-list'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(),
         name='restaurant-detail'),
    path('restaurant/menu/<int:pk>/',
         MenuDetailView.as_view(), name='menu-detail'),
    path('restaurant/menu/items/<int:pk>/',
         ItemDetailView.as_view(), name='item-detail'),
    path('restaurant/create/',
         RestaurantCreateView.as_view(), name='Restaurant-create'),
    path('restaurant/menu/create/',
         MenuCreateView.as_view(), name='menu-create'),
    path('restaurant/menu/items/create/',
         ItemCreateView.as_view(), name='item-create'),
    path('restaurant/<int:pk>/delete/',
         RestaurantDeleteView.as_view(), name='restaurant-delete'),
    path('restaurant/menu/<int:pk>/delete/',
         MenuDeleteView.as_view(), name='menu-delete'),
    path('restaurant/menu/items/<int:pk>/delete/',
         ItemDeleteView.as_view(), name='item-delete'),
]
