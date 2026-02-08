from django.urls import path
from .views import (
    CSVUploadAPIView,
    DatasetHistoryAPIView,
    LatestDatasetSummaryAPIView,
    DatasetPDFReportAPIView,
    RegisterAPIView,
   LoginAPIView,
)

urlpatterns = [
    path("upload/", CSVUploadAPIView.as_view(), name="csv-upload"),
    path("history/", DatasetHistoryAPIView.as_view(), name="dataset-history"),
    path("summary/latest/", LatestDatasetSummaryAPIView.as_view(), name="latest-summary"),
    path("report/<int:dataset_id>/", DatasetPDFReportAPIView.as_view(), name="dataset-report"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),

]
