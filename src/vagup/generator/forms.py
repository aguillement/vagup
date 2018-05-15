from django import forms
from material import Layout, Fieldset, Column, Row, Span10, Span6, Span3, Span2


class VagrantForm(forms.Form):

    base_box = forms.ChoiceField(
        choices=(('centos7', 'bento/centos-7'), ('debian8.2', 'bento/debian-8.2')),
        label='Base box',
        widget=forms.RadioSelect)

    u""" Personal Details """
    machine_name = forms.CharField(label='Machine name', default='machine1')
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    parent_name = forms.CharField(label='In case of a minor please provide details')

    layout = Layout(
        'base_box',
        Fieldset("Personal Details (Sole/First Accountholder/Minor)",
                 Row(Span2('full_name'), Span2('full_name')),
                 Row(Column('date_of_birth',
                            'email',
                            'parent_name'))),
    )
