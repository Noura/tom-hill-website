#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

TARGET = 'to-deploy/'

pages = [ {
            'template': 'index.html',
            'path': '',
            'tabname': 'About',
          },
          {
            'template': 'lessons.html',
            'path': 'lessons',
            'tabname': 'Teaching'
          },
          {
            'template': 'contact.html',
            'path': 'contact',
            'tabname': 'Contact'
          }
        ]

def main():
    here = os.path.dirname(__file__)
    deploy_target = os.path.join(here, TARGET)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    if os.path.exists(deploy_target):
        shutil.rmtree(deploy_target)
    os.makedirs(deploy_target)
    shutil.copytree(os.path.join(here, 'static'), os.path.join(deploy_target, 'static'))

    # all content is in one file now; show and hide pages with JS
    current_page = pages[0]
    tem = templates.get_template('base.html')
    ctx = { 'pages': pages, 'current_page': current_page }
    out_dir = os.path.join(deploy_target, current_page['path'])
    if current_page['path']:
        os.makedirs(out_dir)
    with codecs.open(os.path.join(out_dir, 'index.html'), 'w') as out:
        out.write(tem.render(**ctx))

if __name__ == '__main__':
    main()
