from django.urls import path
from . import views
from .views import finchesList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', finchesList.as_view(), name='finches_index'),
    path('finches/create/', views.finchesCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.finchesUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.finchesDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/', views.finches_detail, name='finch_detail'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]
