from django import forms
from material import Layout, Fieldset, Column, Row, Span10, Span6, Span3, Span2
from .widgets import DefaultTextFieldWidget


class VagrantForm(forms.Form):

    base_box = forms.ChoiceField(
        choices=(('centos7', 'bento/centos-7'), ('debian8.2', 'bento/debian-8.2')),
        label='Base box',
        widget=forms.RadioSelect)

    u"""Machine Details"""
    machine_name = forms.CharField(label='Machine name', initial='machine', widget=DefaultTextFieldWidget)
    check_updates = forms.BooleanField(label='Automatically check updates', required=False)

    u"""Network"""
    guest_port = forms.CharField(label='Guest port', max_length='4')
    host_port = forms.CharField(label='Host port', max_length='4')
    mac_address = forms.CharField(label='MAC address', max_length='12', required=False)

    u"""Synced folder"""
    folder_source = forms.CharField(label='Folder source', initial='./')
    folder_target = forms.CharField(label='Folder target', initial='/var/www')
