from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(
        label="Your name", max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-10/10 border border-red-50 bg-white-100",
            }))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 3,
            "class": "w-10/10 border border-red-50 bg-white-100",
        }),
            help_text='You can message me about anything you want. '
        )
    sender = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-10/10 border border-red-50 bg-white-100",
        }
        )
    )

def clean_message(self):
    # Accept any message, unless it contains the word 'chimera'
    message = self.cleaned_data['message']
    if 'chimera' in message.lower():
        raise forms.ValidationError('What did I tell you about chimeras?!')
    return message