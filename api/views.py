from rest_framework import generics
from blog.models import BlogPost

from .serializers import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
	pass
	lookup_field     = 'pk'
	queryset         = BlogPost.objects.all()
	serializer_class = BlogPostSerializer

	def get_queryset(self):
		return BlogPost.objects.all()


# non-buildin method
	# def get_object(self):
		# pk = self.kwargs.get("pk")
		# return BlogPost.objects.get(pk=pk)