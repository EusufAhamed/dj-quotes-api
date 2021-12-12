from rest_framework import serializers

from quote_app.models import Quote, QuoteCategory

class QuoteCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    quote = serializers.StringRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        quote_category = QuoteCategory.objects.create(**validated_data)
        
        return quote_category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        
        return instance

class QuoteSerialaizerList(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quote = serializers.CharField(style={'base_template': 'textarea.html'})
    author = serializers.CharField(max_length=100)
    quote_category = serializers.StringRelatedField(read_only=True)
   

class QuoteSerialaizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    quote = serializers.CharField(style={'base_template': 'textarea.html'})
    author = serializers.CharField(max_length=100)
    quote_category = serializers.PrimaryKeyRelatedField(queryset=QuoteCategory.objects.all())

    def create(self, validated_data):
        quote = Quote.objects.create(**validated_data)

        return quote

    def update(self, instance, validated_data):
        instance.quote = validated_data.get('quote', instance.quote)
        instance.author = validated_data.get('author', instance.author)
        instance.quote_category = validated_data.get('quote_category', instance.quote_category)
        instance.save()
        
        return instance