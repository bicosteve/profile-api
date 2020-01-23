from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''test api view'''

    def get(self,request,format=None):
        '''returns a list of apiview features'''

        api_view = [
            'methods are post,put, get, patch',
            'is cool to learn',
            'mapped on urls',
        ]

        return Response({'message':'hello','api':api_view})