from rest_framework.response import Response
from rest_framework import status
from booklets.models import Booklet
from .serializers import BookletSerializer,UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,BasePermission




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    booklets=Booklet.objects.all()
    serializer=BookletSerializer(instance=booklets,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)




@api_view(["POST"])
def create(request):
    serializer=BookletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Booklet has been created succefully"
        },status=status.HTTP_201_CREATED )

    return Response(data={
        "success": False,
        "errors":serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)    



@api_view(["POST"])
def edit(request,id):
    booklet=Booklet.objects.get(pk=id)
    serializer=BookletSerializer(instance=booklet,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "Booklet has been Updated succefully"
            
        },status=status.HTTP_200_OK)

    return Response(data={
        "success": False,
        "errors":serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)  




@api_view(["Delete"])
def delete(request, id):  
    booklet = Booklet.objects.get(pk=id)  
    booklet.delete()  
    return Response("booklet has been deleted successfully")  





@api_view(["GET"])
def show(request,id):
    booklets=Booklet.objects.get(pk=id)
    serializer=BookletSerializer(instance=booklets,many=False)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

     


@api_view(["POST"])
def api_signup(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered succefully"
            
        },status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors":serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST) 
    
       
