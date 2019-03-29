from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url('api/postings/', include('api.urls')),
    url('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    url(r'blog/login/$', login_user, name="login_user"),
    url(r'blog/register/$', register_new_user, name="register_new_user"),
    url(r'blog/logout/$', User_Logout, name="user_logout"),
    url(r'blog/endzone/$', error404, name="error404"),
]
