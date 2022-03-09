from django.urls import path
from .views import CaseListView, CaseDetailsView

urlpatterns = [
    path('cases/', CaseListView.as_view()),
    path('cases/<int:id>/', CaseDetailsView.as_view())
]