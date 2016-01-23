import requests


def get_latlong(query):
    """Get lattitude and longitude for city
    @param string query: name of location to get latlon for
    @returns: location in latlon
    """
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?"
                     "address={}".format(query))
    location = r.json()['results'][0]['geometry']['location']

    return location


def get_height_ahn2(wkt_point):
    """get AHN2 height for WKT point geometry
    @param string wkt_point: point geometry as WKT.
    @returns: height in m NAP.
    """
    r = requests.get("https://nxt.staging.lizard.net/api/v2/raster-aggregates/?page_size=0&agg=curve&geom={}&raster_names=dem%2Fnl&srs=EPSG:4326&start=2015-01-14T21:01:01&stop=2015-01-21T21:01:01&window=3600000".format(wkt_point), verify=False)
    height = r.json()['data'][0]

    return height








def get_height_profile_ahn2(wkt_line):
    """get height profile for WKT line geometry
    @param string wkt_line: line geometry as WKT.
    @returns: array with [distance, height] pairs.
    """
    r = requests.get("https://nxt.staging.lizard.net/api/v2/raster-aggregates/?page_size=0&agg=curve&geom={}&raster_names=dem%2Fnl&srs=EPSG:4326&start=2015-01-14T21:01:01&stop=2015-01-21T21:01:01&window=3600000".format(wkt_line), verify=False)
    height_profile = r.json()

    return height_profile
