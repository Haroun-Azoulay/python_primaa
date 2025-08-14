from PIL import Image
import geojson
def process(image: Image.Image) -> geojson.Feature:
"""
Detects Regions of Interest (ROIs) in an image.
The result is a geojson Feature containing a MultiPolygon geometry.
"""
...
