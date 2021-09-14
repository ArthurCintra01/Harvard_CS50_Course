from random import choice
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import markdown2

from . import util

class SearchEntryForm(forms.Form):
    search_entry = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'search', 'placeholder':'Search'}))

def updateTemp(entryName):
    en = util.get_entry(entryName)
    if en == None:
        html = markdown2.markdown("# Error\n \tYour requested page was not found")
    else:
        html = markdown2.markdown(en)
    with open('encyclopedia/templates/encyclopedia/temp.html', 'w') as f:
        f.write(html)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : SearchEntryForm()
    })

def entry(request, entryName):
    updateTemp(entryName)
    return render(request, "encyclopedia/entry.html",{
        "name" : entryName,
        "form" : SearchEntryForm()
    })

def random(request):
    random_name =choice(util.list_entries())
    updateTemp(random_name)
    return render(request, "encyclopedia/entry.html" , {
        "name" : random_name,
        "form" : SearchEntryForm()
    })


def search(request):
    if request.method == 'POST':
        form = SearchEntryForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search_entry']
            updateTemp(search)                          
            return render(request, "encyclopedia/entry.html", {
                "name" : search,
                "form" : SearchEntryForm()
            })     
        else:
            return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "form" : SearchEntryForm()
            })
                