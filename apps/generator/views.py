# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

import string
import random
def id_generator(size=14, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def index(request):
	try:
		if request.session['attempt'] != None:
			return render(request, "generator/index.html")
		else:
			request.session['attempt']=0
			return render(request, "generator/index.html")
	except:
		return render(request, "generator/index.html")


def generate(request):
	print request.method
	if request.method == "GET":
		request.session['attempt'] += 1
		request.session['word'] = id_generator()
		print request.session['attempt']
		return redirect('/')
	else:
		return redirect('/')

def reset(request):
	request.session['attempt']=None
	return redirect('/')

