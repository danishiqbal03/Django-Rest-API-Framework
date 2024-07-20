from django.http import JsonResponse
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer

# def api_home(req):
#     # if req.method == 'GET':
#     #     body = req.body #json string byte
#     #     data = {}
#     #     try:
#     #         data = json.loads(body) #converts json string byte to python dict
#     #     except:
#     #         pass

#     #     data['headers'] = dict(req.headers)

#     #     print(data['headers']['Content-Type'])
#     #     query = req.GET.get('query', None)
#     #     if query:
#     #         print(query)  # This will print the value of the query parameter
#     #         return JsonResponse({"msg": f"Received query: {query}"})
#     #     else:
#     #         return JsonResponse({"error": "No query parameter provided"}, status=400)
#     # return JsonResponse({"error": "Invalid request method"}, status=400)

#     if req.method == "GET":
#         data = Product.objects.all().order_by('?').first()
#         res = {}
#         # res['title'] = data.title
#         # res['content'] = data.content
#         # res['price'] = data.price
#         res = model_to_dict(data,fields=['id','title'])

#         return JsonResponse(res) #excepts dict as argument
#         #whereas HttpResponse excepts string as argument


# @api_view(['GET'])
# def api_home(req):
#     instance = Product.objects.all().order_by('?').first()
#     data={}
#     if instance:
#         # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()  # Save the validated data
        return Response(serializer.data)
    return Response(serializer.errors, status=400)  # Handle invalid data