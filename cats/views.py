from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from cats.forms import CatForm, ParentForm
from cats.models import Categories, Cat, Parent


# Create your views here.
class IndexView(TemplateView):
    template_name = 'cats/index.html'
    extra_context = {
        'title': 'Тоськин дом - главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Categories.objects.all()[:3]
        return context_data


# def index(request):
#     context = {
#         'object_list': Categories.objects.all()[:3],
#         'title': 'Тоськин дом - главная'
#     }
#     return render(request, 'cats/index.html', context)


# def categories(request):
#     context = {
#         'object_list': Categories.objects.all(),
#         'title': 'Все наши породы'
#     }
#     return render(request, 'cats/categories_list.html', context)


class CategoriesListView(ListView):
    model = Categories
    extra_context = {
        'title': 'Все наши породы'
    }

    def category_cats(request, pk):
        category_item = Categories.objects.get(pk=pk)
        context = {
            'object_list': Cat.objects.filter(category_id=pk),
            'title': f'Кошки породы: {category_item.name}'
        }
        return render(request, 'cats/cats.html', context)


class CatsListView(ListView):
    model = Cat
    fields = ('name', 'category',)
    success_url = reverse_lazy('cats:cats')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Categories.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Кошки породы: {category_item.name}'

        return context_data


class AllCatsListView(ListView):
    model = Cat
    fields = ('name', 'category',)
    success_url = reverse_lazy('cats:all_cats')


class CatCreateView(CreateView):
    model = Cat
    form_class = CatForm
    success_url = reverse_lazy('cats:categories')


class CatUpdateView(UpdateView):
    model = Cat
    form_class = CatForm

    # def get_success_url(self):
    #     return reverse('cats:cat_update', args=[self.kwargs.get('pk')])
    def get_success_url(self):
        return reverse('cats:cats', args=[self.object.category.pk])


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Cat, Parent, form=ParentForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class CatDeleteView(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:categories')
