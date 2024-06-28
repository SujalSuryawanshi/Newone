

from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, View, UpdateView
from .models import Choices,Post
from django.urls import reverse_lazy


class Home(View):
    def get(self,request):
        post=Post.objects.all()
        context={
            'post':post
        }
        return render(request,'index.html', context)
    
class AddPost(CreateView):
    model=Post
    template_name='addpost.html'
    fields='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context
    

class Edit(UpdateView):
    model=Post
    template_name='edit.html'
    fields='__all__'


class DeletePost(DeleteView):
      model=Post
      template_name='delete_item.html'
      success_url= reverse_lazy('home')
