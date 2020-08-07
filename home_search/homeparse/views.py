from django.shortcuts import render
from django.template import loader
from pathlib import Path

from django.http import HttpResponse
import requests
import re


def index(request):
    path = r'C:\Users\explod\PycharmProjects\\real_estate_bot\\base\\'
    files = ['era_base.txt', 'fastighets_base.txt', 'lansfast.txt', 'svenskfast_base.txt']
    all_links = []
    for file in files:
        with open(Path(path+file)) as file_read:
            links = file_read.readlines()
            for link in links:
                r = requests.get(str(link.replace("\n", "")))
                if 'era_base' in file:
                    pic_link = era_pics_parser(r.text)
                all_links.append({link: pic_link})
                pic_link = ""

    template = loader.get_template('index.html')
    context = {'all_links': all_links}
    return HttpResponse(template.render(context, request))


def era_pics_parser(page_content):
    try:
        regex = r"\"https:..process\S*\""
        return re.search(regex, page_content).group(0).replace("\"", "")
    except:
        return ""
