from django.urls import path
from core.views import CheckListsAPIView,CheckListAPIView,CheckListItemCreateAPIView,CheckListItemAPIView

urlpatterns = [
    
    path('api/checklists/',CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/',CheckListAPIView.as_view()),
    path('api/checklistitem/create/',CheckListItemCreateAPIView.as_view()),
    path('api/checklistitem/<int:pk>/',CheckListItemAPIView.as_view()),


]
