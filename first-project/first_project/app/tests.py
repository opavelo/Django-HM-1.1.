from django.test import TestCase
import os

# Create your tests here.

msg = os.listdir(path='.')
item = ''
for i in msg:
    item = item + '\n' + i
print(item)