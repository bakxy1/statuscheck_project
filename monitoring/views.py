from rest_framework import viewsets
from .models import StatusCheckResult
from .serializers import StatusCheckResultSerializer


# Create your views here.
class StatusCheckResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusCheckResult.objects.all().order_by("-checked_at")
    serializer_class = StatusCheckResultSerializer
