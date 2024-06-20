import os
from django.contrib.gis.utils import LayerMapping
from .models import Sub_Counties

sub_counties_mapping = {
    'constituen': 'CONSTITUEN',
    'geom': 'MULTIPOLYGON',
}

sub_county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Data/nairobi_sub_counties.shp'))

def run(verbose=True):
    lm = LayerMapping(Sub_Counties, sub_county_shp, sub_counties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)