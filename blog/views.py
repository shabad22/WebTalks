from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from users.models import Profile
from django.contrib.auth.models import User


def bloggers(request):
    bloggers = User.objects.exclude(id=request.user.id)
    context = {
        'bloggers' : bloggers
    }
    return render(request, 'blog/bloggers.html', context)
        

def comments(request):
    return render(request, 'blog/comments.html')

def home(request): 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-Date_posted']
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Title__icontains=query)

        else:
            object_list = Post.objects.all().order_by('-Date_posted')
        return object_list

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Title','Content']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Title','Content']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False
    

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})