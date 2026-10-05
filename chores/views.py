import os
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from .models import Chore

# Custom Application Metrics
APP_ENV = os.getenv('APP_ENV', 'dev')

CHORE_CREATIONS = Counter(
    'chores_created_total',
    'Total chores successfully created',
    ['environment']
)

CHORE_FAILURES = Counter(
    'chore_creation_failures_total',
    'Total failures during chore creation',
    ['environment']
)

ACTIVE_CHORES = Gauge(
    'chores_active_total',
    'Current number of incomplete chores',
    ['environment']
)

def metrics_view(request):
    """Exposes Prometheus scrape metrics."""
    ACTIVE_CHORES.labels(environment=APP_ENV).set(
        Chore.objects.filter(is_completed=False, is_deleted=False).count()
    )
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)

@csrf_exempt
def chore_list_api(request):
    if request.method == 'GET':
        chores = Chore.objects.filter(is_deleted=False)
        data = [
            {
                'id': chore.id,
                'name': chore.name,
                'description': chore.description,
                'frequency': chore.frequency,
                'is_completed': chore.is_completed,
            }
            for chore in chores
        ]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            name = body.get('name') or body.get('title')
            if not name:
                CHORE_FAILURES.labels(environment=APP_ENV).inc()
                return JsonResponse({'error': 'Name is required'}, status=400)

            frequency = body.get('frequency', 'daily').lower()
            description = body.get('description', '')

            chore = Chore.objects.create(
                name=name,
                frequency=frequency,
                description=description,
            )

            CHORE_CREATIONS.labels(environment=APP_ENV).inc()

            return JsonResponse({
                'id': chore.id,
                'name': chore.name,
                'description': chore.description,
                'frequency': chore.frequency,
                'is_completed': chore.is_completed,
            }, status=201)

        except Exception as e:
            CHORE_FAILURES.labels(environment=APP_ENV).inc()
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
