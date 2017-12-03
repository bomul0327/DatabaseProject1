from django import forms
#from django.db import connection
from .models import Manager

class manager_manage_form(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ('id', 'pw', 'pos', 'phonenum')

#def insert_sql(model):
#    with connection.cursor() as cursor:
#        cursor.execute("INSERT INTO cctv_manager('id', 'pw', 'pos', 'phonenum') VALUES(%s, %s, %s, %s)", [model.id], [model.pw], [model.pos], [model.phonenum])
#        row = cursor.fetchone()
#        return row
