# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework import permissions
# from .models import Extractors
#from .serializers import ExtractSerializer
import MeCab
class ExtractorsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # todos = Todo.objects.filter(user = request.user.id)
        # serializer = TodoSerializer(todos, many=True)
        return Response("Hello")
        #return Response("Hello", status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        content = request.data.get('content', '')
           # Initialize MeCab
        mecab = MeCab.Tagger('-Owakati')
        
        # Use MeCab to segment Japanese text into words
        words = mecab.parse(content).strip().split()
        length = len(words)
        
        return Response({'words': words, 'length': length})