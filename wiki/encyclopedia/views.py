from django.shortcuts import render
from django import forms
import markdown2

from . import util


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
