from django.forms import ModelForm
from .models import Opinion, Category, Item


class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = ('item', 'title_text', 'message_text')
        labels = {
            'title_text': 'Title',
            'message_text': 'Message',
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name_text', 'description_text')
        labels = {
            'name_text': 'Name',
            'description_text': 'Description',
        }


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name_text', 'description_text', 'category', 'type_text')
        labels = {
            'name_text': 'Name',
            'description_text': 'Description',
            'category': 'Category',
            'type_text': 'Type'
        }
