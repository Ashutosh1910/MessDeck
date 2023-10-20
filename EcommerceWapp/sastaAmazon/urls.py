from django.urls import path
from . import views
from .views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView

urlpatterns = [
    path('',views.homepage,name="AppHome" ),
     path('productpage/',ProductListView.as_view(),name="ProductsPage"),
     path('product/<int:pk>/',ProductDetailView.as_view(),name="ProductPage"),
     path('product/new/',ProductCreateView.as_view(),name="ProductAddPage"),
     path('product/<int:pk>/update/',ProductUpdateView.as_view(),name="ProductUpdatePage"),
     path('product/<int:pk>/delete/',ProductDeleteView.as_view(),name="ProductDeletePage")



     ]
    

        

