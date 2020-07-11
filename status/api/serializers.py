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

    def validate_content(slef, value):
        if len(value) > 1000:
            raise serializers.ValidationError('This is not fair...')
        return value

    def validate(slef, data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or image is require')
        return data