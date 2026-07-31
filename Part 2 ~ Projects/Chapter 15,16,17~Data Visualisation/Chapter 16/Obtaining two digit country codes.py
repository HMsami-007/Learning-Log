# Try importing from the direct plugin package paths
try:
    from pygal_maps_world.maps import COUNTRIES
except ImportError:
    try:
        from pygal_maps_world.i18n import COUNTRIES
    except ImportError:
        from pygal.maps.world import COUNTRIES

# Print out the sorted codes
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

