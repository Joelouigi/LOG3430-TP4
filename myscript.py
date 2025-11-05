import os

os.system("git bisect start cd11759a673fd90853c4604dba8268af32bc2b2a e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
os.system("git bisect run python3.9 manage.py test")