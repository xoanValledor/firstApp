from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.
def post_list(request):
#         return render(request, 'catalog/post_list.html', {})
#     obj = {"a": 1, "b": 2}
#     return render(request, 'catalog/post_list.html', {"obj_as_json": json.dumps(obj)})
#     return HttpResponse(json.dumps(obj), content_type='application/json')

    data = {
        'name': 'Pablo',
        'location': 'MAdrid',
        'is_active': True,
        'pinchazos': 28,
        
         'MAC': '00:75:6C:00:34:C9',
    }
    return JsonResponse(data)