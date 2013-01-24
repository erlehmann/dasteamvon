#!/usr/bin/python
# -*- coding: utf-8 -*-

# ⓒ 2012  Nils Dagsson Moskopp

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# Dieses Programm hat das Ziel, die Medienkompetenz der Leser zu
# steigern. Gelegentlich packe ich sogar einen handfesten Buffer
# Overflow oder eine Format String Vulnerability zwischen die anderen
# Codezeilen und schreibe das auch nicht dran.

from bottle import get, post, request, run, view
from functools import partial
from os import path, walk
from random import choice
from string import Template
from sys import argv
from urllib import quote

view = partial(view, quote=quote, name=argv[1])

def gibe_statuses(**kwargs):
    result = []
    with open('templates') as f:
        lines = f.readlines()
    for l in lines:
        template = Template(l)
        try:
            status = template.substitute(kwargs)
            result.append(status)
        except KeyError:
            pass
    return result

def gibe_variables():
    result = {}
    variables = [d for d in walk('variables').next()[2]]
    for v in variables:
        with open(path.join('variables', v)) as f:
            result[v] = f.readlines()
    return result

@get('/')
@view('index.tpl')
def index():
    variables = gibe_variables()
    request_dict = dict(request.query)
    request_dict = {k:v for k,v in request_dict.items() if v != ''}
    print request_dict
    statuses = gibe_statuses(**request_dict)
    return {
        'statuses': statuses,
        'variables': variables
    }

run(host='localhost', port=8080, reloader=True)
