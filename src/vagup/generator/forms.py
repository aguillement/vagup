from django import forms
from material import Layout, Row, Span5, Fieldset, Column, Span10, Span2


class VagrantForm(forms.Form):

    os = forms.ChoiceField(
        choices=(('bento', 'bento/centos-7'), ('C', 'Cumulative')),
        label='Base box',
        widget=forms.RadioSelect)

    layout = Layout('e')
