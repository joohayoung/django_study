from django.contrib import admin
from .models import Post

#관리자 admin이 게시글post에 접근할 권한을 준다.
# Register your models here.

admin.site.register(Post)
