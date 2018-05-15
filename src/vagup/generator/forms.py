from django import forms
from material import Layout, Fieldset, Column, Row, Span10, Span6, Span3, Span2


class VagrantForm(forms.Form):

    base_box = forms.ChoiceField(
        choices=(('centos7', 'bento/centos-7'), ('debian8.2', 'bento/debian-8.2')),
        label='Base box',
        widget=forms.RadioSelect)

    u""" Personal Details """
    machine_name = forms.CharField(label='Machine name', initial='machine')

    layout = Layout(
        'base_box',
        Fieldset("Personal Details (Sole/First Accountholder/Minor)",
                 Row('machine_name'),
        ),
    )
