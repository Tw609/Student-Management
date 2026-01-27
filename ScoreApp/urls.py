from django.urls import path
from . import views

urlpatterns = [
    path('',views.score_list,name="score_list"),
    path('add/',views.score_add,name="score_add"),
    path('edit/<int:index>',views.score_edit,name="score_edit"),
    path('delete/<int:index>',views.score_delete,name="score_delete"),
]
