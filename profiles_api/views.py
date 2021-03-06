from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters #allows search by specific name
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated



from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    ''' Test Api Viewset'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''return a hello message'''

        a_viewset = [
        'usese actions(list, create, retrieve,update)',
        'automatically maps to urls using routers',
        'provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        '''create a new hello message'''

        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =  serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''Handle getting object by id'''
        return Response({'http_method':'GET'})

    def update(self, request,pk=None):
        '''handle updating object'''
        return Response({'http_method':'PUT'})

    def partial_update(self, request,pk=None):
        '''handle updating part of an object'''
        return Response({'http_method':'PATCH'})

    def destroy(self, request,pk=None):
        '''handle removing an object'''
        return Response({'http_method':'DELETE'})


#user registration
class UserProfileViewSet(viewsets.ModelViewSet):
    '''handle creating and updating profiles'''

    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)#to search objects by name, email or id
    search_fields = ('name','email',) #fields used to search and filter


#user login
class UserLoginApiView(ObtainAuthToken):
    '''creates user authentication token'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''handles creating reading updating profile feed items'''
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        '''sets the user profile to logged in user'''
        serializer.save(user_profile=self.request.user)
