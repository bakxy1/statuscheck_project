from celery import shared_task
import requests
import time
from .models import StatusCheckResult


@shared_task
def check_website_status(service_name, url):
    """
    Celery task to check the status of a single website
    """
    start_time = time.time()

    try:
        response = requests.get(url, timeout=10)
        response_time_ms = (time.time() - start_time) * 1000

        StatusCheckResult.objects.create(
            service_name=service_name,
            success=True,
            http_status_code=response.status_code,
            response_time_ms=response_time_ms,
        )
        return f"{service_name}: Success ({response.status_code})"
    except requests.exceptions.RequestException as e:
        response_time_ms = (time.time() - start_time) * 1000
        StatusCheckResult.objects.create(
            service_name=service_name,
            success=False,
            http_status_code=None,
            response_time_ms=response_time_ms,
        )
        return f"{service_name}: Failed ({e})"


@shared_task
def run_all_checks():
    sites_to_check = [
        {"name": "Google", "url": "https://www.google.com"},
        {"name": "GitHub", "url": "https://github.com"},
        {"name": "Hacker News", "url": "https://news.ycombinator.com"},
    ]
    print(f"Running checks for {len(sites_to_check)} sites...")
    for site in sites_to_check:
        check_website_status.delay(service_name=site["name"], url=site["url"])
