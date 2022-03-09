from django.urls import path
from .views import CaseListView, CaseDetailsView, StepDetailsView, StepListView

urlpatterns = [
    path('cases/', CaseListView.as_view()),
    path('cases/<int:id>/', CaseDetailsView.as_view()),
    path('steps/', StepListView.as_view()),
    path('steps/<int:id>/', StepDetailsView.as_view())
]