from django.conf.urls import url, include
from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from blog.views import *

app_name = "blog"

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact_blog, name="contact_blog"),
    path('about/', personal_blog, name="personal_blog"),
    path('panel/', Blog_Posting.as_view(), name="admin_panel"),
    path('panel/save', post_new, name="post_new"),
    path('account/create/', register_new_user, name="register_new_user"),
    path('404/', error404, name="error404"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)