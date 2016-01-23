from shapely.geometry import mapping

from input_output import read_txt
from input_output import write_shape

from apis import get_latlong
from apis import get_height_ahn2

from apis import get_height_profile_ahn2

from geobuilder import point
from geobuilder import line


# files
in_cities = "cities.txt"
out_shape = "/home/arjen/Desktop/city_info_result.shp"

# we want our data to look like this
schema = {'geometry': 'Point',
          'properties': {'city': 'str',
                         'height_ahn2': 'float'}
                         }

# we want to store each result in a list
results = []

# read text file with cities
cities = read_txt(in_cities)

# main loop
for city in cities:
    city = city.strip()
    print city
    # get location from google
    location = get_latlong(city)
    # build geometry
    geometry = point(location['lng'], location['lat'])
    geometry_wkt = geometry.wkt
    print geometry_wkt
    # get info from lizard
    height_ahn2 = get_height_ahn2(geometry_wkt)
    # landuse = get_landuse(geometry_wkt)
    

    results.append({"geometry": mapping(geometry),
                    "properties": {"city": city,
                                   "height_ahn2": height_ahn2}
                                   })

# save results to a shapefile
write_shape(out_shape, schema, results)

# build a linestring from an array of cities
city_route = line([result['geometry']['coordinates'] for result in results])
city_route_wkt = city_route.wkt  # city_route.AsWKT()

# get height profile for linestring
height_profile_ahn2 = get_height_profile_ahn2(city_route_wkt)
