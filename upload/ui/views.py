# coding:utf-8

import os
import subprocess

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.conf import settings

from forms import OemResourcesForm



UPLOAD_FILE_PATH = '/tmp/nginx_upload/'
DOWMLOAD_FILE_PATH = '/tmp/nginx_download/'
def upload(request, template):
    if request.method == 'POST':
        resources = OemResourcesForm(request.POST, request.FILES)
        if resources.is_valid():
            save_file(request.FILES)
    else:
        resources = OemResourcesForm()

    return TemplateResponse(request, template, {'resources': resources})


def save_file(FILES):
    f = FILES['filename']
    filename = os.path.join(UPLOAD_FILE_PATH, f.name)
    with open(filename, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    generate_upgrad_package(filename)

def generate_upgrad_package(filename):
    # TO generata_package
    subprocess.call(['mv', filename, DOWMLOAD_FILE_PATH])
