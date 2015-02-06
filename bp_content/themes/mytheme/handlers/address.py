
"""Specifies address information for the app. 
"""
from google.appengine.api import search


states = {'name': 'hd televisions', 'children': []}
books = {'name': 'books', 'children': []}

ctree =  {'name': 'root', 'children': [states]}
