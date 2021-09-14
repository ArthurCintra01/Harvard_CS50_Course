from random import choice
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import markdown2
from . import util

#forms
class SearchEntryForm(forms.Form):
    search_entry = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'search', 'placeholder':'Search'}))

class createPageForm(forms.Form):
    title = forms.CharField(label='title')
    page = forms.CharField(label=False, widget=forms.Textarea(attrs={ 'placeholder':'Page' }))

#utilities
def updateTemp(entryName):
    en = util.get_entry(entryName)
    if en == None:
        html = markdown2.markdown("# Error\n \tYour requested page was not found")
    else:
        html = markdown2.markdown(en)
    with open('encyclopedia/templates/encyclopedia/temp.html', 'w') as f:
        f.write(html)

#view functions
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
    return HttpResponseRedirect(f"wiki/{random_name}") 


def search(request):
    searchresults = []
    if request.method == 'POST':
        form = SearchEntryForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search_entry']
            for entry in util.list_entries():
                if (search == entry):
                    updateTemp(search)         
                    return HttpResponseRedirect(f"wiki/{search}")  
                elif (search.lower() in entry.lower()):
                    searchresults.append(entry)

            return render(request, "encyclopedia/search.html",{
                "searchresults" : searchresults,
                "form" : SearchEntryForm()
            })   
        else:
            return HttpResponseRedirect(reverse('wiki:index'))
                
def createPage(request):
    if request.method == 'POST':
        form = createPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            for entry in util.list_entries():
                if title.lower() == entry.lower():
                    html = markdown2.markdown("# Error\n \tAn encyclopedia entry already exists with the provided title!")
                    with open('encyclopedia/templates/encyclopedia/temp.html', 'w') as f:
                        f.write(html)
                    return render(request, "encyclopedia/entry.html",{
                        "name" : 'Error',
                        "form" : SearchEntryForm()
                     })
            page = form.cleaned_data['page']
            util.save_entry(title,page)
            return HttpResponseRedirect(f"wiki/{title}")
    return render(request, "encyclopedia/createPage.html", {
        'form' : SearchEntryForm(),
        'createForm' : createPageForm()
    })

def editPage(request, entryName):
    initial = {'title':entryName, 'page': util.get_entry(entryName)}
    editform = createPageForm(initial=initial)
    return render(request, "encyclopedia/editPage.html", {
        'form': SearchEntryForm(),
        'editForm' : editform,
        'name': entryName
    })

def postEdit(request):
    if request.method == 'POST':
        editform = createPageForm(request.POST)
        if editform.is_valid():
            title = editform.cleaned_data['title']
            page = editform.cleaned_data['page']
            util.save_entry(title,page)
            return HttpResponseRedirect(f"wiki/{title}")