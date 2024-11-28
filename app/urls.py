from django.urls import path
from app import views

urlpatterns = [
    path('update/', views.ProductsUpdateAPIView.as_view(), name='async_products_update'),
]
