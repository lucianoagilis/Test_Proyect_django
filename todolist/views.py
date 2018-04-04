from django.views import View
from django.shortcuts import render, redirect
from todolist.models import Item
from . import forms


class ItemView(View):
    def get(self, request):
        items = Item.objects.all()
        context = {'items': items}
        return render(request, 'index.html', context)


class ModifyItemView(View):
    def post(self, request, pk):
        item = Item.objects.get(pk=pk)
        form = forms.MyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'item': item, 'form': form}
        return render(request, 'edit.html', context)

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        form = forms.MyForm(instance=item)
        context = {'item': item, 'form': form}
        return render(request, 'edit.html', context)

# Create your views here.
