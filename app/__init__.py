import os
from flask import Flask, jsonify, render_template, url_for, redirect
import sys  
import json
from functools import wraps
import time

from flaskext.markdown import Markdown

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)
Markdown(app, extensions=['fenced_code', 'tables'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BLOG_DIR = os.path.join(BASE_DIR, 'docs')

def get_category(DIR):
    for path, subdirs, files in os.walk(DIR):
        data = []
        desc = ''
        for dic in subdirs:
            for xpath, xsubdirs, xfiles in os.walk(os.path.join(path, dic)):
                md = os.path.join(xpath, 'desc.md')
                with open(md, 'r') as read_file:
                    desc = (read_file.read())
                    read_file.close()
                data.append({
                    "name":dic,
                    "desc":str(desc),
                    "url":dic.replace(' ', '-'),
                    "date_created": time.ctime(os.path.getctime(xpath)),
                    "date_modified": time.ctime(os.path.getmtime(xpath))
                })
        return data

def get_file_list(category_name):
    category = category_name.replace('-',' ')
    data = {}
    DIR = os.path.join(BLOG_DIR, category)
    check = os.path.isdir(DIR)
    if check:
        for path, subdirs, files in os.walk(DIR):
            desc = ''
            with open(os.path.join(path, 'desc.md'), 'r') as read_desc:
                desc = (read_desc.read())
                read_desc.close()
            data = {
                "category":category,
                "category_url":category_name,
                "desc":desc,
                "topic":[
                    {
                        "name":f.split('.')[0],
                        "url":f.replace(' ','-'), 
                        "date_created":time.ctime(os.path.getctime(os.path.join(path, f))),
                        "date_modified": time.ctime(os.path.getmtime(os.path.join(path, f)))
                    } for f in files if f != 'desc.md'
                ]
            }

            return data
    else:
        return False

def get_topic_detail(category_name, filename):
    category = os.path.join(BLOG_DIR, category_name.replace('-',' '))
    filename_new = filename.replace('-',' ')
    check = os.path.isfile(os.path.join(category, filename_new))
    read = ''
    if check:
        with open(os.path.join(category, filename_new), 'r') as read_file:
                read = (read_file.read())
                read_file.close()
        data = {
            "topic":filename,
            "description":read,
            "date_created":time.ctime(os.path.getctime(os.path.join(category, filename_new))),
            "date_modified": time.ctime(os.path.getmtime(os.path.join(category, filename_new)))
        }
        return data
    return check

@app.route('/')
def index():
    return render_template('index.html', category=get_category(BLOG_DIR))

@app.route('/<category>')
def category(category):
    data = get_file_list(category)
    if data == False:
        return redirect(url_for('index'))
    return render_template('api-topic.html', data=data)

@app.route('/<category>/<topic>')
def topic_detail(category, topic):
    data = get_topic_detail(category, topic)
    if data == False:
        return redirect(url_for('index'))
    return render_template('detail.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)