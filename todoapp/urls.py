from django.urls import path
from . import views

urlpatterns = [
    path('world/', views.myworld),
    path('product/', views.ListProductAPIView.as_view(), name='products'),
    path('create/', views.createProductAPIView.as_view(), name='products'),
    path('update/<int:pk>', views.updateProductAPIView.as_view(), name='products'),
    path('delproduct/<int:pk>',
         views.destroyProductAPIView.as_view(), name='products'),
]
