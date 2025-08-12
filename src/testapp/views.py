from django.shortcuts import render
from . import forms

# Create your views here.
def main_test(request):
    page_title = 'Test Page'
    html_template = 'htmx/htmx_contact_form.html'

    context = {
        'page_title': page_title,
    }
    return render(request, html_template, context)

def contact_form(request, *args, **kwargs):
    page_title = 'Contact Form'
    html_template = 'htmx/htmx_contact_form.html'

    if request.method == 'POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            # do_something_with_form_data(form.cleaned_data)
            return render(request, 'htmx/htmx_contact_form_confirm.html')
    else:
        form = forms.NameForm()

        context = {
            'form': form,
            'page_title': page_title,
        }
    return render(request, html_template, context)

def contact_form_only(request, *args, **kwargs):
    if request.method == 'POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            # do_something_with_form_data(form.cleaned_data)
            return render(request, 'htmx/htmx_contact_form_confirm.html')
    else:
        form = forms.NameForm()
        html_template = 'htmx/htmx_contact_form_only.html'

        context = {
            'form': form,
        }
    return render(request, html_template, context)