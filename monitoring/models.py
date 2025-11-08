from django.db import models


# Create your models here.
class StatusCheckResult(models.Model):
    service_name = models.CharField(max_length=100)
    success = models.BooleanField()
    http_status_code = models.PositiveIntegerField(null=True, blank=True)
    response_time_ms = models.FloatField(null=True, blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        status = "Success" if self.success else "Failed"
        return f"{self.service_name} - {status} at {self.checked_at.strftime('%Y-%m-%d %H:%M')}"
