from django.test import TestCase
import pytest

from rest_framework.test import APIClient
from rest_framework import status
from .models import StatusCheckResult


# Create your tests here.
@pytest.mark.django_db
def test_api_list_endpoint():
    client = APIClient()
    response = client.get("/api/results/")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_status_check_result_creation():
    result = StatusCheckResult.objects.create(
        service_name="Test Service",
        success=True,
        http_status_code=200,
        response_time_ms=120.5,
    )
    assert result.service_name == "Test Service"
    assert result.success == True
    assert StatusCheckResult.objects.count() == 1
