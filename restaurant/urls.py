from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>', views.display_menu_item, name='menu_item'),
    path('book/', views.book, name='book'),
    path('api/menu/', views.MenuItemsView.as_view(), name='api_menu'),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view(), name='api_menu_item'),
    path('api-token-auth/', obtain_auth_token),
]
