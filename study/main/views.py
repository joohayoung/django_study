from django.shortcuts import render, redirect
from .models import Post # View에 Model(Post 게시글) 가져오기

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request,'main/index.html')

def blog(request):
    postlist = Post.objects.all() #모든 post를 가져와 postlist에 저장한다.
    return render(request,'main/blog.html', {'postlist':postlist}) #blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져온다.

def posting(request, pk):
    post=Post.objects.get(pk=pk) # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    return render(request, 'main/posting.html',{'post':post})   # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post':post})