from django.urls import path

from feature.views.CategoryView import CategoryView

urlpatterns = [
    path('category', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view())
]
