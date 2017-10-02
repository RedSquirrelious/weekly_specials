from rest_framework import serializers
from  .models import Market

class MarketSerializer(serializers.ModelSerializer):
    '''maps model to JSON'''

    class Meta:
        '''maps serializer fields with model fields'''
        model = Market
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')