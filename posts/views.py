from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['title'] = 'List of all posts'
        return context


class PostDetailsView(DetailView):
    template_name = "posts/details.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Post: " + str(context['post'])
        context['posts'] = Post.objects.all()
        return context
