# # from django.db import models

# # class Dataset(models.Model):
# #     file_name = models.CharField(max_length=255)
# #     uploaded_at = models.DateTimeField(auto_now_add=True)

# #     total_equipment = models.IntegerField()

# #     avg_flowrate = models.FloatField()
# #     avg_pressure = models.FloatField()
# #     avg_temperature = models.FloatField()

# #     health_score = models.IntegerField()

# #     summary = models.JSONField()

# #     def __str__(self):
# #         return self.file_name

# from django.db import models

# from django.conf import settings

# class Dataset(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="datasets"
#     )

#     file_name = models.CharField(max_length=255)
#     total_equipment = models.IntegerField()
#     avg_flowrate = models.FloatField()
#     avg_pressure = models.FloatField()
#     avg_temperature = models.FloatField()
#     health_score = models.FloatField()
#     summary = models.TextField()
#     uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.conf import settings


class Dataset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="datasets"
    )

    file_name = models.CharField(max_length=255)

    total_equipment = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    health_score = models.FloatField()

    summary = models.JSONField()  # ✅ FIX IS HERE

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
