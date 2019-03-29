from django.urls import path
from .views import (
    productListView,
    productDetailView,
    productCreateView,
    productEditView,
    productDeleteView
    )

app_name = "product"
urlpatterns = [
    path('',productListView,name="product"),
    path('product/<int:id>',productDetailView, name="give_product_id"),
    path('product/create',productCreateView),
    path('product/<int:id>/edit',productEditView),
    path('product/<int:id>/delete',productDeleteView),
]