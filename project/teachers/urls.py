from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "teacher_profil"),
    path('group-details/<int:pk>/discipline/<int:pk1>/', views.GroupDetailView.as_view(), name = 'group_details')
]