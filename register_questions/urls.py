from django.urls import path

from accounts.views import RegionListAPIView, DistrictListAPIView, CountryListAPIView
from .views import RegisterQuestionVariantCreateAPIView, RegisterQuestionCreateAPIView, RegisterQuestionStatistics

urlpatterns = [
    path('question/', RegisterQuestionCreateAPIView.as_view()),
    path('question-variant/', RegisterQuestionVariantCreateAPIView.as_view()),
    path('for-chart/', RegisterQuestionStatistics.as_view()),
    path('regions/', RegionListAPIView.as_view()),
    path('districs/', DistrictListAPIView.as_view()),
    path('country/', CountryListAPIView.as_view()),
]
