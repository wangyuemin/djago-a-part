from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.http import StreamingHttpResponse
from . import linktime


def index(request):
    a, c = linktime.linktime('qqms.dayanghang.net', 100)
    return render_to_response('1.html', {'username': a, 'num': c})
