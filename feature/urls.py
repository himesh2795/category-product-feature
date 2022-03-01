from django.urls import path

from feature.views.CategoryView import CategoryView
from feature.views.ProductView import ProductView

urlpatterns = [
    path('category', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
    path('product', ProductView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
]
