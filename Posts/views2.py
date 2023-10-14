from django.views import generic
from .models import post

class PostList(generic.ListView):
    model = post

    # Context : post_list , object_list
    # templates :  post_list.html (in Posts Folder)


class PostDetail(generic.DetailView):
    model = post


class AddPost(generic.CreateView):
    model = post
    fields = ['author','title', 'content', 'tags', 'image']
    success_url = '/blog/'


class EditPost(generic.UpdateView):
    model = post
    fields = ['author','title', 'content', 'tags', 'image']
    success_url = '/blog/'
    template_name = 'Posts/edit_post.html'


class DeletePost(generic.DeleteView):
    model = post
    success_url = '/blog/'