# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def create(request):
    return render(request, 'posts/create.html')
