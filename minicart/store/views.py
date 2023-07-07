from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductmodelSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action


# Create your views here.

class ProductView(APIView):
    
    def get(self,request):
        product=Product.objects.all()
        dser=ProductmodelSerializer(product,many=True)
        return Response(data=dser.data)
    def post(self,request):
        ser=ProductmodelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"success"})
        return Response(data=ser.errors)

class Specificview(APIView):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("id")
        product=Product.objects.get(id=did)
        dser=ProductmodelSerializer(product)
        return Response(data=dser.data)
    def put(self,request,*args,**kwargs):
        did=kwargs.get("id")
        product=Product.objects.get(id=did)
        ser=ProductmodelSerializer(data=request.data,instance=product)
        if ser.is_valid():
            ser.save
            return Response({"msg":"success"})
        return Response({"msg":"failed"})
    def delete(self,request,*args,**kwargs):
        did=kwargs.get("id")
        Product.objects.filter(id=did).delete()
        return Response({"msg":"deleted"})
    
class ProductVSet(ViewSet):
    def retrieve(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        prod=Product.objects.get(id=did)
        dser=ProcessLookupError(prod)
        return Response(data=dser.data)
    def list(self,request):
        prod=Product.objects.all()
        dser=ProductmodelSerializer(prod,many=True)
        return Response(data=dser.data)
    def create(self,request):
        ser=ProductmodelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def update(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        prod=Product.objects.get(id=did)
        ser=ProductmodelSerializer(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def destroy(self,request,*args,**kwargs):
        did=kwargs.get("pk")
        prod=Product.objects.get(id=did)
        prod.delete()
        return Response({"msg":"deleted"})
    @action(methods=['GET'],detail=False)
    def category(self,request,*args, **kwargs):
        cat=Product.objects.values_list('category',flat=True).distinct()
        return Response(data=cat)

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class ProductMVset(ModelViewSet):
    serializer_class=ProductmodelSerializer
    queryset=Product.objects.all()
    # authentication_classes=[BasicAuthentication]
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    
    
            
from .serializers import UsermodelSerializer

class UserVset(ViewSet):
    def create(self,request):
        ser=UsermodelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        return Response({"msg":"failed"})       