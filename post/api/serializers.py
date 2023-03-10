from rest_framework import  serializers

from ..models import Prods, Category


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model=Category
        fields=["title","id"]

class ProdsCatSerializer(serializers.ModelSerializer):

    category=CategorySerializer()
    class Meta:
        model=Prods
        fields=["id","name","price","category","image","description","sale"]



class ProdsSerializer(serializers.ModelSerializer):

    #def to_representation(self, instance):
        #response = super().to_representation(instance)
        #response['category'] = CategorySerializer(instance.category).data
        #return response

    class Meta:
        model=Prods
        fields=["id","name","price","category","image","description","sale"]

