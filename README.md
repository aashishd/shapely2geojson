# shapely2geojson
This is a repo which contains code to convert shapely objects to geojson features

There are two methods primarily which can be used to convert shapely features
**shapely2geojson.transformer.transform**

This function takes in any shapely feature and transforms the coordinates and return them to you as how they would look in a geojson feature.


**shapely2geojson.transformer.get_feature** 

This function accepts any shapely feature and returns the corresponding geojson feature to it