from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Main route
    path('inventory/', views.load_inventory, name='load_inventory'),  # Inventory route
    path('shop/', views.load_shop_items, name='load_shop_items'),  # Shop route
    path('shop/buy/<int:item_code>/', views.buy_item, name='buy_item'),  # Buy item route
    path('shop/sell/<int:item_code>/', views.sell_item, name='sell_item'),  # Sell item route
    path('quests/', views.load_quests, name='load_quests'),  # Quests route
    path('enhance/<int:item_code>/', views.enhance_item, name='enhance_item'),  # New route for enhancing items

]
