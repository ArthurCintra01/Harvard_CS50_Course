from random import choice
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import markdown2

from . import util

#class SearchEntryForm(forms.Form):
#    article = forms.CharField(label="Search entry")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entryName):
    en = util.get_entry(entryName)
    if en == None:
        html = markdown2.markdown("# Error\n \tYour requested page was not found")
    else:
        html = markdown2.markdown(en)
    with open('encyclopedia/templates/encyclopedia/temp.html', 'w') as f:
        f.write(html)
    return render(request, "encyclopedia/entry.html",{
        "name" : entryName
    })

def random(request):
    random_name =choice(util.list_entries())
    random_entry = util.get_entry(random_name)
    html = markdown2.markdown(random_entry)
    with open('encyclopedia/templates/encyclopedia/temp.html', 'w') as f:
        f.write(html)
    return render(request, "encyclopedia/entry.html" , {
        "name" : random_name
    })
