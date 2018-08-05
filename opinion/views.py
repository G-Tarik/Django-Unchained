from django.shortcuts import render, redirect, get_object_or_404
from django.forms import HiddenInput
from django.http import HttpResponseNotFound
import opinion.data_handler as dh
from .models import Opinion, Item
from .forms import OpinionForm

TABLES = ['category', 'item']


def list_all(request):
    category_id = request.GET.get('filter', '')
    context = dh.prepare_list(category_id)

    return render(request, 'opinion/list_all.html', context)


def show_opinion(request, opinion_id):
    opinion = get_object_or_404(Opinion, id=opinion_id)
    context = {'opinion': opinion}

    return render(request, 'opinion/show_opinion.html', context)


def add_opinion(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    opinion = Opinion(item=item, category=item.category)
    if request.method == 'POST':
        render_target = dh.save_opinion(opinion, request)
    else:
        form = OpinionForm(instance=opinion)
        form.fields['item'].queryset = Item.objects.filter(category_id=item.category_id)
        context = {'form': form, 'table': 'opinion',
                   'action_url': 'opinion:add_opinion', 'action_arg': item_id}
        render_target = render(request, 'opinion/add_form.html', context)

    return render_target


def edit_opinion(request, opinion_id):
    opinion = get_object_or_404(Opinion, id=opinion_id)
    if request.method == 'POST':
        render_target = dh.save_opinion(opinion, request)
    else:
        form = OpinionForm(instance=opinion)
        form.fields['item'].widget = HiddenInput()
        context = {'form': form, 'opinion_id': opinion_id, 'item_name': opinion.item.name_text}
        render_target = render(request, 'opinion/edit_opinion.html', context)

    return render_target


def add_category_or_item(request, table):
    if table not in TABLES:
        HttpResponseNotFound('<p><Wrong URL/p>')
    render_target = dh.save_category_or_item(request, table)

    return render_target


def delete_opinion(request):
    if request.method == 'POST':
        Opinion.objects.filter(id=request.POST['op_id']).delete()

    return redirect('opinion:list_all')
