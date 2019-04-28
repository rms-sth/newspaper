from django.views.generic import *
from django.urls import reverse_lazy, reverse
from .models import Post, Tag
from .forms import AdminNewsForm
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views.generic.edit import FormView




class AdminNewsListView(ListView):
    model = Post
    template_name = 'admintemplates/newsapp/newslist.html'
    # context_object_name ='news'


class AdminNewsDetailView(DetailView):
    model = Post
    template_name = 'admintemplates/newsdetail.html'


class AdminNewsCreateView(CreateView):
    form_class = AdminNewsForm
    template_name = 'admintemplates/newsapp/newscreate.html'
    success_url = reverse_lazy('newsapp:adminnewslist')

    def form_valid(self, form):
        user = self.request.user.id
        author = User.objects.get(id=user)
        form.instance.author = author
        form.instance.update_by = author
        return super().form_valid(form)


class AdminNewsUpdateView(UpdateView):
    model = Post
    form_class = AdminNewsForm
    success_url = reverse_lazy('newsapp:adminnewslist')
    template_name = 'admintemplates/newsapp/newsupdate.html'

    def form_valid(self, form):
        user = self.request.user.id
        author = User.objects.get(id=user)
        form.instance.author = author
        form.instance.update_by = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('newsapp:adminnewslist')


class AdminNewsDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('newsapp:adminnewslist')


class ClientHomeView(ListView):
    template_name = 'clienttemplates/clienthome.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(ClientHomeView, self).get_context_data(**kwargs)
        context['popularposts'] = Post.objects.all()[:5]
        context['latest'] = Post.objects.filter().order_by('-created_at')[0:1]
        context['latests'] = Post.objects.filter().order_by('-created_at')[0:4]
        return context


class ClientPostDetailView(DetailView):
    template_name = 'clienttemplates/clientnewsdetail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(ClientPostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ClientPostTopic(ListView):
    model = Post
    template_name = 'clienttemplates/clientnewstopic.html'

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return Post.objects.filter(topic=self.topic)

    def get_context_data(self, **kwargs):
        context = super(ClientPostTopic, self).get_context_data(**kwargs)
        context['topic'] = self.topic
        context['categories'] = Category.objects.all()
        return context


class ClientPostTag(ListView):
    model = Post
    template_name = 'clienttemplates/clientnewstag.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Post.objects.filter(tag=self.tag)

    def get_context_data(self, **kwargs):
        context = super(ClientPostTag, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        context['categories'] = Category.objects.all()
        return context


class ClientPostCategory(ListView):
    model = Post
    template_name = 'clienttemplates/clientnewscategory.html'

    # def get_queryset(self):
    #     self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
    #     return Post.objects.filter(tag=self.tag)

    def get_context_data(self, **kwargs):
        context = super(ClientPostCategory, self).get_context_data(**kwargs)
        # context['category'] = self.tag
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.filter(topic__category=self.kwargs['pk'])
        # post__category = Category.objects.get(id=self.kwargs['pk'])
        print(context['posts'])
        return context