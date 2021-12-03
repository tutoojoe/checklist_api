from http.client import error
from django.http.response import Http404
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from .serializers import CheckListSerializer,CheckListItemSerializer
from .models import CheckList, CheckListItem
from .permissions import IsOwner


# Create your views here.

# trying function based views


# class CheckListsAPIView(APIView):
class CheckListsAPIView(ListCreateAPIView):

    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    
    """
    here listing and creation
    """

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset


"""
    the below is the actual functions runs when the list and create view happens.!
    by using generic views, this can be simplified to few lines of code

    def get(self, request, format=None):
        
        data = CheckList.objects.filter(user = request.user)
        # serializer = CheckListSerializer(data, many=True)
        serializer = self.serializer_class(data, many = True)
        serialized_data = serializer.data
        return Response(serialized_data)

    def post(self, request,format=None):
        #creation code
        print(request.data)
        serializer = self.serializer_class(data = request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""

# class CheckListAPIView(APIView):
class CheckListAPIView(RetrieveUpdateDestroyAPIView):

    """
    retrieval, updation, delete/destroy
    """

    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated,IsOwner]


    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset


"""
    this is the function runs behind the scene

    # we will first check whether the object is available or not
    def get_object(self, pk):
        try:
            obj = CheckList.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj

        except CheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response (serialized_data,status=status.HTTP_200_OK)
    
    def put(self, request, pk, format = None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response (serialized_data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""



# class CheckListItemCreateAPIView(APIView):
class CheckListItemCreateAPIView(CreateAPIView):

    """ 
    create checklist item
    
    """

    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = CheckListItemSerializer

"""   
    This is behind the scenes

 def post(self, request, format= None):
        #creation code    
        serializer = self.serializer_class(data = request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""



class CheckListItemAPIView(APIView):
    """
    retrieve, update, delete
    """

    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = CheckListItemSerializer

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset

"""
    def get_object(self, pk):
        try:
            obj = CheckList.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj

        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response (serialized_data,status=status.HTTP_200_OK)
    
    def put(self, request, pk, format = None):
        checklist_item= self.get_object(pk)
        serializer = self.serializer_class(checklist_item, data=request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response (serialized_data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""