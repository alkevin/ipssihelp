from django import forms


class AdForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '3'
            }
        )
    )
    type = forms.ChoiceField(
        label='Category',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=(
            ("1", "Demand"),
            ("2", "Supply"),
        )
    )
