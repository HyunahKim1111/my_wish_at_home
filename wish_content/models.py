from django.db import models
import os

#포스트 메인 페이지
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
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
        return f'/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
