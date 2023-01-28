import uuid 
from pathlib import Path
import os

PROJECT_DIR = Path(__file__).resolve().parent

class BlogSaveing:
    def __init__(self, content):
        self.content = content
        self.filename = self.genreate_file_name()
        self.prefix = '''{% extends "layout/base.html" %}
                            {% block content %}'''
        self.suffix = '''{% endblock %}'''

    def save(self):
        # generate html file from content and store it in templates/blogs
        # TODO : handle html file generation :
        print(PROJECT_DIR)
        path = os.path.join(PROJECT_DIR, 'jinja2', 'blogs', self.filename)
        with open(path, 'w') as f:
            f.write(self.prefix + self.content + self.suffix)
            f.close()

    def genreate_file_name(self):
        return str(uuid.uuid4()).replace('-','')[4:14] + '.html'

    def getfilename(self):
        return self.filename