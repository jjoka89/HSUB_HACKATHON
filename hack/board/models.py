from django.db import models
from account.models import Account
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 각 카데고리의 이름을 담는 필드
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  # 사람이 읽을 수 있는 텍스트로 고유 URL을 만들기 위해 만들어진 필드

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return f'/board/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'
        

class BigCategory(models.Model):
    bigname = models.CharField(max_length=50, unique=True)  # 각 카데고리의 이름을 담는 필드
    bigslug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  # 사람이 읽을 수 있는 텍스트로 고유 URL을 만들기 위해 만들어진 필드

    def __str__(self):
            return self.bigname

    class Meta:
        verbose_name_plural = 'BigCategories'
        
class DateCategory(models.Model):
    date = models.CharField(unique=True, max_length=20)
    
    def __str__(self):
        return self.date
    
    class Meta:
        verbose_name_plural = 'DateTime'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    big_category = models.ForeignKey(BigCategory, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Account,  on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL) 
    post_hit = models.PositiveIntegerField(default=0)
    date_category = models.ForeignKey(DateCategory, null=True, on_delete=models.SET_NULL)
    # null=True 는 필드의 값이 NULL(정보 없음)로 저장되는 것을 허용합니다. 결국 데이터베이스 열에 관한 설정
    # blank=True 는 필드가 폼(입력 양식)에서 빈 채로 저장되는 것을 허용
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/board/{self.pk}/'
    
    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()
        return f"" 
        
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'


