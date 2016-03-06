#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import handler
import generator

from flask import Flask

from config import config as C

app = Flask(__name__)


@app.route('/')
def index():
    return handler.index()


@app.route('/page/<int:page_id>', strict_slashes=False)
def page(page_id):
    return handler.page(page_id)


@app.route('/post/<string:year>/<string:month>/<string:day>/<post_name>')
def post(year, month, day, post_name):
    return handler.post(year, month, day, post_name)


@app.route('/feed', strict_slashes=False)
@app.route('/feed.xml')
@app.route('/atom.xml')
def feed():
    return handler.feed()


@app.route('/category/<string:c>', strict_slashes=False)
def category(c):
    return handler.category(c)


@app.route('/tag/<string:t>', strict_slashes=False)
def tag(t):
    return handler.tag(t)


@app.route('/<string:custom_page_name>', strict_slashes=False)
def custom_page(custom_page_name):
    return page_not_found(None)


@app.errorhandler(404)
def page_not_found(e):
    return handler.page_not_found()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print('Unknown arguments.')
        elif sys.argv[1] == 'generate':
            with app.app_context():
                generator.generate_static_site()
    else:
        app.run(debug=False, host=C.host, port=C.port)
