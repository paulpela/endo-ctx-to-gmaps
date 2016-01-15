# endo-ctx-to-gmaps

Convert coords from Endomondo CTX files to a Google Maps waypoint JS array.

Made this quick and dirty hack to plot a heatmap of my training routes stored in Endomondo on a Google Map. 

Unfortunately, Endomondo does not have an API to access the data, so the only (?) way to do it is to export each exercise by hand to separate files, then somehow extract the waypoint data from those files to create a usable dataset. 

Google Maps requires just a simple array of `google.maps.LatLng()` coordinantes and it will do most of the work for you.

For more info on Google Maps Heatmap Layer feature go to: https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap

# Usage

1. Put `convert.py` in any suitable location.
2. Put all your CTX files to `./inputs` direcotry.
2. Run `python convert.py > output.js`
