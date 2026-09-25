import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chore

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
        except Exception:
            body = {}

        name = body.get('name') or body.get('title') or 'New Chore'
        frequency = body.get('frequency', 'daily').lower()
        description = body.get('description', '')

        chore = Chore.objects.create(
            name=name,
            frequency=frequency,
            description=description,
        )
        return JsonResponse({
            'id': chore.id,
            'name': chore.name,
            'description': chore.description,
            'frequency': chore.frequency,
            'is_completed': chore.is_completed,
        }, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
