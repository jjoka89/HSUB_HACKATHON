from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category,Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import CommentForm
from django.contrib import messages
from django.db.models import Q

class PostList(ListView):
    model = Post #이렇게 선언하는 동시에 get_contexxt_data에서 자동으로 post_list = Post.objects.all()을 명령함 그래서  post_list.html에서 {% for %} 명령문을 바로 쓸 쑤 있음.
    #template_name = 'board/ShowPost.html' 
    ordering = '-pk'
    paginate_by = 5
    paginate_orphans = 3
    
    def get_context_data(self, **kwargs): #p326
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['pagelist'] = pagelist
        
        
        return context

class PostDetail(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs): #p326
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        context['comments'] = Comment.objects.filter(post = self.get_object())
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'category'] #카테고리 추가 예정  컴공게시판에 업로드할지 화공게시판에 업로드할지
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/board/')



        
        
class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title', 'content', 'category']  #카테고리 추가 예정  컴공게시판에 업로드할지 화공게시판에 업로드할지
    
    template_name = 'board/post_update_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
                return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
    

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category).order_by('-pk')
        

    return render(request, 'board/post_list.html',  # 템플릿은 포스트 목록 페이지를 만들 떄 사용했던 것을 그대로 사용
                {'post_list': post_list,  # post_list.html을 사용하기에 PostList 클래스에서
                'categories': Category.objects.all(),  # context로 정의했던 부분을 딕셔너리 형태로 직접 정의해야함.
                'no_category_post_count': Post.objects.filter(category=None).count(),
                'category': category
                }
                )
    

def search(request):
    blogs = Post.objects.all()

    q = request.POST.get('q', "") 

    if q:
        blog = blogs.filter( Q(title__icontains =q) | Q(content__icontains = q))
        return render(request, 'board/search_result.html', {'blogs' : blog, 'q' : q})
    
    else:
        return render(request, 'board/search_result.html')


def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
        
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    comment.delete()
    return redirect(post.get_absolute_url())

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # success_url = post.get_absolute_url()
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        
    else:
        post.like_users.add(request.user)
    return redirect(post.get_absolute_url())



