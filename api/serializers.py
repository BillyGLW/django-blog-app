from rest_framework import serializers
from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogPost
		fields = [ 
			'author',
			'title',
			'content', 
			'created_date', 
			'article_image', 
		]





	# author = models.ForeignKey("blog.MyUser",on_delete = models.CASCADE,verbose_name = "Smith")
    # title = models.CharField(max_length = 50,verbose_name = "Lorem ipsum")
    # content = RichTextField()
    # created_date = models.DateTimeField(auto_now_add=True,verbose_name="Dorem sit")
    # article_image = models.FileField(blank = True,null = True,verbose_name="Amet")