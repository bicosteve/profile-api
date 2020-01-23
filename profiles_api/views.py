from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profiles_api import serializers


class HelloApiView(APIView):
    '''test api view'''

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        '''returns a list of apiview features'''

        api_view = [
            'methods are post,put, get, patch',
            'is cool to learn',
            'mapped on urls',
        ]

        return Response({'message':'hello','api':api_view})


    def post(self,request):
        '''create a hello message with our name'''

        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        '''updating an object'''

        return Response({'method':'PUT'})


    def patch(self, request,pk=None):
        '''updating partial part of an object'''

        return Response({'method':'PATCH'})

    def delete(self, request,pk=None):
        '''deletes an object'''
        return Response({'method':'DELETE'})
