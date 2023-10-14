from django.views import generic
from .models import post

class PostList(generic.ListView):
    model = post

    # Context : post_list , object_list
    # templates :  post_list.html (in Posts Folder)

class PostDetail(generic.DetailView):
    model = post