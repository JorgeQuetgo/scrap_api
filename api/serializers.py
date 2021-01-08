from rest_framework import serializers
from api.models import Product, Feature
from scrapping import product_scraper


class ProductSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id', 'code', 'name', 'brand', 'price', 'created_at', \
                 'updated_at', 'features'

    def get_features(self, obj):
        return Feature.objects.filter(product=obj).values('id', 'name',
                                                          'description')


class PageScrapSerializer(serializers.Serializer):
    link_list = serializers.ListField()

    def create(self, validated_data):
        # TODO refactor refactor refactor
        for link in validated_data["link_list"]:
            print(str(link))
            result = product_scraper.ProductScrapper(link)
            new_product = result.get_product_data()
            if Product.objects.filter(code=new_product['code']).first() is None:
                prod = Product.objects.create(**new_product)
                features = result.get_product_feature_data()
                for key, value in features.items():
                    Feature.objects.create(
                        product=prod,
                        name=key,
                        description=value
                    )
        return {"message": "products inserted"}
