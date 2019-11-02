from django.views.generic import TemplateView
from gallery.models import Gallery
from posts.models import Post


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['galleries'] = Gallery.objects.all()
        # context['events'] = Events.objects.all()
        context['title'] = 'Homepage'
        return context
