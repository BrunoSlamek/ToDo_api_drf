from rest_framework import serializers
from ToDo import models

class TodoSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = models.Todo
      fields = '__all__'
