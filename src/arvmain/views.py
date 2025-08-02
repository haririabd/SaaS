from django.shortcuts import render

def index_view(request, *args, **kwargs):
    page_title = 'Homepage'
    html_template = 'index.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)

def about_view(request, *args, **kwargs):
    page_title = 'About'
    html_template = 'index.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)