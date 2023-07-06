from rest_framework import serializers
from .models import society

class societySerializer(serializers.ModelSerializer):
    class Meta:
        model=society
        fields='__all__'

    def validate(self, attrs):
        maintenance_rating=attrs.get('maintenance_rating')
        if maintenance_rating:
            if maintenance_rating < 1 or maintenance_rating > 10:
                raise serializers.ValidationError('Enter maintenance_rating greater 1 and less than 10')
        return attrs   
