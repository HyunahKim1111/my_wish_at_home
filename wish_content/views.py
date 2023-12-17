from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

#포스트 메인페이지
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 카테고리
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(request, 'wish_content/post_list.html',
                  {
                      'post_list': post_list,
                      'categories' : Category.objects.all(),
                      'no_category_post_count' : Post.objects.filter(category=None).count(),
                      'category' : category,
                  })

#태그
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(request, 'wish_content/post_list.html',
                  {
                      'post_list': post_list,
                      'tag' : tag,
                      'categories': Category.objects.all(),
                      'no_category_post_count' : Post.objects.filter(category=None).count(),
                  })



#포스트 상세페이지
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


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

