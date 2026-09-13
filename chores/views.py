from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chore

@csrf_exempt
def chore_list_api(request):
    if request.method == 'GET':
        chores = list(Chore.objects.filter(is_deleted=False).values('id', 'title', 'is_completed'))
        return JsonResponse(chores, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        chore = Chore.objects.create(title=data.get('title', ''))
        return JsonResponse({'id': chore.id, 'title': chore.title, 'is_completed': chore.is_completed}, status=201)