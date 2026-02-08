from django.contrib import admin
from .models import Dataset

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "file_name",
        "uploaded_at",
        "total_equipment",
        "health_score",
    )

    ordering = ("-uploaded_at",)
