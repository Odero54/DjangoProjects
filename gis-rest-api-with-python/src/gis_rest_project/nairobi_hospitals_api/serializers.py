from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import NairobiSubCounties, NairobiHealthFacilities

class NairobiSubCountiesSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = NairobiSubCounties
        fields = "__all__"
        geo_field = "geom"

class NairobiHealthFacilitiesSerializer(GeoFeatureModelSerializer):

    def get_distance(self, obj):
        obj = serializers.CharField()
        return obj

    class Meta:
        model = NairobiHealthFacilities
        fields = "__all__"
        geo_field = "geom"
        read_only_fields = ["distance"]