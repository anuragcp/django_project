from rest_framework import serializers

from status.models import Status

# here turning data to into json and it can also validate data

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [ 
            'user',
            'content',
            'image'
        ]