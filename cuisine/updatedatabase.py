from home.models import *
import json
import os
from django.conf import settings  


json_file_path = os.path.join(settings.STATICFILES_DIRS[0], "items.json")
f= open(json_file_path)

data = json.load(f)

for i in data:
    itm = Items(
        name=i['title'],
        category=Category.objects.get(name='dairy'),
        desc=i['description'],
        left_in_stock=100,
        price=i['price'],
        img_path='images/'+i['type']+'/'+i['title']+'.jpg'
    )
    itm.save()
print("#############SUCESS##########")