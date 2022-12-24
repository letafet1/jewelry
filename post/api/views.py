from rest_framework.decorators import  api_view
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ProdsSerializer,ProdsCatSerializer
from post.models import Prods, Category





class ProdsTheListView(generics.ListAPIView):
    queryset = Prods.objects.all()
    serializer_class = ProdsCatSerializer


class ProdsListView(generics.ListAPIView):
    queryset = Prods.objects.all()
    serializer_class = ProdsSerializer


@api_view(['GET'])
def prods_list_view(request):

    if request.method == 'GET':
        prods = Prods.objects.all()
        serializer = ProdsSerializer(prods, many=True)
        return Response(serializer.data)
