from .models import Blog
from .serializer import Blogserializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

'''
전체 블로그를 조회
'''
    # 함수형 뷰
# @api_view(['GET', 'POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def blog_list(request):
# 	if request.method == 'GET':
# 		blogs = Blog.objects.all()
# 		serializer = Blogserializer(blogs, many=True)
# 		return Response(serializer.data, status=status.HTTP_200_OK)
# 	elif request.method == 'POST':
# 		serializer = Blogserializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status = status.HTTP_201_CREATED)
# 	return Response(status=status.HTTP_400_BAD_REQUEST)

    # 클래스 뷰
# class BlogList(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get(self, request):
#         blogs = Blog.objects.all()
#         serializer = Blogserializer(blogs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = Blogserializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
'''
한 블로그 조회
'''

    #함수형 뷰
# @api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsOwnerOrReadOnly])
# def blog_detail(request, pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#         if request.method == "GET":
#             serializer = Blogserializer(blog)
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         elif request.method == 'PUT':
#             serializer = Blogserializer(blog, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#         elif request.method == 'DELETE':
#             blog.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
        
#     except Blog.DoesNotExist: # 예외(오류) 발생 시 아래 코드 실행
#         return Response(status=status.HTTP_404_NOT_FOUND)

    #클래스 뷰
# class BlogDetail(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsOwnerOrReadOnly]
#     def get_object(self, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         return blog

#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = Blogserializer(blog)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = Blogserializer(blog, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]