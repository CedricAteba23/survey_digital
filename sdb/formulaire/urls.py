from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('formulaire/', views.FormulaireList.as_view()),
    path('formulaire/<int:pk>/', views.FormulaireDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)