from django.urls import path
#.은 현재 폴더에 있는 views.py를 사용할 수 있게 가져오라는 뜻
from . import views


urlpatterns = [
    path('blog/tag/<str:slug>/', views.tag_page),
    path('blog/category/<str:slug>/', views.category_page),
    path('my_wish/', views.my_wish),
    path('content/', views.content),
    path('blog/<int:pk>/', views.PostDetail.as_view()), #포스트상세페이지 CBV방식
    path('blog/', views.PostList.as_view()), #포스트 메인페이지 CBV방식
    path('', views.index),
    # path('', views.index), -- FBV방식
    # path('<int:pk>/', views.single_post_page), #FBV방식
]