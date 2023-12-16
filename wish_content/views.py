from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

#포스트 메인페이지
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categoies'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

#포스트 상세페이지
class PostDetail(DetailView):
    model = Post

# 컨텐츠 페이지
def content(request):
    return render(request,'wish_content/content.html')

# 마이위시 페이지
def my_wish(request):
    return render(request, 'wish_content/my_wish.html')

def index(request):
    return render(request, 'wish_content/index.html')

# #포스트 메인페이지
# def index(request):
#     posts = Post.objects.all().order_by('-pk') # Post.objects.all() 이 방식으로 views.py에서 데이터베이스에 퀴리를 날려 원하는 레코드를 가져올 수 있어
#     return render(request, 'wish_content/index.html',
#                   {'posts':posts},
#                   )

# # 포스트 상세페이지
# def single_post_page(request, pk): # 매개변수가 request뿐이었던 index함수와 달리 single페이지 함수는 pk를 매개변수로 더 받는다.
#     post = Post.objects.get(pk=pk)
#     # Post 모델의 pk필드 값이 single_post_page() 함수의 매개변수로 받은 pk와 같은 레코드를 가져오라는 뜻

#     return render(request, 'wish_content/single_post_page.html',
#                   {'post':post}
#                   )

