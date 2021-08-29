from rest_framework import serializers
from .models import Todo
from .models import Person
from .models import PayCheck

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','firstName', 'lastName')

class PayCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayCheck
        fields = ('id','name', 'hourly', 'totalHours')