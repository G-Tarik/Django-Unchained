from django.db.models import F
from django.shortcuts import redirect, render
from .models import Category, Item, Opinion
from .forms import OpinionForm, CategoryForm, ItemForm

PLUS1 = 1
MINUS1 = -1


def prepare_list(category_id):
    categories = Category.objects.all()
    try:
        category_selected = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        category_selected = None
    context = {'category_selected': category_selected, 'categories': categories}

    return context


def save_opinion(opinion, request):
    form = OpinionForm(request.POST, instance=opinion)
    if form.is_valid():
        new_opinion = form.save()
        update_opinions_counter(new_opinion.item_id, PLUS1)
        return redirect('opinion:show_opinion', opinion_id=new_opinion.id)

    return redirect('opinion:add_opinion', item_id=opinion.item_id)


def save_category_or_item(request, _model):
    models = {'category': CategoryForm, 'item': ItemForm}
    if request.method == 'POST':
        form = models[_model](request.POST)
        if form.is_valid():
            form.save()
            return redirect('opinion:list_all')
    else:
        form = models[_model]()

    context = {'form': form,
               'table': _model,
               'action_arg': _model,
               'action_url': 'opinion:add_category_or_item'}

    return render(request, 'opinion/add_form.html', context)


def delete_record(opinion_id):
    opinion = Opinion.objects.get(id=opinion_id)
    opinion.delete()
    update_opinions_counter(opinion.item_id, MINUS1)


def update_opinions_counter(item_id, direction):
    item = Item.objects.filter(id=item_id)
    item.update(opinions_number=F('opinions_number') + 1 * direction)
