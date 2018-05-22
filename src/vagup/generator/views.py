
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def index(request):
    return render_to_response('index.html')


def generator(request):
    u"""Generate vagrantfile."""

    if request.method == 'POST':
        data = request.POST
        response = HttpResponse(content_type='text')
        response['Content-Disposition'] = 'attachment; filename="Vagrantfile"'

        response.write('# -*- mode: ruby -*- \n')
        response.write('# vi: set ft=ruby : \n\n')
        response.write('Vagrant.configure("2") do |config| \n\n\t')

        # Base box
        response.write('config.vm.box = "{}"\n\n\t'.format(data['base_box']))

        # Machine name
        response.write('config.vm.provider "virtualbox" do |v| \n\t\t')
        response.write('v.memory = {}\n\t\t'.format(data['memory'])) if data['memory'] else None
        response.write('v.name="{}"\n\t'.format(data['machine_name']))
        response.write("end \n\n\t")

        # Box check update
        if not data.getlist('auto_update'):
            response.write('config.vm.box_check_update = false\n\t')
        else:
            response.write('config.vm.box_check_update = true\n\t')

        # Network
        response.write('config.vm.network "public_network", guest: {}, host:{}'.format(data['guest_port'], data['host_port']))

        if data['mac_address']:
            response.write(', :mac => "{}"'.format(data['mac_address']))
        response.write('\n\t')

        # Synced folder
        response.write('config.vm.synced_folder "{}", "{}" \n\n\t'.format(data['source_folder'], data['target_folder']))

        # Provision yum|apt
        provision(response, data)

        # Provision python

        response.write("end")
        return response

    return render(request, 'generator/generate.html')


def provision(response, data):
    u"""YUM / APT provision"""

    response.write('config.vm.provision "shell", inline: <<-SHELL\n\t\t')
    response.write('sudo su\n\t\t')

    if data['base_box'] == 'bento/centos7':
        base_command = "yum install -y"

    else:
        base_command = "apt-get install --assume-yes"
        response.write('apt-get update\n\t\t')

    if data['packages']:
        packages = data['packages'].split('\\')
        response.write('{} '.format(base_command))
        for each in packages:
            response.write('{} '.format(each))
        response.write('\n\t')

    if data.getlist('pgsql10'):
        response.write('yum install -y postgresql10 postgresql10-server\n\n\t\t')
        response.write('su - postgres -c "createuser --createdb --no-superuser --createrole --no-password {}\n\t\t'.format(data['username']))
        response.write('su - {} -c "createdb -O {} {}" \n\t'.format(data['username'], data['username'], data['database_name']))

    return response
