from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description'] 
        # fields = '__all__' 
        # fields = ['id', 'title', 'logo', 'description'] 


        