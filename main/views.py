from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloWorldSerializer
from .models import HelloWorldModel


class HelloWorldView(APIView):
    def get(self, request):
        obj = HelloWorldModel.objects.all() 
        seralizers = HelloWorldSerializer(obj, many=True)

        return Response(data=seralizers.data, status=200)