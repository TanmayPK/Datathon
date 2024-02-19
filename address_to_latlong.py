from geopy.geocoders import Nominatim
import pandas as pd

mug = pd.read_parquet("data/mug_locations.parquet.gzip")
geolocator = Nominatim(user_agent="geoapiExercises")


def geocode_address(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


print(geocode_address("1600 Amphitheatre Parkway, Mountain View, CA"))
# mug[["Latitude", "Longitude"]] = mug["address_campus"].apply(
#     lambda x: pd.Series(geocode_address(x))
# )
