from django.urls import path
from . import views

app_name = 'scand'

urlpatterns = [
    path('create/', views.ImageCreateView.as_view(), name="image-create-view"),
    path('search-form/', views.SearchFormView.as_view(), name="search-form"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('images/', views.ImageListView.as_view(), name="images"),
    path('images/<int:pk>/', views.ImageDetailView.as_view(), name="image-detail"),
    path('images/update/<int:pk>/', views.ImageUpdateView.as_view(), name="image-update"),
    path('images/pdf/', views.SavePDF.as_view(), name="save-pdf")
]