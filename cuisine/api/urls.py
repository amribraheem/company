from django.urls import path
from cuisine.api.views import (RestaurantListView,
                               MenuListView,
                               itemListView,
                               RestaurantDetailView,
                               MenuDetailView,
                               ItemDetailView,
                               IItemCreate
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
    # path('restaurant/<int:pk>/items/create/',
    #      ItemDetailView.as_view(), name='item-detail'),
]
