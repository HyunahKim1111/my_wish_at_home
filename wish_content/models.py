from django.db import models

#포스트 메인 페이지
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='wish_content/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='wish_content/files/%Y/%m/%d/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time = models.DateField(auto_now=True)

    # 관리자페이지에서 글을 문자로 뿌려주는 역할
    def __str__(self):
        return f'[{self.pk}]{self.title}{self.time}'
    #메인페이지에서 제목을 클릭하면 상세페이지로 넘어가는 url
    def get_absolute_url(self):
        return f'wish_content/{self.pk}/'
