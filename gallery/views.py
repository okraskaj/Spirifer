from django.views.generic import DetailView, ListView
from .models import Gallery


class GalleryListView(ListView):
    template_name = "gallery/list.html"
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        context['title'] = 'List of all galleries'
        return context

class GalleryDetailsView(DetailView):
    template_name = "gallery/details.html"
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gallery: " + str(context['post'])
        context['galleries'] = Gallery.objects.all()
        return context
