from django.shortcuts import render
from rest_framework.views import APIView,Response
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
# Create your views here.

# class PostlistView(APIView):
#   def get(self,request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts,many=True)
#     return Response(serializer.data)

## LIST VIEW
# class PostListApiView(ListAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer


## CREATE VIEW 
# class PostCreateAPIView(CreateAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer


# LIST AND CREATE IN A VIEW 

# class PostListCreateAPIView(ListCreateAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly]


# FOR DETAILS -----------------------------------------------------------------
# class PostDetailView(RetrieveAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer

# # DELETE VIEW----------------------------
# class PostDeleteAPIView(DestroyAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer

# # UPDATE -------------------------------
# class PostUpdateAPIView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

## 3 view in a view -------------------------------- 
# class PostDetailView(RetrieveUpdateDestroyAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer
#   permission_classes = [IsAuthorOrReadOnly]



#_____________________________________________________________
# ALL IN ONE 

class PostSetView(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly]

